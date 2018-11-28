//written on C++ (compatible with DevC++ / MS Visual C++ 6)
#include<stdio.h>

int main()
{
	int alt[100][100],basinx[26],basiny[26],flow,floweast,flownorth,flowsouth,flowwest,h,i,j,k,l,nbasin,numbasin,t,w,x0,x1,xbasin[100][100],xflow[100][100],y0,y1,ybasin[100][100],yflow[100][100];
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d %d",&h,&w);
		for(j=0;j<h;j++)for(k=0;k<w;k++)scanf("%d",&alt[j][k]);
		for(j=0;j<h;j++)
		{
			for(k=0;k<w;k++)
			{
				xflow[j][k]=j;yflow[j][k]=k;
				flow=0;
				flownorth=0;
				if(j)
				{
					if(alt[j-1][k]<alt[j][k])flownorth=alt[j][k]-alt[j-1][k];
				}
				if(flownorth>flow){xflow[j][k]=j-1;yflow[j][k]=k;flow=flownorth;}
				flowwest=0;
				if(k)
				{
					if(alt[j][k-1]<alt[j][k])flowwest=alt[j][k]-alt[j][k-1];
				}
				if(flowwest>flow){xflow[j][k]=j;yflow[j][k]=k-1;flow=flowwest;}
				floweast=0;
				if(k<w-1)
				{
					if(alt[j][k+1]<alt[j][k])floweast=alt[j][k]-alt[j][k+1];
				}
				if(floweast>flow){xflow[j][k]=j;yflow[j][k]=k+1;flow=floweast;}
				flowsouth=0;
				if(j<h-1)
				{
					if(alt[j+1][k]<alt[j][k])flowsouth=alt[j][k]-alt[j+1][k];
				}
				if(flowsouth>flow){xflow[j][k]=j+1;yflow[j][k]=k;flow=flowsouth;}
			}
		}
		printf("Case #%d:\n",i);
		nbasin=0;
		for(j=0;j<h;j++)
		{
			for(k=0;k<w;k++)
			{
				xbasin[j][k]=j;ybasin[j][k]=k;
				while(1)
				{
					x0=xbasin[j][k];y0=ybasin[j][k];
					x1=xflow[x0][y0];y1=yflow[x0][y0];
					xbasin[j][k]=x1;ybasin[j][k]=y1;
					if((x0==x1)&&(y0==y1))break;
				}
				numbasin=nbasin;
				for(l=0;l<nbasin;l++)
				{
					if((x1==basinx[l])&&(y1==basiny[l])){numbasin=l;break;}
				}
				if(numbasin==nbasin){basinx[nbasin]=x1;basiny[nbasin]=y1;nbasin++;}
				printf("%c ",numbasin+'a');
			}
			printf("\n");
		}

	}
	return 0;
}