//By Lin
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std; 

int		main()
{
	int cas , tt = 0; 
	scanf("%d", &cas ); 
	while ( cas -- ) 
	{
		int	n,x,s,p, ans = 0; 
		scanf("%d%d%d", &n ,&s , &p ); 
		int t1 , t2;
		t1 = t2 = 0; 
		for (int i = 0; i<n; i++)
		{
			scanf("%d", &x );
			if ( (x == 3*p-4 && x>=2 ) || (x == 3*p-3 && x>=1 ) ) t1++; 
			if ( x >= 3*p-2 ) t2++; 
		}
		printf("Case #%d: %d\n" , ++tt , min(t1,s)+t2 );
	}
	return 0; 
}
