#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#pragma warning(disable : 4996)

#define MAXN	1000
#define TOL		1e-8
int N, min_idx;
int num[MAXN], dif[MAXN];

void init()
{
	scanf("%d", &N);
	int tmp;
	for (int i=0;i<N;++i)
	{
		scanf("%d", &num[i]);
		if (i==0)
		{
			tmp=num[i];
			min_idx=i;
		}
		else if (num[i]<tmp)
		{
			tmp=num[i];
			min_idx=i;
		}	
	}
}
/*
double gcd(double a, double b)
{
	if (fabs(a)<TOL)
		return b;
	while (fabs(b)>TOL)
	{
		if (a>b)
			a=a-b;
		else
			b=b-a;
	}
	return a;
}
*/
int gcd(int a, int b)
{
	if (a==0)
		return b;
	while (b!=0)
	{
		if (a>b)
			a=a-b;
		else
			b=b-a;
	}
	return a;
}

int solve()
{
	for (int i=0;i<N;++i)
	{
		dif[i]=num[i]-num[min_idx];
	}
	// gcd
	int g1=dif[0], g2;
	for (int i=1;i<N;++i)
	{
		g1=gcd(g1,dif[i]);
	}
	//
	g2=g1-(num[min_idx]-num[min_idx]/g1*g1);
	return g2%g1;
}

int main()
{
//	freopen("..\\B-sample.in","r",stdin);freopen("..\\B.out","w",stdout);
	freopen("..\\B-small-attempt0.in","r",stdin);freopen("..\\B-small.out","w",stdout);
//	freopen("..\\B-large-practice.in","r",stdin);freopen("..\\B-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		init();
		int ret=solve();
		printf("%d\n",ret);
		
		fflush(stdout);
	}
	return 0;
}

