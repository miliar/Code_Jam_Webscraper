#include <stdio.h>
#include <string.h>

int  main(void)
{
    int  n,c,p,l,k,i,j;
    long int temp;

    FILE *fp,*fpo;

	if((fp= fopen("d:\\codejam\\A-small.in","r"))==NULL)
	{printf("Error oprning file input.in");return 0;}

	if((fpo= fopen("d:\\codejam\\A-smallO.txt","w"))==NULL)
	{printf("Error oprning file output.txt");return 0;}

	fscanf(fp,"%d",&n);

	for (c=0; c<n; c++)
	{
	    fscanf (fp,"%d %d %d",&p,&k,&l);

	     long int freq[1000],ans=0;

	     for (i=0; i<l;i++)
	     {
		 fscanf(fp,"%ld",&freq[i]);
	     }

	     for (i=0;i<l-1;i++)
	    {
		for (j=i+1;j<l;j++)
		{
		if (freq[j]>freq[i])
		{
		    temp=freq[i];
		    freq[i]=freq[j];
		    freq[j]=temp;
		}
		}
	    }

	int t=1;
	for (i=0; i<l;)
	{
	    for (j=0; j<k;j++)
	    {
		ans = ans+freq[i]*t;
	    }
	    t++;
	}

	if (c!=n-1)
		fprintf (fpo,"Case #%d: %d\n",c+1,ans);
	   else
		fprintf (fpo,"Case #%d: %d",c+1,ans);
	}
fclose(fp);
fclose(fpo);
return 1;
}
