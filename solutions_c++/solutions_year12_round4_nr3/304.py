#include <cstdio>
#include <stack>
#include <cmath>
using namespace std;

#define MAXB 2100
#define MAXH 1000000000
int tallest[MAXB];
int heights[MAXB];
stack<int> hs;
stack<int> ds;
bool can;

int main ()
{
	int T, N;
	int i, j;
	scanf("%d",&T);
	
	for ( int cnt = 1; cnt <= T; cnt++ )
	{
		scanf("%d",&N);
		can = true;
		
		for ( i = 1; i < N; i++ ) 
		{
			scanf("%d",&tallest[i]);
			//printf("%d ",tallest[i]);
			heights[i] = -1;
		}
		
		heights[N] = -1;
		while ( !ds.empty() ) ds.pop();
		while ( !hs.empty() ) hs.pop();
		heights[1] = MAXH;
		hs.push(MAXH);
		ds.push(N+1);
		heights[tallest[1]] = MAXH;
		hs.push(MAXH);
		ds.push(tallest[1]);
		//printf("\n%d\n",tallest[1]);
		int newb, newh, th, td;
		
		for ( i = 2; i < N; i++ )
		{
			if ( hs.top() == heights[i] ) { hs.pop(); ds.pop(); }
			if ( heights[i] == -1 ) heights[i] = 0;
			
			newb = tallest[i];
			//printf("\nhi %d %d %d\n",newb,ds.top(),heights[N]);
			if ( newb > ds.top() ) { can = false; break; }
			if ( heights[newb] != -1 ) continue;
			
			th = hs.top();
			td = ds.top();
			
			newh = ceil( ((1.0 * (newb-i))/(td-i)*(th-heights[i])) ) + heights[i];
			heights[newb] = newh;
			hs.push(newh);
			ds.push(newb);
		}
		
		if ( heights[N] == -1 ) heights[N] = 0;
		printf("Case #%d:",cnt);
		if ( !can ) printf(" Impossible\n");
		else
		{
			for ( i = 1; i <= N; i++ )
				printf(" %d",heights[i]);
			printf("\n");
		}
	}
}