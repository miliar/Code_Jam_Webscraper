#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *in, *out;

char welcome[] = "welcome to code jam";

int start(char*buffer)
{
	int dyn[1000][19] = {{0,},};
	int k;
	int i;
	for( k = 1; k < (int)strlen(buffer)+1; k++)
	{
		for( i = 0; i < 19; i++)
		{
			if( buffer[k-1] == welcome[i] )
			{
				if( i == 0 )
				{
					dyn[k][0] = dyn[k-1][0]+1;
				}
				else
				{
					dyn[k][i] = (dyn[k-1][i] + dyn[k-1][i-1])%10000;
				}
			}
			else
				dyn[k][i] = dyn[k-1][i];
		}
	}
	return dyn[k-1][18];
}

int main()
{
	in = fopen("C-large.in","r");
	out = fopen("output.txt","w");

	int n;
	fscanf(in,"%d",&n);

	char buffer[1000];
	int temp;
	fgets(buffer,1000,in);
	int k;
	for( k = 0; k < n; k++)
	{
		fgets(buffer,1000,in);
		temp = start(buffer);
		fprintf(out,"Case #%d: %d%d%d%d\n",k+1,temp%10000/1000,temp%1000/100,temp%100/10,temp%10);
	}
}