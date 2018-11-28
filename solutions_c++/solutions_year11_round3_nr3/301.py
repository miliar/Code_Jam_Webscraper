#include<stdio.h>

int t,n;
__int64 l,h;
__int64 a[100005];

int main()
{
	FILE *fp1;
	FILE *fp2;
	int i,k,temp,p,l1;
	__int64 la;
	__int64 j;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(fp1,"%d",&n);
		fscanf(fp1,"%I64d %I64d",&l,&h);
		la=0;
		for(j=1;j<=n;j++)
			fscanf(fp1,"%I64d",&a[j]);
		for(j=1;j<=n;j++)
			for(k=j+1;k<=n;k++)
				if(a[j]>a[k])
					temp=a[j],a[j]=a[k],a[k]=temp;
		for(j=l;j<=h;j++)
		{
			p=0;
			for(k=1;k<=n;k++)
			{
				if(a[k]%j==0 || j%a[k]==0)
				{
					p+=1;
				}
			}
			if(p==n)
			{
				la=j;
				break;
			}
		}
		if(la==0)
			fprintf(fp2,"Case #%d: NO\n",i);
		else
			fprintf(fp2,"Case #%d: %I64d\n",i,la);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}