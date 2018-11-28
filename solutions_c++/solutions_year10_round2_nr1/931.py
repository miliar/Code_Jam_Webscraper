#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;
typedef struct node{
	map<string,struct node *> next;
};

vector <string> v;
void create(struct node* current, int i){
	if (i<v.size()){
		if (current->next.find(v[i])==current->next.end()){
			current->next[v[i]]=new struct node;
		}
		create(current->next[v[i]],i+1);
	}
}
int show(struct node *current,int i){
	map<string,struct node*>::iterator it;
	int ii;
	int k=0;
	for (it=current->next.begin();it!=current->next.end();it++)
	{
		//for(ii=0;ii<i;ii++)
		//printf(" ");
		k++;
		//printf("%s\n",it->first.c_str());
		k+=show(it->second,i+1);
	}
	return k;
}
int main(){
	int T,t;
	int n,m;
	int i,j;
	int k1,k2;
	char s[200];
	string p;
	scanf("%d",&T);
	for (t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&m);
		struct node* home=new struct node;
		for (i=0;i<n;i++){
			scanf("%s",s);
			for (j=0;s[j];j++)
			if (s[j]=='/') s[j]=' ';
			stringstream ss(s);
			v.clear();
			while(ss>>p)
				v.push_back(p);
			create(home,0);
		}
		k1=show(home,0);
		for (i=0;i<m;i++){
			scanf("%s",s);
			for (j=0;s[j];j++)
			if (s[j]=='/') s[j]=' ';
			stringstream ss(s);
			v.clear();
			while(ss>>p)
				v.push_back(p);
			create(home,0);
		}
		k2=show(home,0);
		printf("%d\n",k2-k1);
	}
  return 0;
}
