#include<cstdio>
#include<algorithm>
const int INF = 2000000;
using namespace std;

int ind , t ,  n , i , a;

int main()
{
	freopen("candy.in","r",stdin);
	freopen("candy.out","w",stdout);
	
	scanf("%d",&t);
	
	for( ind = 1 ; ind <= t ; ++ind ) {
		int sum = 0 , xsum = 0 , mins = INF;
		scanf("%d",&n);
		
		for( i = 1 ; i <= n ; ++i ) { 
			scanf("%d",&a);
			mins = min( a , mins );
			xsum ^= a , sum += a;
		}
		
		printf("Case #%d: ", ind);
		
		if ( xsum ) 
			printf("NO\n");
		else
			printf("%d\n",sum - mins);
	}
	
return 0;
}