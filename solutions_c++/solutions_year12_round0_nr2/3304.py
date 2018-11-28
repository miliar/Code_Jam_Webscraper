#include <stdio.h>
#include <string.h>

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	int ans = 0;
	scanf("%d",&T);
	int N,S,p;
	for( int i = 1; i <= T ; ++ i)
	{
		ans = 0;
		scanf("%d %d %d",&N,&S,&p);
		int sp = 0 ; 
		int sum ;
		for( int j = 0 ; j < N ; j ++ )
		{
			scanf("%d",&sum);
			if( sum >= 3* p )
			{
				ans ++;
				continue;
			}
			sum -= p;
			if( p - 1 >= 0 && sum >= 2*(p-1) )
			{
				ans ++;
			}
			else if( p-2 >= 0 && sum >= 2*(p-2))
			{
				sp ++;
			}
			
		}
		if( sp > S )
			sp = S;
		ans += sp;
		printf("Case #%d: %d\n",i,ans);
		
	}
	return 0;
}