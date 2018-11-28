#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))

__int64 r,n,k;
__int64 st[3200];
__int64 money[3200];
__int64 gp[3200];
__int64 ans;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("c.txt","w",stdout);
	int i,j,k;
	int cn=1,cs;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(i=0;i<n;i++){
			scanf("%I64d",&gp[i]);
		}
		int cur = 0;
		for(i=0;i<2200;i++)
		{
			st[i] = cur;
			__int64 sum = 0,cnt = 0;
			for(j=cur;;j=(j+1)%n)
			{
				sum += gp[j];
				cnt++;
				if(sum>k || cnt>n) break;
			}
			sum -= gp[j];
			money[i] = sum;
			cur = j;
		}
		int start = -1,end = -1;
		__int64 gs = 0;
		for(i=0;i<2100;i++)
		{
			int ok = 0;
			for(j=i+1;j<2100;j++)
			{
				if(st[i]==st[j] && st[i+1]==st[j+1])
				{
					ok = 1;
					break;
				}
			}
			if(ok) break;
		}
		start = i;end = j-1;
		for(i=start;i<=end;i++) gs += money[i];


		ans = 0;
		for(i=0;i<start && i<r;i++)
		{
			ans += money[i];
		}
		r -= start;
		ans += r/(end-start+1)*gs;
		r %= (end-start+1);
		for(i=start;i<start+r;i++) ans += money[i];
		printf("Case #%d: %I64d\n",cn++,ans);
	}
	return 0;
}
