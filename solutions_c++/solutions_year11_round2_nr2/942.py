#include<stdio.h>

int p[1005];
int v[1005];
int temp;
int la[3][1000005];
int la1[3][1000005];
double last;

double mine(double a,double b,double c)
{
	if(a<=b && a<=c)
		return a;
	if(b<=a && b<=c)
		return b;
	return c;
}

void main()
{
	int i,j,k,l,t,n,d,m,sum=0,max=-2140000000,min=2140000000,l1,l2,x;
	FILE *fp1;
	FILE *fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(l=1;l<=t;l++)
	{
		fscanf(fp1,"%d %d",&n,&d);
		l1=0;
		for(i=1;i<=n;i++)
			fscanf(fp1,"%d %d",&p[i],&v[i]);
		for(i=1;i<=n;i++)
			for(j=i+1;j<=n;j++)
				if(p[i]>p[j])
				{
					temp=p[i],p[i]=p[j],p[j]=temp;
					temp=v[i],v[i]=v[j],v[j]=temp;
				}
		l1=1;
		last=0;
		for(i=1;i<=1000;i++)
			la[1][i]=la[2][i]=0;
		for(i=1;i<=n;i++)
		{
			la[1][l1]+=(v[i]-1)*d;
			if(i!=n)
			{
				if(p[i+1]-p[i]<=d)
				{
					la[1][l1]+=(d-(p[i+1]-p[i]));
				}
				else
				{
					la[2][l1]=(p[i+1]-p[i]-d)*2;
					l1++;
				}
			}
		}
		for(i=1;i<=l1;i++)
		{
			last+=la[1][i];
		}
		for(i=1;i<=i+1;i++)
		{
			if(l1==1)
				break;
			x=0;
			for(j=1;j<=l1;j++)
			{
				if(la[1][j]!=0)
					x++;
			}
			if(x!=0)
				last-=(x-1);
			for(j=1;j<l1;j++)
			{
				if(la[1][j]!=0 && la[2][j]!=0)
					la[2][j]--;
				if(la[1][j+1]!=0 && la[2][j]!=0)
					la[2][j]--;
				if(la[1][j]==0 && la[1][j+1]==0)
					la[2][j]=0;
				if(la[1][j]!=0)
					la[1][j]--;
			}
			if(la[1][l1]!=0)
				la[1][l1]--;
			l2=1;
			for(j=1;j<=l1;j++)
				la1[1][j]=la1[2][j]=0; 
			for(j=1;j<=l1;j++)
			{
				la1[1][l2]+=la[1][j];
				if(la[2][j]!=0)
				{
					la1[2][l2++]=la[2][j];
				}
			}
			l1=l2;
			for(j=1;j<=l2;j++)
				la[1][j]=la1[1][j],la[2][j]=la1[2][j];
		}
		fprintf(fp2,"Case #%d: %lf\n",l,last/2);
	}
	fclose(fp1);
	fclose(fp2);
}
