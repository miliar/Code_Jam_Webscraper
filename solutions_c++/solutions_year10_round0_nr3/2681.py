//theme park
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>

int _tmain(int argc, _TCHAR* argv[])
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int T,R,k,N,price,gr;
	int g[1500],h[1500];
	int i,j,tc,cnt;
	
	//freopen("C:\A-small-practice.in","r",stdin);
	//freopen("C:\A-small-practice.out","w",stdout);
	fscanf(fp,"%d",&T);
	for(i=1;i<=T;i++)
	{
		price = 0;
		fscanf(fp,"%d%d%d",&R,&k,&N);
		for(j=0;j<N;j++)
			fscanf(fp,"%d",&g[j]);

		for(j=0;j<R;j++)
		{
			cnt = 0;
			for(tc=0;tc<N;tc++)
			{
				gr = tc;
				if((g[tc]+cnt) <= k)
				{
					cnt = cnt + g[tc];
					h[tc] = g[tc];
				}
				else
					break;
			}

			price = price + cnt;

			for(tc=0;tc<N-gr;tc++)
				g[tc] = g[gr+tc];

			for(tc = 0;tc<gr;tc++)
				g[N-gr+tc] = h[tc];
		}

		fprintf(ofp,"Case #%d: %d\n", i, price);
	}
	
	return 0;
}

