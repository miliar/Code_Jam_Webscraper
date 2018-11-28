#include <vector>
#include <algorithm>
using namespace std;

#include <stdio.h>

int p;
int k;
int l;
int ar[1024];

void Read()
{
	scanf("%d%d%d", &p, &k, &l);
	for (int i=0; i<l; i++)
		scanf("%d", &ar[i]);
}

double Solve()
{
	double ans = 0;

	std::sort(ar, ar+l);

	int row = 1;
	int cnt = 0;
	for (int i=l-1; i>=0; i--)
	{
		ans += row * ar[i];
		cnt++;
		if(cnt == k)
		{
			cnt = 0;
			row++;
		}
	}

	return ans;
}

int main()
{
	freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);

	int t;
	int n;

	scanf("%d", &n);
	for (t=1; t<=n; t++)
	{
		Read();		
		printf("Case #%d: %.0lf\n", t, Solve());
	}
	return 0;
}

