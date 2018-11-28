#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long LL;

LL sum, a[1010];
LL R, K;
int n;

int skip[1010];
LL lft[1010];

int main ()
{
//	freopen("x.in", "r", stdin);
//	freopen("x.out", "w", stdout);
	int cases, index; scanf("%d",&cases);
	for(index = 0; index < cases; index ++ )
	{
		scanf("%lld%lld%d", &R, &K, &n);
		sum = 0;
		for(int i = 0; i < n; i ++) {
			scanf("%lld", a+i);
			sum += a[i];
		}

//		if( index != 27 ) continue;
		
		memset( skip, 0xff, sizeof( skip ) );

		int start = 0;
		LL ans = 0;
		while(R){
			int pre = start;
			LL d = K;
			if( d >= sum ) {
				start = pre;
				d -= sum;
			} else {
				for( ; d - a[start] >= 0; start = (start + 1) % n ) d -= a[start];
			}
			if( skip[pre] == -1 ) { 
				lft[pre] = d;
				skip[pre] = start;
				R -- ;
				ans += ( K - lft[pre] );
			} else // get a looop
			{
				LL tot = 0; start = pre; int cnt = 0;
				do {
					tot += ( K - lft[pre] );
					pre = skip[pre];
					cnt ++ ;
				} while( pre != start );
//				printf("%lld %d\n",R, cnt);
				ans += tot * (R / cnt);
				R %= cnt;
				
				while( R ) {
					ans += ( K - lft[pre] );
					pre = skip[pre];
					R -- ;
				}

				break;
			}
			
		}
		printf("Case #%d: %lld\n", index+1, ans);
	}
	return 0;
}
