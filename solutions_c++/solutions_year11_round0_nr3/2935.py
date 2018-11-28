#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

int main()
{
	FILE *in=fopen("d:/input.in.txt","r");
    FILE *out=fopen("d:/output.txt","w");
	FILE *outin=fopen("d:/inputFormat.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
	fprintf(outin,"%d",T);
	vector <int> vvv;
	int initBinPos=1;
	for (int i=0; i<(1<<22);i++)
	{
		if ( !(i < 1<<initBinPos ) )
			initBinPos++;

		vvv.push_back(initBinPos);
	}

    for (int ii=0;ii < T ;ii++)
    {
		int maxVal=-1;
		int N = 0;
 		fscanf(in,"%d",&N);
		fprintf(outin,"\n%d:%d\n",ii+1,N);
		vector <int> v;
		for (int i=0;i < N ;i++)
        {
			int n;
			fscanf(in,"%d ",&n); 
			fprintf(outin,"%d ",n);
			v.push_back(n);
		}
		int sz=v.size();
		for (int i=0;i<(1<<sz);i++)
		{
			int Sean = 0,actualSean=0;
			int patrick = 0,actualPatrick=0;
			for (int j=0;j<sz;j++) 
			{
				int posval = i & (1 << j);
				if ( posval == 0 )
				{
					actualSean=actualSean+v[j];
					for ( int k=0;k<vvv[v[j]];k++)
					{
						int prod=1<<k;
						int valInp = v[j]&prod;
						int valSean = Sean&prod;
						if ( valInp )
						{
							if ( valSean )
							{
								Sean &= ~(1 << k); 
							}
							else
							{
								Sean |= 1 << k; 
							}
						}
						else if ( valSean )
						{
							Sean |= 1 << k; 
						}
					}
				}
				else
				{
					actualPatrick=actualPatrick+v[j];
					for ( int k=0;k<vvv[v[j]];k++)
					{
						int prod=1<<k;
						int valInp = v[j]&prod;
						int valP = patrick&prod;
						if ( valInp )
						{
							if ( valP )
							{
								patrick &= ~(1 << k); 
							}
							else
							{
								patrick |= 1 << k; 
							}
						}
						else if ( valP )
						{
							patrick |= 1 << k; 
						}
					}
				}
			}
			if ( patrick == Sean &&  actualSean > 0 && actualPatrick >0 )
			{
				maxVal=max(maxVal,actualSean);
				maxVal=max(maxVal,actualPatrick);
			}
		}
		if ( maxVal == -1 )
			fprintf(out,"Case #%d: NO\n",ii+1);
		else
			fprintf(out,"Case #%d: %d\n",ii+1,maxVal);

	}
	return 0;
}
