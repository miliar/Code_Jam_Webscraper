#include<stdio.h>

int t;
int a[505][505];
char c[505];
double x,y,sx,sy,x1,y1,cx,cy;

int main()
{
	int i,j,k,l,n,m,d,kk,max;
	FILE *fp1=fopen("input.in","r");
	FILE *fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(l=1;l<=t;l++)
	{
		fscanf(fp1,"%d %d %d\n",&n,&m,&d);
		for(i=1;i<=n;i++)
		{
			fscanf(fp1,"%s",c);
			for(j=1;j<=m;j++)
			{
				a[i][j]=c[j-1]-'0';
			}
		}
		max=0;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				sx=a[i][j];
				x=y=0;
				for(k=1;k<=n;k++)
				{
					if(i+k==n+1||j+k==n+1)
						break;
					x-=sx/2;
					y-=sx/2;
					cx=i;
					cx+=i+k;
					cx/=2;
					cy=j;
					cy+=j+k;
					cy/=2;
					for(kk=0;kk<=k;kk++)
					{
						x+=a[i+kk][j+k]*(i+kk-cx);
						sx+=a[i+kk][j+k];
						y+=a[i+kk][j+k]*(j+k-cy);
					}
					for(kk=0;kk<k;kk++)
					{
						x+=a[i+k][j+kk]*(i+k-cx);
						sx+=a[i+k][j+kk];
						y+=a[i+k][j+kk]*(j+kk-cy);
					}
					x1=x;
					x1-=a[i][j]*(i-cx);
					x1-=a[i+k][j]*(i+k-cx);
					x1-=a[i][j+k]*(i-cx);
					x1-=a[i+k][j+k]*(i+k-cx);
					y1=y;
					y1-=a[i][j]*(j-cy);
					y1-=a[i+k][j]*(j-cy);
					y1-=a[i][j+k]*(j+k-cy);
					y1-=a[i+k][j+k]*(j+k-cy);
					if(x1==0 && y1==0 && k+1>max)
						max=k+1;
				}
			}
		}
		if(max>=3)
			fprintf(fp2,"Case #%d: %d\n",l,max);
		else
			fprintf(fp2,"Case #%d: IMPOSSIBLE\n",l);
	}
	fclose(fp1);
	fclose(fp2);
}