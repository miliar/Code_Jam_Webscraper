#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int,int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
using namespace std;
int a[1010];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(it,0,test)
	{
		int n;
		scanf("%d",&n);
		int p=0;
		int sum=0;
		FOR(i,0,n)
		{
			scanf("%d",&a[i]);
			p^=a[i];
			sum+=a[i];
		}
		printf("Case #%d: ",it+1);
		if (p!=0)
			printf("NO\n");
		else
		{
			int min1=2000000000;
			FOR(i,0,n)
				min1=MIN(min1,a[i]);
			sum-=min1;
			printf("%d\n",sum);
		}
	}
    return 0;
}