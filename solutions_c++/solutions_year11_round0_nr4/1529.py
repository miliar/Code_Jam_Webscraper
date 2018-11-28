#include<stdio.h>

int main()
{
    FILE *fp,*fp1;
    fp1=fopen("input.in","r");
    fp=fopen("output.out","w");
    int t,count=0,n=0;
    fscanf(fp1,"%d",&t);
    for(int i=0;i<t;i++)
    {
	fscanf(fp1,"%d",&n);
	for(int j=0;j<n;j++)
	{
	    int k;
	    fscanf(fp1,"%d",&k);
	    if((j+1)!=k)
		count++;
	}
	fprintf(fp,"Case #%d:\t %d\n",i+1,count);
	count=0;
	//fprintf(fp,"\n");
    }
    return 0;
}
