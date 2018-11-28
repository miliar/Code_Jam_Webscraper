#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

__int64 answer[2010];
int n,r,k;

int findsite(int start){
	int l,h,m;
	__int64 sum;
	l = 0;
	h = n-1;
	while(l <= h){
		m = (l+h)>>1;
		sum = (answer[start+m]-answer[start-1]);
		if(sum == k) return m;
		else if(sum < k) l = m+1;
		else h = m-1;
	}
	return h;
}

int main()
{
	int t,i,j,T,start,re,starts[1010],t2;
	__int64 v[1010],total,xhj[1010],t1;
	freopen("C-large.in","r",stdin);
	freopen("clar.out","w",stdout);
	scanf("%d",&T);
	for(t = 0; t < T; t++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(i = 0; i < n; i++){
			scanf("%I64d",&v[i]);
		}
		answer[0] = 0;
		for(i = 1; i <= n; i++){
			answer[i] = answer[i-1]+v[i-1];
		}
		for(j = n+1,i = 0; i < n; i++,j++){
			answer[j] = answer[j-1]+v[i];
		}
		start = 0;
		total = 0;
		memset(xhj,0,sizeof(xhj));
		for(i = 0; i < r; i++){
			if(xhj[start] == 1) break;
			xhj[start] = 1;
			starts[start] = i;
			re = findsite(start+1);
			total += (answer[start+re+1]-answer[start]);
			start = (start+re+1)%n;		
		}
		if(i < r){
			t1 = 0;
			t2 = start;
			start = 0;
			for(j = 0; j < starts[t2]; j++){
				re = findsite(start+1);
				t1 += (answer[start+re+1]-answer[start]);
				start = (start+re+1)%n;		
			}
			i -= starts[t2];
			total = (total-t1)*((r-starts[t2])/i);
			total += t1;
			r = (r-starts[t2]) % i;
			start = t2;
			for(j = 0; j < r; j++){
				re = findsite(start+1);
				total += (answer[start+re+1]-answer[start]);
				start = (start+re+1)%n;
			}
		}
		printf("Case #%d: %I64d\n",t+1,total);
	}
	return 0;
}