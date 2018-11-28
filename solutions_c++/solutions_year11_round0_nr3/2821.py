#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>
#include <queue>
#include <stack>
#include <list>
#include <deque>
#include <set>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <utility>
#include <cassert>
#include <time.h>
using namespace std;

#define  max(a,b)  ((a)>(b)?(a):(b))
#define  min(a,b)  ((a)<(b)?(a):(b))
#define out(x) (cout << #x << " = " << x <<endl)
const int inf = 0x3f3f3f3f;
const double eps = 1e-10;
#define N 100005

int a[1002];

int main()
{
	int T;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	cin >> T;
	int cases = 1;
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small-attempt0.out","w",stdout);
	while(T--)
	{
		int i,n,tt = 0,ans = 0;
		int tmp;
	    cin >> n;
	
	
		for(i = 0; i < n; i++)
		{
		   cin >> a[i];
		   tt ^= a[i];
		}
		sort(a,a+n);
		for(i = 1; i < n; i++)
			ans += a[i];
		printf("Case #%d: ",cases++);
		if(!tt)
			printf("%d\n",ans);
		else 
			puts("NO");
	}
	return 0;
}
