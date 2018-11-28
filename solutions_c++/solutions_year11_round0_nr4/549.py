#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <vector>
#include <map>
#include <set>

#include <algorithm>
#include <cmath>

using namespace std;


const int maxN = 1300;
double f[maxN];
bool calc[maxN];
double p[maxN][maxN];


double F(int n)
{
	if(calc[n])
	{
		return f[n];
	}
	calc[n] = true;
	double res = 0;
	for(int k = 1; k < n; k++)
	{
		res += F(n - k) * p[n][k];
	}
	res++;
	res /= (1 - p[n][0]);
	return f[n] = res;
}


void init()
{
	calc[0] = true;	
	p[1][1] = 1;
	for(int n = 1; n <= 1000; n++)
	{
		int N = n + 1;
		for(int k = 0; k <= n; k++)
		{
			p[n + 1][k + 1] += p[n][k] / N;
			p[n + 1][k - 1] += p[n][k] * k / N;
			p[n + 1][k] += p[n][k] * (n - k) / N;
		}
	}
}


int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	init();
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		int n;
		scanf("%d", &n);
		int k = 0;
		for(int i = 0; i < n; i++)
		{
			int a;
			scanf("%d", &a);
			a--;
			if(i != a)
			{
				k++;
			}
		}
//		k = testNumber;
		double res = k;//F(k);
		//if(fabs(res - k) > 1e-7)
		//{
		//	throw 42;
		//}
		printf("Case #%d: %.10lf\n", testNumber, res);
	}
	return 0;
}