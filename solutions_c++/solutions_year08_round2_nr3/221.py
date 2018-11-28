#include <iostream>
#include <vector>
#define MAXN 5010

using namespace std;

int spN[MAXN];
int spB[MAXN];
int ans[MAXN];

void init ( int n )
{
	int i;
	for ( i = 1; i <= n; i ++ )
	{
		spN[i] = i + 1;
		spB[i] = i - 1;
	}
	spB[1] = n;
	spN[n] = 1;
}

void Solve ( int n )
{
	int sp = 1;
	int i;
	for ( i = 1; i <= n; i ++ )
	{
		int x = 0;
		for ( ; ;sp = spN[sp] )
		{
			x ++;
			if ( x == i )
			{
				int temp = sp ;
				spN[spB[temp]] = spN[sp] ;
				spB[spN[sp]] = spB[temp];
				ans[sp] = i;
				sp = spN[sp];
				break;
			}
		}
	}
}

void ansQuest ()
{
	int i;
	int Q;
	int Case;
	int m;
	scanf ("%d",&m);
	for ( i = 0; i < m; i ++ )
	{
		scanf ("%d",&Q);
		printf (" %d",ans[Q]);
	}
	printf ("\n");
}

int main (void)
{
	freopen ("c.in","r",stdin);
	freopen ("3.out","w",stdout);
	int T;
	int i, j;
	int n, Case = 0;
	scanf ("%d",&T);
	while ( T -- )
	{
		Case ++;
		scanf ("%d",&n);
		init (n);
		Solve(n);
		printf("Case #%d:",Case);
		ansQuest();
	}
	return 0;
}