#include<cstdio>
#include<iostream>
#include<algorithm>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<bitset>
#include<gmpxx.h>
#include<utility>

#define mp make_pair
#define pb push_back
#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,n-1)

typedef long long ll;
typedef mpz_class BigInt;

using namespace std;

int t,n,m;

struct node{
	map<string,node*> next;
};

int main(){
	cin>>t;
	repp(cas,1,t){
		cin>>n>>m;
		node *root=new node;
		rep(i,n){
			node *hoge=root,*fuga;
			string buf;
			cin>>buf;
			rep(j,buf.length())if(buf[j]=='/')buf[j]=' ';
			stringstream is(buf);
			string piyo;
			while(is>>piyo){
				if(hoge->next.find(piyo)!=hoge->next.end()){
					hoge=hoge->next[piyo];
				}else{
					fuga=new node;
					hoge->next[piyo]=fuga;
					hoge=fuga;
				}
			}
		}
		int ans=0;
		rep(i,m){
			node *hoge=root,*fuga;
			string buf;
			cin>>buf;
			rep(j,buf.length())if(buf[j]=='/')buf[j]=' ';
			stringstream is(buf);
			string piyo;
			while(is>>piyo){
				if(hoge->next.find(piyo)!=hoge->next.end()){
					hoge=hoge->next[piyo];
				}else{
					fuga=new node;
					hoge->next[piyo]=fuga;
					hoge=fuga;
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}
