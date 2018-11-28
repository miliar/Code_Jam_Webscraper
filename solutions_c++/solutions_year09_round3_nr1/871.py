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
typedef vector< long long > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

//char ch;

int main(){
	int t=GI;
	int cnt=0;
	string s;
	while(t--){
		cnt++;
		map<char,int>mp;
		for(char cc='a';cc<='z';cc++)mp[cc]=-1;
		for(char cc='0';cc<='9';cc++)mp[cc]=-1;
		string s=GS;
		int x=0;
		bool seen[10];
		SET(seen,0);
		mp[s[0]]=1,seen[1]=1;
		f(i,1,sz(s)){
			if(mp[s[i]]>=0)continue;
			//if(!(s[i]>='a' && s[i]<='z'))continue;
			f(j,0,10){
				if(seen[j])continue;
				seen[j]=1;
				mp[s[i]]=j;
				break;
			}	
		}
		//f(i,0,sz(s))cout<<mp[s[i]]<<" ";
		string ans="";
		f(i,0,sz(s))ans+=(mp[s[i]]+'0');
		int maxval=-1;
		f(i,0,sz(ans))maxval=max(maxval,(ans[i]-'0'));
		maxval++;
		int64 answer=0,ret=1;
		for(int i=sz(ans)-1;i>=0;i--){
			answer+=((int64)(ans[i]-'0')*ret);
			ret=ret*(int64)(maxval);
		}
		cout<<"Case #"<<cnt<<": "<<answer<<endl;
	}
	return 0;	
}
