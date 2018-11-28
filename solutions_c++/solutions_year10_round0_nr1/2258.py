#include <stdio.h>
#include <afxtempl.h>
#include <afxwin.h>
#include <math.h>


void snapper(FILE *file,int n, long k, int t)
{
	if (k < pow(2,n) - 1)
	{
		fprintf(file,"Case #%d: OFF\n",t);
	} 
	else 
	{
		if (k > pow(2,n) - 1)
		{
			k = k - (pow(2,n) - 1);
			if (k%((int)(pow(2,n))) == 0)
			{
				fprintf(file,"Case #%d: ON\n",t);
			}
			else
				fprintf(file,"Case #%d: OFF\n",t);;
		}
		else
			fprintf(file,"Case #%d: ON\n",t);
	}
	
}
void main()
{
	FILE *file,*wfile;

	if ((file = fopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\googlecodejam\\A-large.in","rw")) == NULL)
	{
		printf("open file fail!");
	}
	if ((wfile = fopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\googlecodejam\\largeoutput.in","w")) == NULL)
	{
		printf("open file fail!");
	}
	long ch;

	int t,n,c = 1;
	long k;


	fscanf(file,"%d",&ch);

	t = (int)ch;
	fscanf(file,"%d",&ch);

	while (t > 0)
	{
		n = (int)ch;

		fscanf(file,"%d",&ch);
		k = (long)ch;

		fscanf(file,"%d",&ch);
		snapper(wfile, n, k, c);
		c ++;
		t --;
	}
	fclose(file);
	fclose(wfile);

}