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

const int nmax = 1005, vmax = 11005;
int a[nmax];
int se[6], ss[6];
int n;
int best;

void rec(int i, int ns)
{
	if(i==n)
	{
		int ms = 15;
		for(int j=0;j<ns;j++)
			ms = min(ms, ss[j]);
		best = max(best, ms);
		return;
	}
	for(int j=0;j<ns;j++)
		if(a[i]  == se[j])
		{
			se[j]++;
			ss[j]++;
			rec(i+1, ns);
			se[j]--;
			ss[j]--;
		}
	if(ns < 5)
	{
		se[ns] = a[i] + 1;
		ss[ns] = 1;
		rec(i+1, ns+1);
	}
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		scanf("%d", &n);
		for(int i=0;i<n;i++)
		{
			scanf("%d", a+i);
		}
		sort(a, a+n);
		//printf("%d: ", n); for(int i=0;i<n;i++) printf("%d ", a[i]); printf("\n");

		best = 0;
		//se[0] = a[0] + 1;
		//ss[0] = 1;
		//rec(1, 1);
		if(n>0)
		{
			best = 1;
			rec(0, 0);
		}

		printf("Case #%d: %d\n",test_case, best);
    }
    return 0;
}
