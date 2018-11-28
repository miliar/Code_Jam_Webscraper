#include<cstdio>
#include<vector>
#include<deque>
#include<cmath>
#include<queue>
#include<set>
#include<cstring>
#include<string>

#define pb push_back
#define mp make_pair
#define ll long long

using namespace std;

int i , j , n , l , h , v[1000] , t , cases;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&t);
	
	for( cases = 1 ; cases <= t ; ++cases ) { 
		
		int ans = -1;
		
		printf("Case #%d: ",cases);
		
		scanf("%d %d %d",&n,&l,&h);
		for( i = 1 ; i <= n ; ++i ) 
			scanf("%d",&v[i]);
		
		for( i = l ; i <= h ; ++i )  {
			
			bool ok = true;
			
			for( j = 1 ; j <= n ; ++j ) 
				if ( v[j] % i != 0 && i % v[j] != 0 ) 
					ok = false;
			if ( ok ) {
				ans = i;
				break;
			}
		}
		
		if ( ans > -1 ) 
			printf("%d\n",ans);
		else
			printf("NO\n");
	}
	
return 0;
}