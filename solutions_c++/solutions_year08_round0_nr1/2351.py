#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <ostream>
#include <map>
#include <algorithm>

using namespace std;

ifstream ifsInput("A-large.in");
ofstream ofsOutout("A-large.out");

typedef map<string, int> mapSearch;
mapSearch g_mSearch;
vector<int> g_vSearchID;

void main()
{
	int N;
	string temp;
	if(getline(ifsInput, temp))
	{
		N = atoi(temp.c_str());
	}

	int S,Q;
	for(int i=1; i<=N; i++)
	{
		int SwitchCouts = 0;
		g_mSearch.clear();
		g_vSearchID.clear();

		// read the counts of SE
		if(getline(ifsInput, temp))
		{
			S = atoi(temp.c_str());
		}

		// read the SE's name
		for(int j=1; j<=S; j++)
		{
			if(getline(ifsInput, temp))
			{
				g_mSearch[temp] = j;
				g_vSearchID.push_back(j);
			}
		}

		// read the counts of Query
		if(getline(ifsInput, temp))
		{
			Q = atoi(temp.c_str());
		}
		
		// read the Query'name
		vector<int>::iterator viter;
		for(j=1; j<=Q; j++)
		{
			if(getline(ifsInput, temp))
			{
				viter = find(g_vSearchID.begin(), g_vSearchID.end(), g_mSearch[temp]);
				
				if(viter != g_vSearchID.end())
				{
					if(g_vSearchID.size() > 1)
					{
						g_vSearchID.erase(viter);
					}
					else
					{
						SwitchCouts++;
						
						// init the g_vSearchID
						g_vSearchID.clear();
						for(int k=1; k<=S; k++)
						{
							g_vSearchID.push_back(k);
						}

						viter = find(g_vSearchID.begin(), g_vSearchID.end(), g_mSearch[temp]);
						g_vSearchID.erase(viter);
					}
				}
			}
		}

		cout << "Case #" << i << ": " << SwitchCouts << endl;
		ofsOutout << "Case #" << i << ": " << SwitchCouts << endl;
		
	}

	ifsInput.close();
	ofsOutout.close();
}