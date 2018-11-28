#include <stdlib.h>
#include <conio.h>
#include <string.h>
#include <math.h>
#include <list>
#include <map>
#include <vector>
#include <stdio.h>
void citire(FILE *f,int &n, int&l, int &h, int *&freq)
{
	
	
	fscanf(f," %d %d %d ",&n,&l,&h);
	freq = (int*)malloc(n*sizeof(int));
	for (int i = 0; i< n ; i++)
	{
		fscanf(f," %d ", &freq[i]);

	}
	
}

void main()
{
	int m;
	FILE *f = fopen("in.txt","r");
	FILE *g = fopen("data.out","w");
	fscanf(f,"  %d ",&m);
	int n, l , h;
	int *freq = NULL;
	for (int k = 0; k<m; k++)
	{
	citire(f,n,l,h,freq);
	bool gasit=true;
	if (l ==1 )
	{
		fprintf(g,"Case #%d: 1\n",k+1);
		
	}
	else

	for (int i = l; i<=h; i++)
	{
		gasit =true;
		for (int j =0; j<n;j++)
			if ((i % freq[j] != 0) && (freq[j] % i != 0))
				gasit = false;
		if (gasit) 
		{
			
			fprintf(g,"Case #%d: %d\n", k+1, i );
			
			break;
		}
	}
	if (gasit == false)
	{
							fprintf(g,"Case #%d: NO\n",k+1);
			
	}

	}
	fclose(g);
}