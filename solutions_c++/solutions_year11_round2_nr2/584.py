#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cs,cn=1,n;
int c,d;
int pos[1000100];

bool check(double time)
{
	double lt = pos[0] - time;
	for(int i=1;i<n;i++)
	{
		double cur = lt + d;
		if(cur > pos[i])
		{
			if(pos[i] + time < cur) return false;
			lt = cur;
		}
		else
		{
			double t = time < pos[i]-cur ? time : pos[i]-cur;
			lt = pos[i] - t;
		}
	}
	return true;
}


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j;
	int p,num;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d",&c,&d);
		n = 0;
		for(i=0;i<c;i++)
		{
			scanf("%d%d",&p,&num);
			while(num--)
			{
				pos[n++] = p;
			}
		}
		sort(pos,pos+n);
		double low = 0,high = 987654321,mid;
		while(high-low > 1e-7)
		{
			mid = (high+low)/2;
			if(check(mid)) high = mid;
			else low = mid;
		}
		printf("Case #%d: %.8lf\n",cn++,high);
	}
	return 0;
}
