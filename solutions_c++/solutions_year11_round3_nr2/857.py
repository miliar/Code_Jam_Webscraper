#include<stdio.h>
#include<stdlib.h>
int m;
long int l,n,c,t;
int main()
{
	long int i1,i,j,k,a[1001],k1,b[1001],p;
	long int s,ss;
	FILE *fp,*dp;
	fp=fopen("d:\\a.txt","r");
	if(!fp) exit(0);
	dp=fopen("d:\\b.txt","w");
	if(!dp) exit(0);
	fscanf(fp,"%d",&m);
	for(i1=1;i1<=m;i1++)
	{
		fscanf(fp,"%ld",&l);
		fscanf(fp,"%ld",&t);
		fscanf(fp,"%ld",&n);
		fscanf(fp,"%ld",&c);
		for(j=0;j<c;j++)
			fscanf(fp,"%ld",&a[j]);
		k=0;
		k1=0;
		s=0;
		ss=s+a[0]*2;
		while(ss<t && k1<n)
		{
			s=s+a[k]*2;
			k++;
			k1++;
			if(k==c)
				k=0;
			if(k1!=n)
				ss=s+a[k]*2;
		}
		if(k1==n)
		{
			fprintf(dp,"Case #%d: %ld\n",i1,s);
			continue;
		}
		b[0]=(ss-t)/2;
		i=1;
		k++;
		while(k1<n)
		{
			b[i]=a[k];
			i++;
			k++;
			k1++;
			if(k==c)
				k=0;
		}
		i--;
		for(j=0;j<i-1;j++)
			for(k=j+1;k<i;k++)
				if(b[j]<b[k])
				{
					p=b[j];
					b[j]=b[k];
					b[k]=p;
				}
		s=t;
		for(j=0;j<i;j++)
		{
			if(j<l)
				s=s+b[j];
			else
				s=s+b[j]*2;
		}
		fprintf(dp,"Case #%d: %ld\n",i1,s);
	}
	fclose(fp);
	fclose(dp);
	return 0;
}