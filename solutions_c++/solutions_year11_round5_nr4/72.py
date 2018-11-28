#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

ll perf(ll c){
	ll a = 0;
	ll b = 1ll<<31;
	while(a<=b){
		ll s = (a+b)/2;
		if(s*s==c) return s;
		if(s*s>c) b = s-1;
		else a = s +1;
	}
	return -1;
}

int main(){ 
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int tc;
	cin>>tc;
	REP(TC,tc){
		string s;
		cin>>s;
		int num = 0;
		REP(i,s.size()) if(s[i]=='?') num++;
		ll res = -1;
		REP(mask,1<<num){
			ll val =  0;
			int pos = 0;
			ll st = 1;
			for(int i=int(s.size())-1;i>=0;i--){
				if(s[i]=='0'){}
				else if(s[i]=='1') val += st;
				else if(mask&(1<<pos)){
					val += st;
					pos++;
				}else pos++;
				st<<=1;
			}
			ll t = perf(val);
			if(t!=-1) {res=t*t;break;}
		}
		printf("Case #%d: ",TC+1);
		s="";
		while(res){
			s.pb(char('0'+(res%2)));
			res/=2;
		}
		reverse(s.begin(),s.end());
		cout<<s<<endl;

	}
#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif
	return 0;
}
