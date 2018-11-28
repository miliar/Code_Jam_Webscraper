#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

/*
int bsearch(string s, vector<string> vs)
{
	int lo=0; int hi=vs.size()-1;
	while(lo <= hi)
	{
		int mid = (lo+hi)/2;
		if (vs[mid] == s) return mid;
		else if (vs[mid] > s) hi=mid-1;
		else lo = mid+1;
	}
	return -1;
}
*/

int main()
{
	string line; stringstream ss;
	getline(cin, line);
	ss.clear(); ss.str(line);
	int ncase;
	ss >> ncase;
//	cout << "ncase: " << ncase << endl;

	vector<string> engines;
	vector<string> queries;
	for(int ix=0; ix < ncase; ix++)
	{
		engines.clear(); queries.clear();
		getline(cin, line);
		ss.clear(); ss.str(line);
		int nengine;
		ss >> nengine;
		for(int ie=0; ie < nengine; ie++)
		{
			getline(cin, line);
			engines.push_back(line);
		}
		getline(cin, line);
		ss.clear(); ss.str(line);
		int nquery;
		ss >> nquery;
		for(int iq=0; iq < nquery; iq++)
		{
			getline(cin, line);
			queries.push_back(line);
		}
		cout << "Case #" << ix+1 << ": ";
		int nswitch = 0;

			int nd = 0;
			vector<string> vprev;
			for(int iq=0; iq < nquery; iq++)
			{
				if (find(vprev.begin(), vprev.end(), queries[iq]) == vprev.end())	
				{
					vprev.push_back(queries[iq]); nd++;
					if (nd == nengine) 
					{ nswitch++; nd = 1; 
						string pp = vprev[vprev.size()-1];
						vprev.clear(); vprev.push_back(pp);
					}
				}
			}

		cout << nswitch << "\n";
	}
}
