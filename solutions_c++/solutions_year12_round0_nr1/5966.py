#include<iostream>
#include<algorithm>
#include<functional>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<string>
#include<queue>
#include<stack>
#include<set>
#include<vector>
#include<sstream>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define REQ(i,n) for(int i=0;i<=(int)(n);i++)
#define FOR(i,k,n) for(int i=(k);i<(int)(n);i++)
#define FEQ(i,k,n) for(int i=(k);i<=(int)(n);i++)
#define SWAP(type,x,y) do{type t=x;x=y;y=t;}while(0)
typedef long long ll;
typedef unsigned long long ull;

map<char,char> F;
string go="ahilnoqruwzyfcbkmxsevpdjgt";
string en="yxdgbkztjfqacehilmnoprsuvw";
char G[26];

void init()
{
	for(int i=0;i<en.length();i++){
		G[go[i]-'a']=en[i];
	}
}

char trans(char c)
{
	return (c==' ')?' ':G[c-'a'];
}

int main()
{
	init();

	int N;
	cin>>N;
	cin.ignore();
	for(int T=1;T<=N;T++){
		string g;
		getline(cin,g);
		string res="";
		for(int i=0;i<g.length();i++){
			res+=trans(g[i]);
		}
		printf("Case #%d: %s\n",T,res.c_str());
	}
	return 0;
}
