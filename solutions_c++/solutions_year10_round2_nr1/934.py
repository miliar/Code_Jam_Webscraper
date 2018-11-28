#include<cstdio>
#include<map>
#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<string>
#include<cstring>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a;i < b;++i)
#define FORZ(i,t) for(int i = 0;i < t;++i)
#define PB push_back

typedef long long LL;

struct Node{
	map<string,Node *> next;
};

int insert(Node *tmp,string path){

	int ret = 0;
	FOR(i,0,path.size())
		if(path[i] == '/')
			path[i] = ' ';
	vector<string> v;
	v.clear();

	string s;
	stringstream ss;
	ss.clear();
	ss << path;
	
	while(ss >> s) v.PB(s);

	for(int i = 0;i < v.size();++i)
		if(tmp->next.count(v[i]))
			tmp = tmp -> next[v[i]];
		else {
			tmp -> next[v[i]] = new Node();
			tmp = tmp -> next[v[i]];
			ret ++;
		}
return ret;
}

void del(Node *tmp)
{
	if(tmp -> next.size() == 0){
		delete(tmp);
		return;
	}
		for(typeof(tmp-> next.begin() ) it = tmp -> next.begin();it != tmp -> next.end();++it)
			del(it -> second);
}

int main(){
	int test = GI;
	
	FOR(i,1,test+1){
		printf("Case #%d: ",i);
		Node *root = new Node();
		
		int N = GI,M =GI;				
		string s;
		

		FOR(j,0,N){
			cin >> s;
			insert(root,s);
		}
		int ans = 0;
		FOR(j,0,M){
			cin >> s;
			ans += insert(root,s);
		}
		printf("%d\n",ans );
		del(root);
		delete(root);
	}

	return 0;
}
