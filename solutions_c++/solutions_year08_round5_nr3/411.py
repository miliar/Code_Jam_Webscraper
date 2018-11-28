#include <stdio.h>

const int MAX = 12;
const int MAX2 = 5000;

int m;
int n;
char s[MAX][MAX];
int deg2[MAX];
int val[MAX2];
int dp[MAX2];
int dpn[MAX2];

void Read()
{
	int i;
	int j;

	for (i=0; i<MAX; i++)
		for (j=0; j<MAX; j++)
			s[i][j] = 0;

	scanf("%d%d", &m, &n);
	for (i=0; i<m; i++)
		scanf("%s", s[i]);
}

bool HasBit(int num, int bit)
{
	return (((num) & (deg2[bit])) != 0);
}

bool IsValid(int mask, char row[MAX])
{
	int i;

	for (i=0; i<n; i++)
		if (row[i] == 'x' && HasBit(mask, i))
			return false;

	for (i=0; i+1<n; i++)
		if(HasBit(mask, i) && HasBit(mask, i+1))
			return false;

	return true;
}

bool IsGood(int mask1, int mask2)
{
	for (int i=0; i+1<n; i++)
		if (HasBit(mask1, i) && HasBit(mask2, i+1) || 
			HasBit(mask1, i+1) && HasBit(mask2, i))
			return false;

	return true;
}

void Solve()
{
	int i;
	int j;
	int k;

	for (i=0; i<MAX2; i++)
		dp[i] = dpn[i] = 0;

	for (i=0; i<deg2[n]; i++)
	{
		if(IsValid(i, s[0]))
			dp[i] = val[i];
		else
			dp[i] = 0;
	}

	for (k=1; k<m; k++)
	{
		for (i=0; i<deg2[n]; i++)
		{
			if(IsValid(i, s[k]))
			{
				int max = 0;
				int cur;

				for (j=0; j<deg2[n]; j++)
				{
					cur  = val[i] + dp[j];
					if (max < cur && IsGood(i, j))
						max = cur;
				}

				dpn[i] = max;
			}
			else
				dpn[i] = 0;
		}

		for (i=0; i<deg2[n]; i++)
		{
			dp[i] = dpn[i];
			dpn[i] = 0;
		}
	}

	int ans = 0;
	for (i=0; i<deg2[n]; i++)
		if (ans < dp[i])
			ans = dp[i];

	printf("%d\n", ans);
}

int main()
{
	freopen("3.in", "rt", stdin);
	freopen("3.out", "wt", stdout);

	int i;
	deg2[0] = 1;
	for(i=1; i<MAX; i++)
		deg2[i] = deg2[i-1]*2;
	for (i=0; i<deg2[MAX-1]; i++)
	{
		int num = i;

		for(int j=0; j<20; j++)
		{
			val[i] += num % 2;
			num /= 2;
		}
	}

	int t;
	int n;

	scanf("%d", &n);
	for (t=1; t<=n; t++)
	{
		Read();		
		printf("Case #%d: ", t);
		Solve();
	}

	return 0;
}

