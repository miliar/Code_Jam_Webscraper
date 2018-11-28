#include <stdio.h>
int t;
__int64 data[1100];
__int64 sum[1100];
__int64 ssum[1100][2];

__int64 cac(__int64 st , int len , int t)
{
	__int64 ssd ;
	if(st > 0)
		ssd = sum[st - 1]; 
	else ssd = 0;
	if(st + t > len)
	{
		return sum[len - 1] + sum[st + t - len - 1] - ssd;
	}
	else 
	{
		return sum[st + t - 1] - ssd;
	}
}

__int64 find(__int64 c , __int64 st , int len , __int64 & ans)
{
	
	if(ssum[st][0]!=-1)
	{
		ans += ssum[st][0];
		return ssum[st][1];
	} 

	int beg = 0 ;
	int end = len - 1;
	int mid;

	__int64 ss = 0;
	while(beg <= end)
	{
		mid = (beg+end)>>1;

		ss = cac(st , len , mid + 1);
		if(ss == c)
		{
			ans += ss;
			ssum[st][0] = ss;
			ssum[st][1] = (mid + st + 1) % len;
			return ssum[st][1];
		}
		if(ss < c)
		{
			beg = mid + 1;
		} else 
		{
			end = mid - 1;
		}
	}
	if(ss < c)
	{
		ans += ss;
		ssum[st][0] = ss;
		ssum[st][1] = (mid + st + 1) % len;
		return ssum[st][1];
		
	} else if(mid > 0)
	{
		ssum[st][0] = cac(st , len , mid);
		ssum[st][1] = (mid + st ) % len;

		ans += ssum[st][0];
		return ssum[st][1];
	}
	return st;
}


int main()
{
	freopen("c:\\gcj2\\C-large.in","r",stdin);
	freopen("c:\\gcj2\\large.out","w",stdout);
	int r,k,n;
	int i,j;

	scanf("%d",&t);

	int cc = 1;
	while(t--)
	{
		 sum[0] = 0;
		 scanf("%d%d%d",&r,&k,&n);
		 for( i = 0 ; i < n ; i++)
		 {
			 scanf("%d",&data[i]);
			 if(i == 0)sum[i] = data[i];
			 else sum[i] = sum[i-1] + data[i];
			 ssum[i][0] = -1;
		 }
		 ssum[n][0] = -1;
		 __int64 st = 0;
		 __int64 ans = 0;
		 for( i = 0 ; i < r ; i++)
		 {
			 st = find( k , st , n , ans);
		 }
		 printf("Case #%d: %I64d\n",cc , ans);
		 cc++;
	}
	return 0;
}