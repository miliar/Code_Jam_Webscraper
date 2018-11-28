#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000

#define GI(x) scanf("%d", &x)

using namespace std;
int n;
struct abc
{
	int x, y, r;
};
abc d[10];
double getans(int a, int b)
{
	double dist = (double)(d[a].x-d[b].x)*(double)(d[a].x-d[b].x) + (double)(d[a].y-d[b].y)*(double)(d[a].y-d[b].y);
	dist = sqrt(dist) + d[a].r + d[b].r;
	return dist;
}
double solve()
{
	if(n == 1)
		return d[0].r;
	if(n == 2)
		return max(d[0].r, d[1].r);
	
	int i, j, k;
	double ans = 0;
	ans = max((double)d[2].r, getans(0,1)/2.0);
	ans = min(ans, max((double)d[0].r, getans(1,2)/2.0));
	ans = min(ans, max((double)d[1].r, getans(0,2)/2.0));
	return ans;
}
int main()
{
	int tes;
	cin >> tes;
	for(int t = 1; t <= tes; t++)
	{
		int i, j, k;
		cin >> n;
		for(i = 0; i < n; i++)
		{
			cin >> d[i].x >> d[i].y >> d[i].r;
		}
		double ans = solve();
		printf("Case #%d: %lf\n", t, ans);
	}
	
	
	return 0;
}
