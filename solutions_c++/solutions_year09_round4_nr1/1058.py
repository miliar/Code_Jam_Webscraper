#include <cstdio>

int n;
char arr[50][50];

void swap(int i, int j)
{
	for (int k = 0; k < n; k++)
	{
		char temp = arr[i][k];
		arr[i][k] = arr[j][k];
		arr[j][k] = temp;
	}
}

int len(int row)
{
	int res = -1;
	for (int i = 0; i < n; i++)
		if (arr[row][i] == '1')
			res = i;
	return res;
}

void solve(int t)
{
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
		gets(arr[i]);

	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = i; j < n; j++)
			if (len(j) <= i)
			{
				for (int k = j-1; k >= i; k--)
				{
					swap(k+1, k);
					cnt++;
				}
				break;
			}
	}
	printf("Case #%d: %d\n", t, cnt);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		solve(i+1);
	}
}