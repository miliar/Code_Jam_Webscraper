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
	FILE *in=fopen("C:/GCJ/CodeJam/CodeJam/input.in.txt","r");
    FILE *out=fopen("C:/GCJ/CodeJam/CodeJam/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
    for (int ii=0;ii < T ;ii++)
    {
		int R = 0,C=0;
 		fscanf(in,"%d %d",&R, &C);
		vector<string> dict;
		for (int i=1;i<=R;i++)
		{
			char s[52];
			fscanf(in,"%s ",&s); 
			string ss(s);
			dict.push_back(ss);
		}
		string bs="\\";
		bool possible=true;
		for (int i=0;i<R;i++)
		{
			for (int j=0;j<C;j++)
			{
				if ( dict[i][j]=='#' )
				{
					if ( ((i+1) < R) && ((j+1) < C) )
					{
						if ( dict[i][j+1]=='#' && dict[i+1][j]=='#' && dict[i+1][j+1]=='#' )
						{
							dict[i][j]='/';
							dict[i][j+1]=bs[0];
							dict[i+1][j]=bs[0];
							dict[i+1][j+1]='/';
						}
						else
						{
							possible=false;
						}
					}
					else
					{
						possible=false;
					}
				}
			}
		}
		
		fprintf(out,"Case #%d:\n",ii+1); 
		if ( !possible )
			fprintf(out,"Impossible\n"); 
		else
		{
			for (int j=0;j<R;j++)
			{
				fprintf(out," %s\n",dict[j].c_str()); 
			}
		}
	}
	return 0;
}
