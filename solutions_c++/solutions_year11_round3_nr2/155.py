#include<cstdio>
#include<vector>
#include<deque>
#include<cmath>
#include<queue>
#include<set>
#include<cstring>
#include<string>
#include<algorithm>

#define pb push_back
#define mp make_pair
#define ll long long

using namespace std;
const int maxn = 1000105;

ll i , j , test , cases , v[maxn] , w[maxn] , n , c , L , speed[maxn] , t;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%lld",&test);
	
	for( cases = 1 ; cases <= test ; ++cases ) { 
		
		printf("Case #%d: ",cases);
		
		scanf("%lld %lld %lld %lld",&L,&t,&n,&c);
		
		for( i = 1 ; i <= c ; ++i ) 
			scanf("%d",&w[i]);
		
		for( i = 1 ; i <= n ; ++i ) {
			if ( i % c != 0 )
				v[i] = w[i % c];
			else
				v[i] = w[c];
		}
		
		ll cnt = 0 , costA = 0 , costB = 0 , first_case = 0 , second_case = 0;
		ll time = 0;
		int La , Lb;
		
		for( i = 1 ; i <= n && time + 2 * v[i] < t; ++i ) 
			time += 2 * v[i];
			
		first_case = time + (t - time)  + (v[i] - (t - time) / 2);
		second_case = time + 2 * v[i];
		
		for( j = i + 1 ; j <= n ; ++j ) 
			speed[++cnt] = v[j];
		
		sort( speed + 1 , speed + cnt + 1);
		
		La = L - 1 , Lb = L;
		
		for( j = cnt ; j >= 1 ; --j ) {
			if ( La > 0 )
				costA += speed[j];
			else 
				costA += 2 * speed[j];
			
			if ( Lb > 0 ) 
				costB += speed[j];
			else
				costB += 2 * speed[j];
			La-- , Lb--;
		}
		
		if ( L == 0 )
			printf("%lld\n",second_case + costB);
		else
			printf("%lld\n", min(costA + first_case, costB + second_case));
	}
	
return 0;
}