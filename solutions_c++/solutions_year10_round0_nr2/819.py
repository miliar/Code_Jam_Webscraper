#include <stdio.h>
#include <malloc.h>
#include <afxtempl.h>
#include <afxwin.h>
#include <math.h>


void fair(FILE *file,int n, long g[], int t)
{
	long happentime,lasthtime = 0;
	long mindiff,df,diff1,diff2;
	int i,curmod;

	if (n == 2)
	{
		diff1 = abs(g[1] - g[0]);
		mindiff = diff1;
	}
	else
	{
		diff1 = abs(g[1] - g[0]);
		diff2 = abs(g[2] - g[1]);
		if (diff1 == 0 || diff2 == 0)
		{
			mindiff = diff1<diff2?diff2:diff1;
		}
		else
		{
			curmod = diff1%diff2;
			while (curmod)
			{				
				diff1 = diff2;
				diff2 = curmod;
				curmod = diff1%diff2;
			//	diff2 = diff2%diff1;//abs(diff2 - diff1);
			}
			mindiff = diff1>diff2?diff2:diff1;
		}
		
	}
	
/*	for (i = 1;i < n-1;i++)
	{
		if (mindiff > abs(g[i+1] - g[i]))
		{
			mindiff = abs(g[i+1] - g[i]);
		}
	}*/
	lasthtime = g[n-1];
	if (mindiff == 1)
	{
		lasthtime = 0;
	}
	else
	{
		while (lasthtime > 0)
		{
			lasthtime -= mindiff;
		}
	}
	
	happentime = abs(lasthtime);
	fprintf(file,"Case #%d: %ld\n",t,happentime);
}
void main()
{
	FILE *file,*wfile;

	if ((file = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\fairwarning\\B-small-attempt0.in","rw")) == NULL)
	{
		printf("open file fail!");
	}
	if ((wfile = fopen("C:\\Documents and Settings\\Administrator\\◊¿√Ê\\googlecodejam\\fairwarning\\B-small-output0.in","w")) == NULL)
	{
		printf("open file fail!");
	}
	long ch;
	int c = 1,t,n,ni = 0;
	long* g = NULL;


	fscanf(file,"%ld",&ch);
	t = (int)ch;

	while (t > 0)
	{
		fscanf(file,"%ld",&ch);
		n = (int)ch;

		if (g == NULL)
		{
		//	g = new int[n];
			if ((g = (long *)(malloc(n*sizeof(long)))) == NULL)
			{
				printf("…Í«Îƒ⁄¥Ê ß∞‹");
			}
		}
		
		ni = 0;
		while (ni < n)
		{
			fscanf(file,"%ld",&ch);
			g[ni] = (long)ch;
			ni ++;
		}
		
		fair(wfile, n, g, c);
		free(g);
		g = NULL;
		c ++;
		t --;
	}
	fclose(file);
	fclose(wfile);

}