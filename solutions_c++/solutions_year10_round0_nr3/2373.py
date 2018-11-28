#include<stdio.h>
#include<stdlib.h>
#include<memory.h>

int queue[1005];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T,i,j,k,l,m,n,N,head,tail,tmp,cas,R;
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&R,&k,&N);
		for (i=0;i<N;i++)
			scanf("%d",&queue[i]);
		head=0;tail=N-1;
		int money=0;
		while (R--)
		{
			l=k;j=0;
			while (l>=queue[head] && j<N)
			{
				tmp=queue[head];
				l-=tmp;
				j++;
				money+=tmp;
				head=(head+1)%N;
				tail=(tail+1)%N;
				queue[tail]=tmp;
			}
		}
		printf("Case #%d: %d\n",cas,money);
	}
}
