#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define pii pair<int,int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;
const ldb pi = fabs(atan2(0.0, -1.0));

LL n;
void Load()
{
	cin >> n;
}

const int maxn = 2000005;

vector <int> pr;
bool ipr[maxn];
void genPrimes()
{
	pr.resize(0);
	memset(ipr, true, sizeof(ipr));
	for (int i = 2; i < maxn; i++)
	{
		if (ipr[i])
		{
			for (int j = 2; i * j < maxn; j++)
				ipr[i * j] = false;
			pr.pb(i);	
		}
	}
}

void Solve()
{
	if (n == 1)
	{
		cout << 0;
		return;
	}
	int res = 1;
	for (int i = 0; i < (int)pr.size(); i++)
	{
		if (pr[i] > n) break;
		LL x = pr[i] * 1LL * pr[i];
		while (x <= n)
		{
			res++;
			x *= pr[i];
		}
	}
	cout << res;
}

int main()
{
//	freopen("c.in", "r" ,stdin);
//	freopen("c.out", "w", stdout);
	int nt;
	scanf("%d", &nt);
	genPrimes();
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
