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

const int nmax = 1005, rmax = 100005;
int r[nmax];
int idx[nmax];
pii sr[nmax];
bool u[nmax];
int cx[nmax], cy[nmax];
int n, X, Y;

void assign(int i, int x1, int y1, int x2, int y2)
{
	int x, y;
	for(; i < n; i++)
	{
		x = max(x1 + r[i], 0);
		y = max(y1 + r[i], 0);
		if(x + r[i] <= x2 && y + r[i] <= y2 && !u[i] && x <= X && y <= Y)
			break;
	}
	if(i >= n)
		return;
	cx[i] = x;
	cy[i] = y;
	u[i] = true;
	//fprintf(stderr, "%d %d %d\n", cy[i], r[i], Y);
	if(cy[i] + r[i] <= Y)
		assign(i+1, x1, cy[i] + r[i], cx[i] + r[i], y2);
	if(cx[i] + r[i] <= X)
		assign(i+1, cx[i] + r[i], y1, x2, y2);
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		//fprintf(stderr, "%d\n", test_case);
		memset(u, false, sizeof(u));
		
		scanf("%d%d%d", &n, &X, &Y);
		for(int i=0;i<n;i++)
		{
			int r;
			scanf("%d", &r);
			sr[i] = pii(r, i);
		}
		
		sort(sr, sr+n, greater<pii>());
		for(int i=0;i<n;i++)
		{
			r[i] = sr[i].first;
			idx[sr[i].second] = i;
		}
		
		assign(0, -rmax, -rmax, X+rmax, Y+rmax);
		
		for(int i=0;i<n;i++)
		{
			assert(u[i]);
			assert(cx[i] >= 0 && cx[i] <= X && cy[i] >= 0 && cy[i] <= Y);
		}
		printf("Case #%d:",test_case);
		for(int i=0;i<n;i++)
			printf(" %d %d", cx[idx[i]], cy[idx[i]]);
		printf("\n");
		
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				if(abs(cx[i] - cx[j]) < r[i] + r[j] && abs(cy[i] - cy[j]) < r[i] + r[j])
				{
					fprintf(stderr, "%d %d\n", i, j);
					assert(false);
				}
	}
	return 0;
}
