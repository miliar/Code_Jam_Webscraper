#include <stdio.h>
#include <string.h>

int P,Q,s[10010],v[110],minimum;
char used[10010],vis[10010];

void go(int day,int sum) {
	if(sum > minimum)	return;
	if(day >= Q) {
		minimum = sum;
		return;
	}
	int i,j,k;
	for(i=0;i<Q;i++)
		if(used[i] == 0) {
			used[i] = 1;
			vis[v[i]] = 1;
			for(j=v[i]-1;j>0 && vis[j] == 0;j--);
			j = v[i]-1-j;
			for(k=v[i]+1;k<=P && vis[k] == 0;k++);
			k = k-v[i]-1;
			go(day+1,sum+j+k);
			used[i] = 0;
			vis[v[i]] = 0;
		}
}

int main() {
	int t,i,j,c=0;
	
	scanf("%d",&t);
	while(t--) {
		scanf("%d%d",&P,&Q);
		for(i=0;i<Q;i++)
			scanf("%d",v+i);
		memset(used,0,sizeof(used));
		memset(vis,0,sizeof(vis));
		minimum = 999999999;
		go(0,0);
		printf("Case #%d: %d\n",++c,minimum);
	}
	
	return 0;
}
