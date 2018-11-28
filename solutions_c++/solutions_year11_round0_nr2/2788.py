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
		int C = 0;
 		fscanf(in,"%d",&C); 
		map< set<char>,char > mcc;
		set< set<char> > cc;
	    for (int i=0;i < C ;i++)
        {
			set <char> c;
			char ch1,ch2,ch3;
			fscanf(in," %c%c%c",&ch1,&ch2,&ch3); 
			c.insert(ch1);
			c.insert(ch2);
			cc.insert(c);
			mcc.insert( pair< set<char>,char >(c,ch3));
		}

		int D = 0;
 		fscanf(in," %d",&D); 
		set< set<char> > dd;
	    for (int i=0;i < D ;i++)
        {
			char ch1,ch2;
			set <char> d;
			fscanf(in," %c%c",&ch1,&ch2); 
			d.insert(ch1);
			d.insert(ch2);
			dd.insert(d);
		}

		int N = 0;
 		fscanf(in," %d ",&N);
		string chlist;
	    for (int i=0;i < N ;i++)
        {
			char ch;
			fscanf(in,"%c",&ch); 
			if ( chlist.size() == 0 )
			{
				chlist=chlist+ch;
			}
			else
			{
				set <char> temp;
				temp.insert(chlist[chlist.length()-1]);
				temp.insert(ch);
				if ( cc.find(temp) != cc.end() )
				{
					chlist[chlist.length()-1]=mcc[temp];
				}
				else
				{
					chlist=chlist+ch;
					for ( int a=0;a<chlist.size();a++ )
					{
						for ( int b=a+1;b<chlist.size();b++ )
						{
							set <char> temp2;
							temp2.insert(chlist[a]);
							temp2.insert(chlist[b]);
							if ( dd.find(temp2) != dd.end() )
							{
								chlist.clear();
								break;
							}
						}
					}
				}

			}
		}

		fprintf(out,"Case #%d: [",ii+1);
		for (int i=0;i < chlist.size() ;i++)
		{
			if ( i != (chlist.size()-1) )
			{
				fprintf(out,"%c, ",chlist[i]);
			}
			else
			{
				fprintf(out,"%c",chlist[i]);
			}
		}
		fprintf(out,"]\n");
	}
	return 0;
}