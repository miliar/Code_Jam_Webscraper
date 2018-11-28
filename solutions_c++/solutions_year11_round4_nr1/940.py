#include <stdio.h>
#include <string.h>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

struct walkway
{
	int st,ed,sp;
}w[3300];
bool cmp1(walkway a,walkway b)
{
	return a.st < b.st;
}
bool cmp2(walkway a,walkway b)
{
	return a.sp < b.sp;
}

int cs,cn=1;
int X,S,R,t,N;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
		for(i=0;i<N;i++)
		{
			scanf("%d%d%d",&w[i].st,&w[i].ed,&w[i].sp);
		}
		sort(w,w+N,cmp1);
		int N2 = N;
		int cur = 0;
		for(i=0;i<N;i++)
		{
			int len = w[i].st - cur;
			if(len > 0)
			{
				w[N2].st = cur;
				w[N2].ed = w[i].st;
				w[N2].sp = 0;
				N2++;
			}
			cur = w[i].ed;
		}
		if(cur < X)
		{
			w[N2].st = cur;
			w[N2].ed = X;
			w[N2].sp = 0;
			N2++;
		}
		N = N2;
		sort(w,w+N,cmp2);
		double ans = 0;
		double left = t;
		for(i=0;i<N;i++)
		{
			int len = w[i].ed - w[i].st;
			if(left > 1e-6)
			{
				double tt = min(left,1.0*len/(w[i].sp+R));
				double ll = len - tt*(w[i].sp+R);
				left -= tt;
				ans += tt;
				ans += ll/(w[i].sp+S);
			}
			else
			{
				ans += 1.0*len/(w[i].sp+S);
			}
		}
		printf("Case #%d: %.8lf\n",cn++,ans);
	}
	return 0;
}


