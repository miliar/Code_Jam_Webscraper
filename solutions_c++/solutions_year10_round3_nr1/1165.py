#include<stdio.h>
int main()
{
	FILE *in,*out;
	in=fopen("in.in","r");
	out=fopen("out.out","w");
	int tc, tc1,n,a[1000],b[1000],i,j;
	long count;
	fscanf(in,"%d\n",&tc);

	tc1=tc;
	while(tc--)
	{
		fscanf(in,"%d\n",&n);
		i=0;
		count=0;
		while(i<n)
		{
			fscanf(in,"%d %d\n",&a[i],&b[i]);
			for(j=0;j<i;j++)
			{
				if((a[i]-a[j])*(b[i]-b[j]) < 0)
					count++;
			}
			i++;
		}
		fprintf(out,"Case #%d: %ld\n",tc1-tc,count);
	}
	return 0;
}
