#include <stdio.h>

int n,lw,hg;
int a[10002];
FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

void process()
{
	int i,j;
	int flag=0;

	for(i=lw ; i<=hg ; i++)
	{
		flag=0;
		for(j=1 ; j<=n ; j++)
		{
			if(i>a[j])
			{
				if(i%a[j]!=0)
				{
					flag=1;
					break;
				}	
			}
			else
			{
				if(a[j]%i!=0)
				{
					flag=1;
					break;
				}
			}
		}
		if(flag==0)
		{
			fprintf(out,"%d\n",i);
			return;
		}
	}
	fprintf(out,"NO\n");
}
int main()
{
	int i,t,j;

	fscanf(in,"%d ",&t);
	for(i=1 ; i<=t ; i++)
	{
		fscanf(in,"%d %d %d ",&n,&lw,&hg);
		for(j=1 ; j<=n ; j++)
			fscanf(in,"%d ",&a[j]);
		fprintf(out,"Case #%d: ",i);
		process();
	}
	return 0;
}
