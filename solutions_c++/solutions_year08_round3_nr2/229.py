#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

#include <math.h>

#define PI 2*acos(0.0)
typedef long long int int64;
typedef unsigned long long int uint64;

using namespace std;
int main()
{
	int i,j,k,l,m,n;
	int64 testId, nTests;

	cin >> nTests;
	for(testId=1;testId<=nTests;testId++)
	{
		int64 ugly=0;
		cout << "Case #" << testId << ": ";
		//XXX  -- Read input --  XXX
		/*
		//scanf("%s %s", p1, p2);
		char str[1024];

        gets(str);
        if (str[0]=='\0')
        	gets(str);
		*/
		string in;
		cin >> in;

		//XXX  -- Process input --  XXX
		int d=in.length()-1;

		if (d==0)
		{
			int64 tot;
			const char *p = in.c_str();
			tot=(*p - '0');
			if ( (tot%2 == 0) ||  (tot%3 == 0) || (tot%5 == 0) || (tot%7 == 0))
			{
				ugly++;
			}
			cout << ugly << endl;
			continue;
		}
		//GENERATE COMBINATION
        vector<int> comb[d];
		for(i=0;i<d;i++)
		{
			comb[i].push_back(0);
			comb[i].push_back(1);
			comb[i].push_back(2);
		}

		vector<int>::iterator iter[d];
        for(i=0; i<d; i++)
			iter[i]=comb[i].begin();

		int combination;
		for(combination=1; 1; combination++)
		{
			for (i=0; i<d-1; i++)
			{
				if(iter[i] != comb[i].end())
					break;
				iter[i]=comb[i].begin();
				iter[i+1]++;
			}

			if (iter[d-1] == comb[d-1].end())
			{
				break;
			}

			const char *p;
			int prev_op=0;

			int64 tot=0;
			int64 val=0;
			int x=0;
			for(x=0, p=in.c_str(); *p; p++, x++)
			{
				int cur_op;
				if (prev_op==0)
				{
					tot*=10;
					tot+=(*p - '0');
					if(x<d)
					{
						cur_op=*(iter[x]);
					}
					else
					{
						cur_op=0;
					}
					prev_op = cur_op;
				}
				else
				{
					if(x<d)
					{
						cur_op=*(iter[x]);
					}
					else
					{
						cur_op=0;
					}
					switch( cur_op ) 
					{
						case 0:
							val*=10; val+=(*p - '0');
							break;
						case 1:
						case 2:
							val*=10; val+=(*p - '0');
							if (prev_op == 1)
							{
								tot=tot+val;
							}
							else if (prev_op == 2)
							{
								tot=tot-val;
							}
							else
							{
								cout << "ERROR in switch prev_op" << prev_op << endl;
							}
							val=0;
							prev_op=cur_op;
							break;
						default:
							cout << "ERROR in switch default " << cur_op << endl;
							break;
					}
				}
			}
			
			//cout << combination << ":" << tot;
						if (prev_op == 1)
							{
								tot=tot+val;
							}
							else if (prev_op == 2)
							{
								tot=tot-val;
							}
			//cout  << ":" << tot << endl;
			if ( (tot%2 == 0) ||  (tot%3 == 0) || (tot%5 == 0) || (tot%7 == 0))
			{
				ugly++;
			}


			iter[0]++;
		}

		//cout << (combination-1) << " ";
		cout << ugly << endl;

		//XXX  -- Print output --  XXX


	}

	return 0;
}
