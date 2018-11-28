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

int a[10005];
int n;
bool ok(int x)
{
	for(int i = 0; i < n;i++)
	{
		if(a[i]%x == 0  || x%a[i] == 0) continue;
		else return 0;
	}
	return 1;
}
int main()
{
	int T;
	freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
	cin >>T;
	int l,r,cases=1;
	while(T--)
	{
		cin >> n >> l >> r;
		int i,j,k;
		for(i = 0; i < n; i++)
			scanf("%d",&a[i]);
		int ans;
		printf("Case #%d: ",cases++);
		for(ans = l; ans <= r; ans++)
		{
		   if(ok(ans))
		   {
                printf("%d\n",ans);
				goto end;
		   }
		}
		puts("NO");
end:;

	}
return 0;

}