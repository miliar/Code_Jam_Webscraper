#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define sqr(a)		((a)*(a))
#define rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define PER(i,n)	per(i,n,0)
#define REP(i,n)	rep(i,0,n)
#define clr(a)		memset((a),0,sizeof (a))
#define SZ(a)		((int)((a).size()))
#define ALL(x)		x.begin(),x.end()
#define mabs(a)		((a)>0?(a):(-(a)))
#define inf			1000000001 
#define eps			1e-6

void swap(int* a,int* b)
{
	if (a != b)
	{
		*a ^= *b;
		*b ^= *a;
		*a ^= *b;
	}
}

int main()
{
	freopen("data1.in","r",stdin);
	freopen("data2.in","w",stdout);

	int T;
	scanf("%d",&T);

	REP(K,T)
	{
		int n;
		int a[1005];
		int res = 0;
		int mini = 0;
		int sum = 0;
		scanf("%d",&n);

		REP(i,n)
		{
			scanf("%d",&a[i]);
			res ^= a[i];
			sum += a[i];
			if (a[i] < a[mini])
			{
				mini = i;
			}
		}
		if (res != 0)
		{
			printf("Case #%d: NO\n",K + 1);
		}
		else
		{
			printf("Case #%d: %d\n",K + 1,sum - a[mini]);
		}
	}

	fclose(stdin);
	fclose(stdout);
}

