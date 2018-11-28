#include <iostream>

using namespace std;

const int MAX = 45;
char mat[MAX][MAX];
int arr[MAX];
int row[MAX];
bool visit[MAX];
int n;

int Slove1()
{
	int i, j, ans;
	memset(arr, 0, sizeof(arr));
	memset(visit, 0, sizeof(visit));
	for (i = 0; i < n; i++)
			row[i] = i;

	for (i = 0; i < n; i++)
	{
		for (j = n-1; j >= 0; j--)
		{
			if(mat[i][j] == '1')
			{
				arr[i] = j;
				break;
			}
		}
	}
	for (i = 0; i < n; i++)
	{
		j = 0;
		while(visit[j%n] || arr[i] > j)
		{
			j++;
		}
		visit[j%n] = 1;
		row[j%n] = i;
	}
	ans = 0;
	for (i = 0; i < n; i++)
	{
		for (j = i+1; j < n; j++)
		{
			if(row[i] > row[j])
				ans++;
		}
	}
	return ans;
}

int Slove2()
{
	int i, j, ans;
	memset(arr, 0, sizeof(arr));
	memset(visit, 0, sizeof(visit));
	for (i = 0; i < n; i++)
			row[i] = i;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if(mat[i][j] == '1')
			{
				arr[i] = j;
				break;
			}
		}
	}
	for (i = 0; i < n; i++)
	{
		j = 0;
		while(visit[j%n] || arr[i] < j)
		{
			j++;
		}
		visit[j%n] = 1;
		row[j%n] = i;
	}
	ans = 0;
	for (i = 0; i < n; i++)
	{
		for (j = i+1; j < n; j++)
		{
			if(row[i] > row[j])
				ans++;
		}
	}
	return ans;
}

int main()
{
	int i, j, k, t, temp, ans,ans1, temq, cas;
	freopen("aain.txt","r",stdin);
	freopen("aaout.txt","w",stdout);
	scanf("%d",&t);
	cas= 0;
	while(t--)
	{
		scanf("%d",&n);
		for (i = 0; i < n; i++)
			scanf("%s",mat[i]);
// 		int flag;
// 		for (i = 0; i < n; i++)
// 		{
// 			if(flag > 0)
// 				break;
// 			for (j = 0; j < n; j++)
// 			{
// 				if(mat[i][j] == '1')
// 				{
// 					if(j < i)
// 						flag = 1;
// 					else if(flag > i)
// 						flag = 2;
// 					break;
// 				}
// 					
// 			}
// 		}
// 		if(flag == 1)
			ans = Slove1();
// 		else if(flag == 2)
// 			ans = Slove2();
// 		else 
// 		{
// 			ans = Slove1();
// 			j = Slove2();
// 			if(ans > j)
// 				ans = j;
// 		}

		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
