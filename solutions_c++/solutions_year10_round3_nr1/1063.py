#include <stdio.h>
#include <malloc.h>
#include <afxtempl.h>
#include <afxwin.h>
#include <math.h>


void Rope(FILE *file,int n, int g[], int t)
{
	int itcount = 0;
	int i,j;
	int leftcom = 0, rightcom;

	for (i=1;i<n;i++)
	{
		for (j=0;j<i;j++)
		{
			leftcom = 0;
			rightcom = 0;
			if (g[2*i] > g[2*j])
			{
				leftcom = 1;
			}
			if (g[2*i+1] > g[2*j+1])
			{
				rightcom = 1;
			}
			if (leftcom+rightcom == 1)
			{
				itcount++;
			}
		}

	}
	fprintf(file,"Case #%d: %d\n",t,itcount);
}
void main()
{
	FILE *file,*wfile;

	if ((file = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\RopeIntranet\\A-large.in","rw")) == NULL)
	{
		printf("open file fail!");
	}
	if ((wfile = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\RopeIntranet\\A-large-output0.in","w")) == NULL)
	{
		printf("open file fail!");
	}

	long ch;
	int c = 1,t,n,ni = 0;
	int* data = NULL;


	fscanf(file,"%d",&ch);
	t = (int)ch;

	while (t > 0)
	{
		fscanf(file,"%d",&ch);
		n = (int)ch;

		if (data == NULL)
		{
			if ((data = (int *)(malloc(n*2*sizeof(int)))) == NULL)
			{
				printf("…Í«Îƒ⁄¥Ê ß∞‹");
			}
		}
		
		ni = 0;
		while (ni < n)
		{
			fscanf(file,"%d",&ch);
			data[2*ni] = (int)ch;
			fscanf(file,"%d",&ch);
			data[2*ni+1] = (int)ch;
			ni ++;
		}
		
		Rope(wfile, n, data, c);
		free(data);
		data = NULL;
		c ++;
		t --;
	}
	fclose(file);
	fclose(wfile);

}