#include <stdio.h>
#include <malloc.h>
#include <afxtempl.h>
#include <afxwin.h>
#include <math.h>


void theme(FILE *file,int r, long k, int n, int g[], int t)
{
	int dollar = 0, num = 0,i = 0,nsum = 0;
	for (i = 0; i < n; i ++)
		nsum += g[i];
	if (k > nsum)
	{
		fprintf(file,"Case #%d: %d\n",t,r*nsum);
	}
	else
	{
		i = 0;
		while (r>0)
		{
			num = 0;
			while (num <= k)
			{
				num += g[i];
				i = (++i)%n;
			}
			i = ((--i)+n)%n;
			num -= g[i];
			dollar += num;
			r --;
		}
		
		fprintf(file,"Case #%d: %d\n",t,dollar);
	}
	
}
void main()
{
	FILE *file,*wfile;

	if ((file = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\theme\\C-small-attempt19.in","rw")) == NULL)
	{
		printf("open file fail!");
	}
	if ((wfile = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\theme\\smalloutput.in","w")) == NULL)
	{
		printf("open file fail!");
	}
	long ch;
	int t,r,k,n,c = 1,ni = 1;
	int* g = NULL;

	fscanf(file,"%d",&ch);
	t = (int)ch;

	while (t > 0)
	{
		fscanf(file,"%d",&ch);
		r = (int)ch;

		fscanf(file,"%d",&ch);
		k = (int)ch;

		fscanf(file,"%d",&ch);
		n = (int)ch;

		if (g == NULL)
		{
			if ((g = (int *)(malloc(n*sizeof(int)))) == NULL)
			{
				printf("…Í«Îƒ⁄¥Ê ß∞‹");
			}
		}
		
		ni = 0;
		while (ni < n)
		{
			fscanf(file,"%d",&ch);
			g[ni] = (int)ch;
			ni ++;
		}
		
		theme(wfile, r, k, n, g, c);
		free(g);
		g = NULL;
		c ++;
		t --;
	}
	fclose(file);
	fclose(wfile);

}