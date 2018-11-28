#include <stdio.h>
#include <string.h>
#include <iostream>

#include <map>
#include <string>

using namespace std;

#define MAX_SWITCHNUM 1001
#define MAX_SEARCHENGINE 100
#define MAX_QUERY 1000

void main()
{
	char buff[256]; // input buffer

	int n; // the number of cases 
	gets(buff);
	sscanf(buff, "%d", &n);

	for(int i = 0; i < n; i++) // case i
	{
		int s; // the number of search engines
		gets(buff);
	 	sscanf(buff, "%d", &s);
		//cout << s << endl;

		map<string, int> se; // search engines
		typedef pair <string, int> Pair_SE;

		for(int j = 0; j < s; j++) // search engine j
		{
			gets(buff);
			string sename(buff); // the name of a search engine
				
			//cout << "se " << j << " " << sename << endl;

			se.insert(Pair_SE(sename, j));
		}

		int q; // the number of incoming queries
		gets(buff);
		sscanf(buff, "%d", &q);

		// create optimal switch number table
		int tblOptSwitch[MAX_QUERY][MAX_SEARCHENGINE];

		for(int j = 0; j < q; j++) // query j
		{
			gets(buff);
			string query(buff); // a query

			if(j == 0) // first query
			{
				for(int m = 0; m < s; m++) // per search engine m
				{
					tblOptSwitch[j][m] = se[query] == m ? MAX_SWITCHNUM : 0;
				}
			}
			else
			{
				for(int m = 0; m < s; m++) // per search engine m
				{
					int iMinSwitch = MAX_SWITCHNUM;
					for(int n = 0; n < s; n++) // previously used search engine n
					{
						int iNewSwitch = se[query] == m ? MAX_SWITCHNUM : m != n ? tblOptSwitch[j-1][n] + 1 : tblOptSwitch[j-1][n];

						if(iNewSwitch < iMinSwitch)
							iMinSwitch = iNewSwitch;
					}
					tblOptSwitch[j][m] = iMinSwitch;
				}
			}
		}

		int iOptSwitchNum = MAX_SWITCHNUM;
		if(q <= 0)
		{
			iOptSwitchNum = 0;
		}
		else
		{
			for(int m = 0; m < s; m++)
			{
				if(tblOptSwitch[q-1][m] < iOptSwitchNum)
					iOptSwitchNum = tblOptSwitch[q-1][m];
			}
		}
						
//		cout << "Case #" << i + 1 << ": " << s << " " << q << " " << iOptSwitchNum << endl;
		cout << "Case #" << i + 1 << ": " << iOptSwitchNum << endl;
	}
	cout << endl;
}