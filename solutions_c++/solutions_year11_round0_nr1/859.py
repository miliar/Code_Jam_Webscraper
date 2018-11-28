#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int order[105][2];
int ol,bl;
int ood[105];
int on;
int bod[105];
int bn;
int oh,bh;

FILE *fin,*fout;

int min(int a,int b)
{
	if(a<b)
		return a;
	return b;
}

int max(int a,int b)
{
	if(a>b)
		return a;
	return b;
}

int abs(int a)
{
	if(a<0)
		return -a;
	return a;
}

int main(void)
{
	int i,j,ans,n,T;
	fin=fopen("A.in","r");
	fout=fopen("A.out","w+");
	fscanf(fin,"%d",&T);
	for(j=1;j<=T;j++)
	{
		fscanf(fin,"%d",&n);
		on=0;bn=0;
		for(i=1;i<=n;i++)
		{
			fgetc(fin);
			order[i][0]=fgetc(fin);
			fgetc(fin);
			fscanf(fin,"%d",&order[i][1]);
			if(order[i][0]=='O')
				ood[++on]=order[i][1];
			else
				bod[++bn]=order[i][1];
		}
		ans=0;
		ol=1;bl=1;
		oh=1;bh=1;
		for(i=1;i<=n;i++)
		{
			ans++;
			if(order[i][0]=='O')
			{
				oh++;
				if(abs(order[i][1]-ol)!=0)
				{
					if(bh<=bn&&bl<bod[bh])
						bl=min(bl+abs(order[i][1]-ol),bod[bh]);
					else if(bh<=bn&&bl>bod[bh])
						bl=max(bl-abs(order[i][1]-ol),bod[bh]);
					ans+=abs(order[i][1]-ol);
					ol=order[i][1];
				}
				if(bh<=bn&&bl<bod[bh])
					bl=min(bl+1,bod[bh]);
				else if(bh<=bn&&bl>bod[bh])
					bl=max(bl-1,bod[bh]);
			}
			else
			{
				bh++;
				if(abs(order[i][1]-bl)!=0)
				{
					if(oh<=on&&ol<ood[oh])
						ol=min(ol+abs(order[i][1]-bl),ood[oh]);
					else if(oh<=on&&ol>ood[oh])
						ol=max(ol-abs(order[i][1]-bl),ood[oh]);
					ans+=abs(order[i][1]-bl);
					bl=order[i][1];
				}
				if(oh<=on&&ol<ood[oh])
					ol=min(ol+1,ood[oh]);
				else if(oh<=on&&ol>ood[oh])
					ol=max(ol-1,ood[oh]);
			}
		}
		fprintf(fout,"Case #%d: %d\n",j,ans);
	}
	return 0;
}
