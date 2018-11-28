#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
using namespace std;

typedef long long ll;
typedef long double ld;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define cs c_str()

#define GI ({long long t;scanf("%lld",&t);t;})
#define COUNT(f,x) ({int _=0;f _+=(x);_;})
#define EXISTS(f,x) ({int _=0;f if(x) {_=1;break;}_;})
#define ALL(f,x) (!EXISTS(f,!(x)))
#define MIN(f,x) ({LL _=LINF;f _<?=(x);_;})
#define MAX(f,x) (-MIN(f,-(x)))

int main()
{
	ll t; t = GI;
	ll cas = 1;
	ll P,K,L;
	while(t--)
	{
		P=GI; K=GI;L=GI;
		vector<ll> freq(L);
		REP(i,L) freq[i] = GI;
		//EACH(x,freq) cout<<"::"<<*x<<" ";
		ll keypad[K][P];
		memset(keypad,-1,sizeof(keypad));
		sort(freq.begin(),freq.end());
		reverse(freq.begin(),freq.end());
		//cout<<"sorted\n";
		//EACH(x,freq) cout<<*x<<" ";
		//cout<<endl;
		ll count = 0;
		if(K*P<L) { cout<<"Case #"<<cas<<": "<<"Impossible\n"; return 0; }
		ll ans=0; ll level = 1;
		int c=0;
		while(1)
		{
			FOR(j,0,K) { /*cout<<freq[c]<<" has level "<<level<<endl;*/ ans += freq[c]*level; c++; if(c==L) goto end;}
			level++;
		}
		
		/*
		REP(j,P)
			REP(k,K)
			if(keypad[k][j]==-1) 
			{ 
			  keypad[k][j]=freq[count];
			  count++; 
			  if(count==L) goto end;
			}
		
		end:
		REP(i,K) { REP(j,P) cout<<keypad[i][j]<<" "; cout<<endl; }
		
		ll ans=0;
		
		REP(i,K)
			REP(j,P)
			   if(keypad[i][j]==-1) continue;
			   else ans+=keypad[i][j]*(j+1);		*/
		end:
		cout<<"Case #"<<cas++<<": "<<ans<<endl;	
	}			
	return 0;
}
