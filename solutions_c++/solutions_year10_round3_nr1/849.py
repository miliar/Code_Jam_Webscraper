#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

int t,n;
int x[1000],y[1000];

int solve()
{
	int i,j;
	int ans = 0;
	for (i=0;i<n;i++)
		for (j=i+1;j<n;j++)
			if ((x[i]-x[j])*(y[i]-y[j])<0)
				ans++;
	return ans;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for (j=0;j<n;j++)
			scanf("%d%d",&x[j],&y[j]);
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}