
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

struct st{
	double prob;
	string type;
	st *next[2];
};

typedef pair<st *, char *> parsed;
vector<st *> malloced;

#define f first
#define s second

parsed maketree(char *p){
	//cout<<"maketree <"<<p<<">"<<endl;
	st *v=new st;malloced.push_back(v);

	while(*p==' ')p++;
	v->prob=strtod(p+1,&p);

	while(*p==' ')p++;
	if(*p==')'){
		return parsed(v,p+1);
	}

	v->type=strtok(p," ");
	p=strtok(NULL,"");

	parsed x=maketree(p);
	p=x.s;
	v->next[0]=x.f;

	parsed y=maketree(p);
	p=y.s;
	v->next[1]=y.f;

	while(*p==' ')p++;
	return parsed(v,p+1);
}

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int line;scanf("%d ",&line);
		string str;
		for(int i=0;i<line;i++){
			string tmp;getline(cin,tmp);
			str+=" "+tmp;
		}
		//cout<<str<<endl;

		parsed ret=maketree((char *)str.c_str());

		static int npr=1;
		printf("Case #%d:\n",npr++);

		int n;scanf("%d ",&n);
		while(n--){
			string type;getline(cin,type);
			//cout<<type<<endl;
			string name=strtok((char *)type.c_str()," ");
			char *tmp=strtok(NULL," ");
			int cnt=atoi(tmp);

			set<string> mp;
			for(int i=0;i<cnt;i++){
				char *type=strtok(NULL," ");
				mp.insert(type);
			}

			//search!

			double prob=1.0;
			st *now=ret.f;

			while(1){
				prob*=now->prob;
				if(now->type.length()==0)break;

				if(mp.count(now->type))now=now->next[0];
				else now=now->next[1];
			}

			printf("%.10f\n",prob);
		}

		for(int i=0;i<malloced.size();i++)delete malloced[i];
		malloced.clear();
	}
	return 0;
}
