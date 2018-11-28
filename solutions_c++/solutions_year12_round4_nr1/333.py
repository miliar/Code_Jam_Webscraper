#include<stdio.h>
#include<memory.h>
#include<algorithm>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int T;
int N,M;
struct LIST
{
	int x,d;
}list[10005];
int D[10005];
int main()
{
	fscanf(in,"%d",&T);
	int i,j,t,x;
	bool Ans;
	for(t=1;t<=T;t++)
	{
		Ans=0;
		fscanf(in,"%d",&N);
		for(i=1;i<=N;i++)	fscanf(in,"%d %d",&list[i].x,&list[i].d);
		fscanf(in,"%d",&M);
		memset(D,0,sizeof(D));
		D[1]=list[1].x;
		for(i=1;i<=N;i++)
		{
			if(list[i].x+D[i]>=M)
			{
				Ans=1;
				break;
			}
			for(j=i+1;j<=N;j++)
			{
				if(list[j].x-list[i].x>D[i]) break;
				x=list[j].x-list[i].x;
				if(x>list[j].d) x=list[j].d;
				if(D[j]<x) D[j]=x;
			}
		}
		fprintf(out,"Case #%d: ",t);
		if(Ans) fprintf(out,"YES\n");
		else fprintf(out,"NO\n");
	}
}