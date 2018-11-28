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

using namespace std;

int main()
{
	FILE *in=fopen("d:/input.in.txt","r");
    FILE *out=fopen("d:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
    for (int ii=0;ii < T ;ii++)
    {
		int N = 0;
 		fscanf(in,"%d",&N); 
		vector < pair<char,int> > seq;
	    for (int i=0;i < N ;i++)
        {
			char c;
			fscanf(in," %c",&c); 
			int p;
			fscanf(in," %d",&p); 
			seq.push_back( make_pair(c,p) );
		}

		int lastor=1;
		int lastbl=1;
		int or=0,bl=0;
		int max=1;
		for ( int i=0;i < N ;i++)
		{
			if ( seq[i].first == 'O' )
			{
				int secondsrequired = abs(seq[i].second-lastor);
				lastor = seq[i].second;
				or=or+secondsrequired+1;
				if ( or<=bl )
					or=bl+1;
			}
			else
			{
				int secondsrequired = abs(seq[i].second-lastbl);
				lastbl=seq[i].second;
				bl=bl+secondsrequired+1;
				if ( bl<=or )
					bl=or+1;
			}
		}
		int val= ( or > bl) ? or:bl;
		fprintf(out,"Case #%d: %d\n",ii+1,val);
	}
	return 0;
}