#include<stdio.h>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>

using namespace std;

const int inf = 2147483647;
const double pi = acos(-1.0);
const double eps = 1e-7;

double dp[50];
int n,c;
double C[50][50];

void init()
{
	C[0][0] = 1;
	for(int i=1;i<50;i++)
	{
		C[0][i] = 1;
		for(int j=1;j<=i;j++)
			C[j][i] = C[j-1][i-1] + C[j][i-1];
	}
}

int main()
{
	init();
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d%d",&n,&c);
		dp[n] = 0;
		for(int i=n-1;i>=0;i--)
		{
			double p = C[c][i] / C[c][n];
			double sum = 0;
			for(int j=1;i+j<=n && j<=c;j++)
			{
				double k = C[j][n-i] * C[c-j][i] / C[c][n];
				sum += k * dp[i+j];
			}
			sum = (sum + 1) / (1 - p);
			dp[i] = sum;
		}
		printf("Case #%d: %.7lf\n",test,dp[0]);
	}
	return 0;
}

