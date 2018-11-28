#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GI64 ({int64 t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define rf(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long int64;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

//char ch;
set < string > dict;
vector < set <char> > ques;

int L,D,N;

bool go(string s){
	f(i,0,L)if(ques[i].find(s[i])==ques[i].end())return 0;
	return 1;
}

int main(){
	string st;
	L=GI,D=GI,N=GI;
	int cnt=0;
	f(i,0,D)st=GS,dict.insert(st);
	f(i,0,N){
		cnt++;
		ques.clear();
		st=GS;
		ques.resize(L);
		int pos=0,n=sz(st),j=0;
		while(1){
			if(j==n)break;
			if(st[j]=='('){
				j++;
				while(st[j]!=')')ques[pos].insert(st[j++]);
				j++;
				pos++;
			}
			else ques[pos++].insert(st[j++]);
		}
		int ans=0;
		tr(k,dict)ans+=go(*k);
		printf("Case #%d: %d\n",cnt,ans);
	}
	return 0;	
}
