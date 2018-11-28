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

#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(int i=(a);i<(int)(b);i++)
#define   per(i,a,b)  for(int i=((a)-1);i>=(int)(b);i--)
#define   PER(i,n)     per(i,n,0)
#define   REP(i,n)     rep(i,0,n)
#define   FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define   clr(a)      memset((a),0,sizeof (a))
#define   SZ(a)         ((int)((a).size()))
#define   ALL(x)      x.begin(),x.end()
#define   mabs(a)     ((a)>0?(a):(-(a)))
#define   inf         1000000001
#define  MAXN     
#define  eps      1e-6

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
		int res = 0;
		int n;
		char c;
		int a[105][2];
		scanf("%d",&n);

		REP(i,n)
		{
			getchar();
			scanf("%c %d",&c,&a[i][1]);
			if (c == 'O')
			{
				a[i][0] = 0;
			}
			else
			{
				a[i][0] = 1;
			}
		}
		a[n][0] = 0;
		a[n][1] = 1;
		a[n + 1][0] = 1;
		a[n + 1][1] = 1;

		int p = 0;
		int j = 0;
		int x = 1;
		int y = 1;
		for (p = 0;a[p][0] != 0 && p < n;p++);
		for (j = 0;a[j][0] != 1 && j < n;j++);

		while (p < n || j < n)
		{
			if (p < j)
			{
				int k = mabs(a[p][1] - x) + 1;
				res += k;
				if (y >= a[j][1] - k && y <= a[j][1] + k)
				{
					y = a[j][1];
				}
				else if (y < a[j][1] - k)
				{
					y += k;
				}
				else
				{
					y -= k;
				}
				x = a[p][1];
				for (p++;a[p][0] != 0 && p < n;p++);
				
			}
			else
			{
				int k = mabs(a[j][1] - y) + 1;
				res += k;
				if (x >= a[p][1] - k && x <= a[p][1] + k)
				{
					x = a[p][1];
				}
				else if (x < a[p][1] - k)
				{
					x += k;
				}
				else
				{
					x -= k;
				}
				y = a[j][1];
				for (j++;a[j][0] != 1 && j < n;j++);
			}
		}

		printf("Case #%d: %d\n",K + 1,res);
	}

	fclose(stdin);
	fclose(stdout);
}

