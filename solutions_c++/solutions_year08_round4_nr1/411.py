#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define INF 133742
#define MAX 32768
#define AND 1
#define OR  0

using namespace std;
FILE *in; FILE *out;

struct Node
{
	int value;
	int changeable, operation;
};

int n, v;
Node a[MAX];
int dyn[MAX][2];

int recurse(int cur, int val)
{
	int i, c;
	int tmp, ans = INF;
	
	if (val == a[cur].value) return 0;
	if (-1  != a[cur].value) return INF;
	if (dyn[cur][val] != -1) return dyn[cur][val];
	
	if (val == 1)
	{
		if (a[cur].operation == AND)
		{
			tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 1);
			ans = min(ans, tmp);
			
			if (a[cur].changeable)
			{
				tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 0) + 1;
				ans = min(ans, tmp);
				
				tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 1) + 1;
				ans = min(ans, tmp);
			}
		}
		else
		{
			tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 0);
			ans = min(ans, tmp);
			tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 1);
			ans = min(ans, tmp);
			tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 1);
			ans = min(ans, tmp);
			
			if (a[cur].changeable)
			{
				tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 1) + 1;
				ans = min(ans, tmp);
			}
		}
	}
	else
	{
		if (a[cur].operation == AND)
		{
			tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 1);
			ans = min(ans, tmp);
			tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 0);
			ans = min(ans, tmp);
			tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 0);
			ans = min(ans, tmp);
		}
		else
		{
			tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 0);
			ans = min(ans, tmp);
			
			if (a[cur].changeable)
			{
				tmp = recurse(cur * 2, 1) + recurse(cur * 2 + 1, 0) + 1;
				ans = min(ans, tmp);
				tmp = recurse(cur * 2, 0) + recurse(cur * 2 + 1, 1) + 1;
				ans = min(ans, tmp);
			}
//			cout << "Here at node " << cur << " with desired value " << val << endl;
//			cout << " -- Best answer found: " << ans << endl;
		}
	}
	
	ans = min(ans, INF);	
	dyn[cur][val] = ans;
	return ans;
}


void doWork(int testNum)
{
	int i;
	int ans = 0;
	fscanf(in, "%d %d", &n, &v);
	
	for (i=1; i<=(n-1)/2; i++)
	{
		a[i].value = -1;
		fscanf(in, "%d %d", &a[i].operation, &a[i].changeable);
	}
	for ( ; i<=n; i++) fscanf(in, "%d", &a[i].value);
	
	memset(dyn, -1, sizeof(dyn));
	ans = recurse(1, v);

	if (ans >= INF) fprintf(out, "IMPOSSIBLE\n");
	else fprintf(out, "%d\n", ans);	
	return;
}

int main(void)
{
	int tests, i;
	
	in = fopen("booleanTree.in", "rt");
	out = fopen("booleanTree.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork(i + 1);
	}
	
	return 0;
}
