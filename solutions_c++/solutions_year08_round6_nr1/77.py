#include "stdio.h"
#include "stdlib.h"
char ch[100];
struct node{
	int w,h,b;
}list[1005];
int h[1005],w[1005],numh,numw,w1,w2,h1,h2;
int main()
{
	int kase,tot,n,m,w_max,w_min,h_max,h_min,i,k,j,l;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d",&n);
		w_max=-1;
		w_min=0x7fffffff;
		h_min=0X7fffffff;
		h_max=-1;
		l=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&list[i].w,&list[i].h);
			scanf("%s",ch);
			if(ch[0]=='B')
			{
				list[i].b=1;
				if(list[i].w>w_max)
					w_max=list[i].w;
				if(list[i].w<w_min)
					w_min=list[i].w;
				if(list[i].h<h_min)
					h_min=list[i].h;
				if(list[i].h>h_max)
					h_max=list[i].h;
				l=1;
			}
			else
			{
				scanf("%s",ch);
				list[i].b=0;
			}
		}
		w1=h1=0x7fffffff;
		w2=h2=-1;
		numh=numw=0;
		for(i=0;i<n;i++)
		{
			if(list[i].b==0)
			{
				if(list[i].w>=w_min&&list[i].w<=w_max)
					h[numh++]=list[i].h;
				else if(list[i].h>=h_min&&list[i].h<=h_max)
					w[numw++]=list[i].w;
			}
		}
		if(l==1)
		{
			for(i=0;i<numh;i++)
			{
				if(h[i]<h_min&&h[i]>h2)
					h2=h[i];
				if(h[i]>h_max&&h[i]<h1)
					h1=h[i];
			}
			for(i=0;i<numw;i++)
			{
				if(w[i]<w_min&&w[i]>w2)
					w2=w[i];
				if(w[i]>w_max&&w[i]<w1)
					w1=w[i];
			}	
		}
		printf("Case #%d:\n",kase);
		scanf("%d",&m);
		while(m--)
		{
			scanf("%d%d",&k,&j);
			if(k>=w_min&&k<=w_max&&j>=h_min&&j<=h_max)
				printf("BIRD\n");
			else if(l==1&&(k<=w2||j<=h2||k>=w1||j>=h1))
				printf("NOT BIRD\n");
			else if(l==0)
			{
				for(i=0;i<n;i++)
					if(list[i].w==k&&list[i].h==j)
						break;
				if(i!=n)
					printf("NOT BIRD\n");
				else
					printf("UNKNOWN\n");
			}
			else
				printf("UNKNOWN\n");
		}
	}
	return 0;
}
