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
#define nextline { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std;

#define PII pair<int,int>
#define mp make_pair
#define pb push_back
typedef long long LL;
typedef long double ldb;

const int inf = (1 << 30) - 1;
const ldb eps = 1e-9;

int n;
int a[1005];
void Load()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void Solve()
{
	sort(a + 0, a + n);
	int xall = 0, sall = 0;
	for (int i = 0; i < n; i++)
	{
		xall ^= a[i];
		sall += a[i];
	}
	if (xall != 0) printf("NO");
	else printf("%d", sall - a[0]);
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for (int tt = 1; tt <= nt; tt++)
	{ 
		Load();
		printf("Case #%d: ", tt);
		Solve();
		printf("\n");
	}	
	return 0;
}
