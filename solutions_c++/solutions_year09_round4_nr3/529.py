#include <iostream>
using namespace std;

struct node
{
	int a[30];
	int mode;
	int id;
}date[20];

int dp[131072];

int a[20] , k;

bool judge(node A , node B)
{
	bool flag;
	int i , j;
	if(A.a[0] == B.a[0])
		return true;
	else if(A.a[0] < B.a[0])
		flag = true;
	else
		flag = false;
	for(i = 1 ; i < k ; i ++)
	{
		if(A.a[i] == B.a[i])
			return true;
		if(flag == true && A.a[i] > B.a[i])
			return true;
		if(flag == false && A.a[i] < B.a[i])
			return true;
	}
	return false;
}

int n , m;

void dfs(int x , int y , int now , int st)
{
	int i , j;
	for(i = st ; i < n ; i ++)
	{
		if((a[i] & x) != 0 || (a[ date[i].id ] & y) == 0)
			continue;
		dfs(x , y & date[i].mode , now | a[i] , i + 1);
	}
	if(dp[x | now] == -1 || dp[x | now] > dp[x] + 1)
		dp[x | now] = dp[x] + 1;
}

int main()
{
	int i , j , t , cas , d;
	freopen("C-small-attempt8.in" , "r" , stdin);
	freopen("1.txt" , "w" , stdout);
	scanf("%d" , &t);
	a[0] = 1;
	d = 0;
	for(i = 1 ; i < 17 ; i ++)
	{
		a[i] = a[i - 1] * 2;
	}
	for(cas = 1 ; cas <= t ; cas ++)
	{
		scanf("%d %d" , &n , &k);
		for(i = 0 ; i < n ; i ++)
		{
			for(j = 0 ; j < k ; j ++)
			{
				scanf("%d" , &date[i].a[j]);
			}
			date[i].id = i;
			date[i].mode = 0;
		}
		for(i = 0 ; i < n ; i ++)
		{
			for(j = 0 ; j < n ; j ++)
			{
				if(judge(date[i] , date[j]) == false)
				{
					date[i].mode |= a[j];
				}
			}
		}
		memset(dp , -1 , sizeof(dp));
		dp[0] = 0;
		m = n;
		for(i = 0 ; i < n ; i ++)
		{
			if(date[i].mode == a[m] - 1 - a[ date[i].id ])
			{
				date[i] = date[n - 1];
				n --;
				i --;
			}
		}
		if(n == 0)
			dp[0] = 1;
		for(i = 0 ; i < a[m] ; i ++)
		{
			if(dp[i] == -1)
				continue;
			dfs(i , a[m] - 1 , 0 , 0);
		}
		printf("Case #%d: %d\n" , cas , dp[a[n] - 1]);
	}
	return 0;
}