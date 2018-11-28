#include <stdio.h>
#include <string.h>
#include <stdlib.h>

__int64 ans[2010];
int n,r,k;

int find(int st){
	int l,h,m;
	__int64 sum;
	l = 0;
	h = n-1;
	while(l <= h){
		m = (l+h)>>1;
		sum = (ans[st+m]-ans[st-1]);
		if(sum == k) return m;
		else if(sum < k) l = m+1;
		else h = m-1;
	}
	return h;
}

int main()
{
	int t,i,j,d,st,re;
	__int64 v[1010],total;
	freopen("C-large.in","r",stdin);
	freopen("cb2.out","w",stdout);
	scanf("%d",&t);
	for(d = 0; d < t; d++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i = 0; i < n; i++){
			scanf("%I64d",&v[i]);
		}
		ans[0] = 0;
		for(i = 1; i <= n; i++){
			ans[i] = ans[i-1]+v[i-1];
		}
		for(j = n+1,i = 0; i < n; i++,j++){
			ans[j] = ans[j-1]+v[i];
		}
		st = 0;
		total = 0;
		for(i = 1; i <= r; i++){
			re = find(st+1);
			total += (ans[st+re+1]-ans[st]);
			st = (st+re+1)%n;
//			if(st == 0) break;
		}
/*		total *= (r/i);
		r %= i;
		for(i = 1; i < r; i++){
			re = find(st);
			total += getsums(st,(st+re)%n);
			st = (st+re+1)%n;
		}*/
		printf("Case #%d: %I64d\n",d+1,total);
	}
	return 0;
}