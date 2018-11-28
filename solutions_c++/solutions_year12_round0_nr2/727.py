#include<stdio.h>
#include<algorithm>
#include<memory.h>
FILE*in=fopen("input.txt","r");
FILE*out=fopen("output.txt","w");
int N;
int T,S,P;
struct LIST
{
	int s;
	int x,y,z;
	bool operator()(LIST a,LIST b)
	{
		if(a.x+a.y+a.z!=b.x+b.y+b.z) return (a.x+a.y+a.z)<(b.x+b.y+b.z);
		return 0;
	}
}list[110];
int M;
int Index[100];
int D[101][101];
int main()
{
	fscanf(in,"%d",&T);
	int i,j,k;
	for(i=0;i<=10;i++)
	{
		for(j=i;j<=10&&j<=i+2;j++)
		{
			for(k=j;k<=10&&k<=j+2;k++)
			{
				if(i+2<k) break;
				list[++M].x=i; list[M].y=j; list[M].z=k;
				if(k==i+2) list[M].s=1;
			}
		}
	}
	std::sort(list+1,list+1+M,LIST());
	for(i=M;i>=1;i--) Index[list[i].x+list[i].y+list[i].z]=i;
	int t,K;
 	for(t=1;t<=T;t++)
	{
		fprintf(out,"Case #%d: ",t);
		memset(D,0,sizeof(D));
		fscanf(in,"%d %d %d",&N,&S,&P);
		for(i=1;i<=N;i++)
		{
			fscanf(in,"%d",&K);
			for(k=Index[K];k<=M;k++)
			{
				if((list[k].x+list[k].y+list[k].z)!=K) break;
				for(j=0;j<i;j++)
				{
					if(D[i-1][j]+(list[k].z>=P)>D[i][j+list[k].s]) D[i][j+list[k].s]=D[i-1][j]+(list[k].z>=P);
				}
			}
		}
		fprintf(out,"%d\n",D[N][S]);
	}
}