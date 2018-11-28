#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;

struct Node{
	string s;
	Node *son,*bro;
	Node(){}
	Node(const string &s,Node *son,Node *bro):s(s),son(son),bro(bro){}
};
const int Max=101000;
vector<string> path;
Node node[Max],*nn;
void getpath(){
	string tmp;
	cin>>tmp;
	int len=tmp.length();
	path.clear();
	for(int i=1,j=1;j<len;){
		while(i<len&&tmp[i]!='/') ++i;
		path.push_back(tmp.substr(j,i-j));
		j=i++;
	}
}
int insert(){
	Node *cur=node,*p;
	for(int i=0;i<path.size();++i){
		for(p=cur->son;p;p=p->bro){
			if(p->s==path[i]) break;
		}
		if(!p){
			int cnt=0;
			for(;i<path.size();++i,++cnt){
				*nn=Node(path[i],NULL,cur->son);
				cur->son=nn;
				cur=nn++;
			}
			return cnt;
		}
		cur=p;
	}
	return 0;
}
int main(){
	int TT;
	cin>>TT;
	for(int cas=1;cas<=TT;++cas){
		int N,M;
		cin>>N>>M;
		nn=node;
		node[0]=Node("",NULL,NULL);
		for(int i=0;i<N;++i){
			getpath();
			insert();
		}
		int ans=0;
		for(int i=0;i<M;++i){
			getpath();
			ans+=insert();
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
