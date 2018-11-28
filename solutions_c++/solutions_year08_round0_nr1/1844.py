#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <math.h>
#include <string.h>
#include <string>


using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

typedef long long LL;  

map<string, int> mp;

char str[1 << 20];

int readInt()
{
	gets(str);
	int r = 0;
	for (int i = 0; str[i]; i++)
		if (str[i] >= '0' && str[i] <= '9')
			r = r * 10 + str[i] - '0';
	return r;
}

const int inf = 100000000;
int s, q;
int a[1 << 10];
int d[1 << 10][1 << 7];

int Solve()
{
	mp.clear();
	s = readInt();
	for (int i = 0; i < s; i++)
	{
		gets(str);
		mp[string(str)] = i;
	}
	q = readInt();
	for (int i = 0; i < q; i++)
	{
		gets(str);
		a[i] = mp[string(str)];
	}
	for (int i = 0; i <= q; i++)
		for (int j = 0; j < s; j++)
			d[i][j] = inf;
	for (int i = 0; i < s; i++)
		d[0][i] = (a[0] == i) * inf;
	for (int i = 0; i < q - 1; i++)
	{
		int M1 = inf;
		for (int j = 0; j < s; j++)
			M1 = min(M1, d[i][j]);
		for (int j = 0; j < s; j++)
			if (j != a[i + 1])
				d[i + 1][j] = min(d[i + 1][j], M1 + 1);
		for (int j = 0; j < s; j++)
			if (j != a[i + 1])
				d[i + 1][j] = min(d[i + 1][j], d[i][j]);
	}
	int r = inf;
	for (int i = 0; i < s; i++)
		r = min(r, d[q - 1][i]);
	return r;
}

int main()
{ 	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = readInt();
	for (int i = 1; i <= t; i++)
	{
		int r = Solve();
		printf("Case #%d: %d\n", i, r);
	}
	return 0;
}
