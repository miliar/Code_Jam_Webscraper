#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

bool ok;
int n;
bool used[20];
int a[20], ans;

void check()
{
	int Patrick = 0, Sean = 0, cnt = 0;
	for (int i = 1; i <= n; i++)
	{
	 	if (used[i]) 
	 	{
	 		Patrick ^= a[i];
	 	}
	 	else 
	 	{
	 		Sean ^= a[i];
	 		cnt += a[i];
	 	}
	}
	if (Patrick != 0 && Patrick == Sean) 
	{
	 	ok = true;
	 	ans = max(ans, cnt);
	}
}

void rec(int k)
{
	if (k == n + 1) 
	{
	    check(); 
		return ;
	}
	used[k] = true;
	rec(k + 1);
	used[k] = false;
	rec(k + 1);
}

void solve(int id)
{
	ok = false;
	ans = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
		scanf("%d", &a[i]);
	rec(1);
	printf("Case #%d: ", id);
	if (!ok) 
	    printf("NO\n");
	else 
		printf("%d\n", ans);
}

int main() 
{
 	freopen("A.in", "r", stdin);
 	freopen("A.out", "w", stdout);

	int test; scanf("%d\n", &test);
	for (int i = 1; i <= test; i++)
		solve(i);

 	return 0;
}
