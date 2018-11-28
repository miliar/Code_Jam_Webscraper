#include<stdio.h>

double a[1000005];
double a1[1000005];
int b[1000005];
int e[1000005];
int sp[1000005];
int n,m,x,s,r;

int main()
{
	int i,j,k,l;
	double t,sum,next;
	double la;
	FILE *fp1=fopen("input.in","r");
	FILE *fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&m);
	for(l=1;l<=m;l++)
	{
		fscanf(fp1,"%d %d %d %lf %d",&x,&s,&r,&t,&n);
		for(i=0;i<=1000;i++)
			a[i]=a1[i]=0;
		for(i=1;i<=n;i++)
		{
			fscanf(fp1,"%d %d %d\n",&b[i],&e[i],&sp[i]);
			a[sp[i]+s]+=(double)(e[i]-b[i])/(sp[i]+s);
		}
		e[0]=0;
		b[n+1]=x;
		for(i=1;i<=n+1;i++)
			a[s]+=(double)(b[i]-e[i-1])/s;
		for(i=1;i<=1000;i++)
		{
			sum=a[i]*(i)/(i+r-s);
			if(t>=sum)
			{
				t-=sum;
				a1[i+r-s]+=sum;
			}
			else if(t==0)
			{
				a1[i]+=a[i];
			}
			else
			{
				a1[i+r-s]+=t;
				a1[i]+=(a[i]*i-t*(i+r-s))/i;
				t=0;
			}
		}
		la=0;
		for(i=0;i<=1000;i++)
		{
			la+=a1[i];
		}
		fprintf(fp2,"Case #%d: %lf\n",l,la);
	}
	fclose(fp1);
	fclose(fp2);
}