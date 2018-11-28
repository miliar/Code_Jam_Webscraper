#include <iostream>
#include <vector>
#define MAXN 1024

using namespace std;

bool f[MAXN];
int prime[MAXN];
vector <int> vc[MAXN];
int k;

void init ()
{
	int i, j;
	memset(f,0,sizeof(f));
	for ( i = 2; i < 100; i ++ )
	{
		if ( f[i] == 0 )
		{
			for ( j = i * i; j < MAXN; j += i )
			{
				f[j] = 1;
			}
		}
	}
	for ( i = 2; i < MAXN; i ++ )
	{
		if ( f[i] == 0 )
			prime[k++] = i;
	}
}

int father[MAXN];

int find(int k)
{
	if (k == father[k])
		return k;
	return father[k] = find(father[k]);
}

int main (void)
{
	freopen ("B-small-attempt0.in","r",stdin);
	freopen ("2.out","w",stdout);
	int T;
	int Case = 0;
	int i, j;
	int A, B, P;
	scanf ("%d",&T);
	k = 0;
	init ();
	while ( T -- )
	{
		Case ++;
		scanf ("%d%d%d",&A,&B,&P);
		for ( i = A; i <= B; i ++ )
			father[i] = i;
		for ( i = 0; i < k; i ++ )
			if ( prime[i] >= P )
				break;
		int t1, t2;
		for ( ; i < k && prime[i] <= B ; i ++ )
		{
			for ( int i1 = A; i1 <= B; i1 ++ )
			{
				if ( i1 % prime[i] != 0 ) continue;
				for ( int j1 = i1+1; j1 <= B; j1 ++ )
				{
					if ( j1 % prime[i] != 0 )
						continue;
					t1 = find(i1);
					t2 = find(j1);
					if ( t1 != t2 )
						father[t2] = t1;
				}
			}
		}
		int ans = 0;
		memset(f,0,sizeof(f));
		for ( i = A; i <= B; i ++ )
		{
			if ( father[i] == i )
			{
				ans ++;
				f[i] = 1;
			}
		}
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}