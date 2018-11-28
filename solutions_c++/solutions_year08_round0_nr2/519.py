#include "stdio.h"
#include <algorithm>
using namespace std;
struct node{
	int be,en,whi;
}list[205];
char ch[10];
int calc()
{
	int i;
	i=((ch[0]-48)*10+(ch[1]-48))*60+(ch[3]-48)*10+ch[4]-48;
	return i;
}
int cmp(node a,node b)
{
	return a.be<b.be;
}
int boo[205];
int main()
{
	int kase,tot,n,m,i,k,j,resa,resb,t,l;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d%d%d",&t,&n,&m);
		for(i=0;i<n;i++)
		{
			scanf("%s",ch);
			list[i].be=calc();
			scanf("%s",ch);
			list[i].en=calc();
			list[i].whi=1;
		}
		for(i=0;i<m;i++)
		{
			scanf("%s",ch);
			list[n+i].be=calc();
			scanf("%s",ch);
			list[n+i].en=calc();
			list[n+i].whi=-1;
		}
		for(i=0;i<m+n;i++)
			boo[i]=0;
		sort(list,list+n+m,cmp);
		resa=resb=0;
		for(i=0;i<n+m;i++)
		{
			if(boo[i]==1)
				continue;
			j=list[i].en+t;
			if(list[i].whi==1)
				resa++;
			else
				resb++;
			l=list[i].whi;
			for(k=i+1;k<n+m;k++)
				if(boo[k]==0&&list[k].whi==-l&&list[k].be>=j)
				{
					boo[k]=1;
					l=-l;
					j=list[k].en+t;
				}
		}
		printf("Case #%d: %d %d\n",kase,resa,resb);
	}
	return 0;
}