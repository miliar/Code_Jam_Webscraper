#include<stdio.h>
long group[1100];
int main()
{
	long t,k,n,a,b,r,income,entry,start,count;
	FILE *fp = fopen("C-small.in","r") , *ofp = fopen("C-small.out","w");
	fscanf(fp,"%ld",&t);
	for(a=1;a<=t;a++)
	{
		fscanf(fp,"%ld %ld %ld",&r,&k,&n);
		income = 0;
		for(b=0;b<(n-1);b++)
			fscanf(fp,"%ld ",&group[b]);
		fscanf(fp,"%ld",&group[b]);
		start = 0;
		for(b=0;b<r;b++)
		{
			entry = 0;
			count=0;
			while(entry<=k && count<n)
			{
				count++;
				entry += group[start];
				start = (start+1)%n;
			}
			start--;
			if(start<0)
				start+=n;
			income += entry;
			if(count<n || entry>k)
				income -= group[start];

		}
		fprintf(ofp,"Case #%ld: %ld\n",a,income);
	}
	return 0;
}