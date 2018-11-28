# include <stdio.h>
# include <string.h>


int n, tot ;
int d[10010], len[10010] ;

int vis[10010] ;
int q[1000100][2] ;


int min(int a, int b){return a<b?a:b;}


int bfs()
{
	int front = 0, rear = 0 ;
	int idx, lll, ll, i ;
	q[rear][0] = 0, q[rear][1] = min(d[0], len[0]) ;
	vis[0] = min(d[0], len[0]) ;
	rear++ ;
	
	
	while (front != rear)
	{
		idx = q[front][0], ll = q[front][1] ;
	//	printf ("%d, %d\n", idx, ll) ;
		if (tot - d[idx] <= ll) return 1 ;
		front++ ;
		for (i = idx+1 ; d[i] - d[idx] <= ll && i < n ; i++)
		{
			lll = min(d[i]-d[idx], len[i]) ;
			if (lll <= vis[i]) continue ;
			vis[i] = lll ;
			q[rear][0] = i, q[rear][1] = lll ;
			rear++ ;
		}
		for (i = idx-1 ; d[idx] - d[i] <= ll  && i >= 0 ; i--)
		{
			lll = min(d[idx]-d[i], len[i]) ;
			if (lll <= vis[i]) continue ;
			vis[i] = lll ;
			q[rear][0] = i, q[rear][1] = lll ;
			rear++ ;
		}
	}
	
	return 0 ;
}


int test()
{
	memset (vis, 0, sizeof(vis)) ;
	return bfs() ;
}


int main ()
{
	int i, T , nCase =1 ;
	freopen ("A-small-attempt1.in", "r", stdin) ;
	freopen ("aout.txt", "w", stdout) ;
	scanf ("%d", &T) ;
	while (T--)
	{
		scanf ("%d", &n) ;
		for (i = 0 ; i < n ; i++)
			scanf ("%d%d", &d[i], &len[i]) ;
		scanf("%d", &tot) ;
		printf ("Case #%d: %s\n", nCase++, test()?"YES" : "NO") ;
	}
	return 0 ;
}
