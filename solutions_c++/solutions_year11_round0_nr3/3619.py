#include<stdio.h>

int t,n;
int a[10005];
int b[105];

int main()
{
	int i,j,min,la,k,l;
	FILE *fp1=fopen("input.in","r");
	FILE *fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(fp1,"%d",&n);
		la=0;
		l=0;
		min=2140000000;
		for(j=1;j<=30;j++)
			b[j]=0;
		for(j=1;j<=n;j++)
		{
			fscanf(fp1,"%d",&a[j]);
			if(a[j]<min)
				min=a[j];
			la+=a[j];
			for(k=1;k<=30;k++)
			{
				b[k]=(b[k]+a[j]%2)%2;
				a[j]/=2;
			}
		}
		for(j=1;j<=30;j++)
			if(b[j]!=0)
				l++;
		if(l!=0)
			fprintf(fp2,"Case #%d: NO\n",i);
		else
			fprintf(fp2,"Case #%d: %d\n",i,la-min);
	}
	fclose(fp1);
	fclose(fp2);
}