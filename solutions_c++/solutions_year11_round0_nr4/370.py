#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>

using namespace std;

const int MAXN = 1024;

int a[MAXN];
bool o[MAXN];

int work(int nCase)
{
	int n, ans = 0;
	scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
		scanf("%d", &a[i]);

	memset(o, false, sizeof(o));
	for (int i = 1; i <= n; i ++)
		if (!o[i] && a[i] != i)
		{
			o[i] = true;
			int z = a[i], nt = 1;  
			while (z != i)
			{
				o[z] = true;
				z = a[z];  nt ++;
			}
			ans += nt;
		}

	printf("Case #%d: %d.000000\n", nCase, ans);
	return 0;
}


int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k ++)
		work(k);
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}