#include<stdio.h>
int main()
{
//	FILE *fin =fopen("A-large.in", "r");
//	FILE *fout=fopen("A-large.out", "w");
	int i,t,n,ol,bl,oi,bi,cnt=0,step;
	int now[2];
	char ch;
	int a[105][2],o[105],b[105];
//	fscanf(fin,"%d",&t);
	scanf("%d",&t);
	while(t--)
	{
		cnt++;
		ol=bl=0;
//		fscanf(fin,"%d",&n);
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
	//		fscanf(fin,"%c",&ch);
	//		fscanf(fin,"%c",&ch);
	//		fscanf(fin,"%d",&a[i][0]);	
			scanf("%c",&ch);
			scanf("%c",&ch);
			scanf("%d",&a[i][0]);	
			if(ch=='O')
			{
				o[ol++]=a[i][0];
				a[i][1]=0;
			}
			else if(ch=='B')
			{
				b[bl++]=a[i][0];
				a[i][1]=1;
			}
		}
		step=0;
		oi=bi=0;
		now[0]=now[1]=1;
		for(i=0;i<n;++i)
		{
			while(now[a[i][1]]!=a[i][0])
			{
				step++;
				if(oi<ol)
				{
					if(o[oi]<now[0])
						now[0]--;
					if(o[oi]>now[0])
						now[0]++;
				}
				if(bi<bl)
				{
					if(b[bi]<now[1])
						now[1]--;
					if(b[bi]>now[1])
						now[1]++;
				}
			}
			step++;
			if(a[i][1]==0)
			{
				oi++;
				if(bi<bl)
				{
					if(b[bi]<now[1])
						now[1]--;
					if(b[bi]>now[1])
						now[1]++;
				}
			}
			if(a[i][1]==1)
			{
				bi++;
				if(oi<ol)
				{
					if(o[oi]<now[0])
						now[0]--;
					if(o[oi]>now[0])
						now[0]++;
				}
			}
		}
	//	fprintf(fout,"Case #%d: %d\n",cnt,step);
		printf("Case #%d: %d\n",cnt,step);
	}
}