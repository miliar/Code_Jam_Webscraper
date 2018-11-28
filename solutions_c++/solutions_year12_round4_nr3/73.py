#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 2005;
const int hmax = 1e9;
int a[nmax];
int y[nmax];
int n;

bool check(int i, int j)
{
	//printf("%d %d\n", i, j);
	if(i == j)
		return true;
	for(int k=i;k<j;k=a[k])
	{
		//printf("  %d %d\n", k, a[k]);
		if(a[k] > j)
			return false;
		if(!check(k+1, a[k]))
			return false;
	}
	return true;
}

void assign(int i, int j, int h, int m)
{
	if(i == j)
		return;
	for(int k=i;k<j;k=a[k])
		y[k] = h - m * (j - k);
	for(int k=i;k<j;k=a[k])
		assign(k+1, a[k], y[a[k]], m+1);
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		scanf("%d", &n);
		for(int i=1;i<n;i++)
			scanf("%d", a+i);
		printf("Case #%d:",test_case);
		if(!check(1, n))
		{
			printf(" Impossible\n");
			continue;
		}
		int h = hmax;
		y[n] = h;
		assign(1, n, h, 0);
		for(int i=1;i<=n;i++)
			printf(" %d", y[i]);
		printf("\n");
	}
	return 0;
}
