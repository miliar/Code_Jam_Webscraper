#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <memory>
#include <string>
#include <set>
#include <map>
#include <queue>
using namespace std;
double wp[150], owp[150], oowp[150];
int n;
char a[150][150];
double solve1(int k)
{
	int kl = 0, len = 0;
	for (int i = 0 ; i < n; i++)
	{
		if (a[k][i] == '1')
			kl++;
		if (a[k][i] != '.')
			len++;
	}
	return 1.0 * kl / len;
}
double solve2(int k)
{
	int kl = 0 , len = 0, p = 0;
	double ans = 0;
	for (int i = 0 ;  i< n; i++)
	{
		if (a[k][i] != '.')
		{

			kl = len = 0;
			for (int j = 0 ; j < n; j++)
				if (j != k)
				{
					if (a[i][j] == '1')
						kl++;
					if (a[i][j] != '.')
						len ++;
				}
			ans += 1.0 * kl / len;
			p++;
		}
	}
	return ans / p;
}
double solve3(int k)
{
	int kl= 0 , len = 0, p =0 ;
	double ans = 0;
	for (int i = 0 ; i < n; i++)
		if (a[k][i] != '.')
		{
			ans += owp[i];
			p++;
		}
		return ans / p;

}
int main(void)
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	char c;
	scanf("%d",&t);
	int q;
	for (q = 1; q<=t;q++)
	{
		scanf("%d",&n);
		scanf("%c",&c);
		for (int i = 0 ; i < n; i++)
		{
			for (int j = 0 ; j < n; j++)
				scanf("%c",&a[i][j]);
			scanf("%c",&c);
		}
		for (int i = 0 ; i < n; i++)
		{
			wp[i] = solve1(i);
		}
		for (int i = 0 ; i < n; i++)
			owp[i] = solve2(i);
		for (int i = 0 ; i < n; i++)
			oowp[i] = solve3(i);
		printf("Case #%d:\n",q);
		for (int i = 0 ; i < n; i++)
		{
			
			double ans = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.6lf\n",ans);
		}
	}
	return 0;
}


