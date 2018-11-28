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
	int T = 0;
    fscanf(in,"%d",&T); 
    for (int ii=0;ii < T ;ii++)
    {
		int N = 0,PD=0,PG=0;
 		fscanf(in,"%d %d %d",&N,&PD,&PG);
		bool possible=false;
		for (int i=1;i<=N;i++)
		{
			int tpd=PD*i;
			if ( tpd%100 == 0 )
			{
				possible=true;
			}
			else
			{
				continue;
			}
		}
		if ( (PG==100 && PD!=100) || (PG==0 && PD!=0) )
			possible=false;

		if ( possible )
			fprintf(out,"Case #%d: %s\n",ii+1,"Possible"); 
		else
			fprintf(out,"Case #%d: %s\n",ii+1,"Broken");

	}
	return 0;
}
