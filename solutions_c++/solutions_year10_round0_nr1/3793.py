#include <stdio.h>

main()
{
	unsigned long T,N,K,i;
	bool fl;
	FILE *fp,*f;
	fp=fopen("A-small.in","r");
	f=fopen("A-small.out","w");
	fscanf (fp,"%ld",&T);
	for (i=1;i<=T;i++)
	{
    	fscanf (fp,"%ld%ld",&N,&K);
    	fl=false;
    	if (K==0) {fprintf (f,"Case #%d: OFF\n",i);continue;}
        while (N!=0)
        {
    		if (K%2==0)
            {
            	fprintf (f,"Case #%d: OFF\n",i);
            	fl=true;
				break;
			}
			K=K/2;
			N--;
		}
		if (!fl) fprintf (f,"Case #%d: ON\n",i);
	}
	fclose(fp);
	fclose(f);
}
