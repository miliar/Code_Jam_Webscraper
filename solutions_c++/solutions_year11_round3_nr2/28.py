#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795

const int max_n=1000000;
const int max_l=2;
long long a[max_n+1];
long long ans[max_n+1][max_l+1];
const long long inf=(long long) (1e18);

int main()
{
	freopen("problem_2.in", "r", stdin);
	freopen("problem_2.out", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int it=1; it<=tc; ++it)
	{
		long long t, x;
		int n, l, c;
		cin >> l >> t >> n >> c;
		for(int i=0; i<c; ++i)
		{
			cin >> x;
			for(int k=0; k*c+i<n; ++k)
				a[k*c+i+1]=x;
		}
		ans[0][0]=0;
		for(int i=1; i<=n; ++i)
		{
			ans[i][0]=ans[i-1][0]+2*a[i];
			for(int j=1; j<=l; ++j)
			{
				long long slow_t=min(max(0ll, t-ans[i-1][j-1]), 2*a[i]);
				assert(slow_t%2==0);
				long long fast_t=a[i]-slow_t/2;
				ans[i][j]=min(ans[i-1][j]+2*a[i], ans[i-1][j-1]+slow_t+fast_t);
			}
		}
		long long answ=inf;
		for(int i=0; i<=l; ++i)
			answ=min(answ, ans[n][i]);
		cout << "Case #" << it << ": " << answ << endl;
	}
	return 0;
}