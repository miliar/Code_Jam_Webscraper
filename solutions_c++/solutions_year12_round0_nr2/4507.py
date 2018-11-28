#include <iostream>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <cassert>
#define FOR(i,a,n) for(int i=(a),_n=(n); i<=_n; i++)
#define FORD(i,a,n) for(int i=(a),_n=(n); i>=_n; i--)
#define REP(i,n) for(int i=0,_n=(n); i<_n; i++)
#define REPD(i,n) for(int i=n-1; i>=0; i--)
#define EACH(it, con) for(__typeof((con).begin()) it = (con).begin(); it!=(con).end(); it++)
#define pb push_back
#define TWO(n) ( 1ll << (n) )
#define ON(bit,n) (bit | TWO(n))
#define OFF(bit,n) (bit & (~TWO(n)))
#define CONTAIN(bit,n) ((bit) & TWO(n))
#define SET(mem,val) memset(mem,val,sizeof mem)
#define pb push_back
#define all(con) con.begin(),con.end()
#define ABS(n) ((n)<0?-(n):(n))
using namespace std;

int main()
{
	int test;
	scanf("%d",&test);
	FOR(cs,1,test){
		int a,n,s,p;
		scanf("%d %d %d",&n,&s,&p);
		int ans=0;
		REP(i,n){
			scanf("%d",&a);
			int base = a/3;
			int sisa = a%3;
			
			if(base >= p)ans++;
			else if(sisa >= 1 && base+1 >= p)ans++;
			else if(s){
				if( (sisa == 0 && base+1 >= p && a>=3) || (sisa == 2 && base+2 >=p && a>=2)){s--;ans++;}
			}
			
			
			//cerr << a << " " << ans << " " << s << endl;
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}

