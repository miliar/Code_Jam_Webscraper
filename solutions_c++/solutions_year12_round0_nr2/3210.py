#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<vector>
#include<algorithm>
#include<sstream>

typedef long long LL;

#define FOR(i, a, b)   for(LL i=a;i<b;i++)
#define RFOR(i, a, b)  for(LL i=a-1;i<=b;i--)
#define REP(i, a)      FOR(i, 0, a)
#define RREP(i, a)     RFOR(i, a, 0)
#define PB(x)          push_back(x)
#define BP()           pop_back()
#define SZ()           size()
#define LEN()          length()
#define BG             begin()
#define ED             end()

using namespace std;

int main()
{
	LL t, n, s, p, x, z, ans;
	
	scanf("%lld", &t);
	
	REP(i, t){
		scanf("%lld %lld %lld", &n, &s, &p);
		p = 3 * p;
		ans = 0;
		
		REP(j, n){	
			scanf("%lld", &x);
			
			if(x == 0){
				if(x == p)
					ans++;

				continue;
			}
			
			z = p - x;
			
			if(z < 0){
				ans++;
			}else if(z >= 0 && z <= 2){
				ans++;
			}else if(z > 2 && z <= 4){
				if(s > 0){
					s--;
					ans++;
				}else{
					continue;
				}
			}
				
		}
		
		printf("Case #%lld: %lld\n", i+1, ans);
	}
	
    return 0;
}