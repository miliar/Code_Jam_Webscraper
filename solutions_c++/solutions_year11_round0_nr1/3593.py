#include<cstdio>
#include<cstring>
using namespace std;

const char sign[2]={'O','B'};
int list[105][2],n,m,i0,i1,j,t,pos[2],target[2];
char tem;

//'O'=0,'B'=1;

void check(int k)
{
	if (target[k]>=n) return;
	if (pos[k]==list[target[k]][1])
	{
		if (target[k]!=i1) return;
		target[k]++;
		j=i1+1;
		while(list[target[k]][0]!=k && target[k]<n) target[k]++;
	}
	else if (pos[k]<list[target[k]][1]) pos[k]++;
	else pos[k]--;
}

int main()
{
	freopen("text.in","r",stdin);
	freopen("text.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			tem=0;
			while(tem!='O' && tem!='B') scanf("%c",&tem);
			if (tem=='O') list[i][0]=0;
			else list[i][0]=1;
			scanf("%d",&list[i][1]);
		}
		pos[0]=1;pos[1]=1;
		i0=0;
		while(list[i0][0]!=0 && i0<n) i0++;
		target[0]=i0;
		i0=0;
		while(list[i0][0]!=1 && i0<n) i0++;
		target[1]=i0;
		i0=0;
		i1=0;
		while(target[0]<n || target[1]<n)
		{
			i0++;
			j=i1;
			check(0);
			check(1);
			i1=j;
			//printf("%d %d\n",pos[0],pos[1]);
		}
		printf("Case #%d: %d\n",cas,i0);
	}
	return 0;
}