#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;

bool v[1200];
int n, s[1200];
double ans[20];

double calc(int k)
{
	if (ans[k] >= 0)return ans[k];
	
	int s[10];
	for (int i = 0; i < k; i++)
	{
		s[i] = i;
	}
	double tmp = 0.0;
	int total = 0;
	int self = 0;
	do
	{
		for (int i = 0; i < k; i++)
		{
			int cnt = 0;
			while (!v[i])
			{
				v[i] = 1;
				++cnt;
				i = v[i];
			}
			if (cnt == k)
				self++;
			else
				tmp += calc(cnt);
		}
		total++;
	} while (next_permutation(s, s + k));
	ans[k] = tmp / (self * total);
	return ans[k];
}

double solve()
{
	memset(v, 0, sizeof (v));
	
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &s[i]);
	}
	double ans = 0.0;
	for (int i = 0; i < n; i++)
	{
		int cnt = 0;
		while (!v[i])
		{
			v[i] = 1;
			++cnt;
			i = v[i];
		}
		ans += cnt;
	}
	return ans;
}

int main()
{
//	for (int i = 0; i < 20; i++)ans[i] = -1;
//	ans[0] = ans[1] = 0;
//	init(5);
	
	
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: %.10f\n", i, solve());
	}
	return 0;
}
