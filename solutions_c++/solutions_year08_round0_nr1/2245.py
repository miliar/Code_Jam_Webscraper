#include <map>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{	
	int cases;
	string tmp;
	ifstream input("input.txt");	
	ofstream output("output.txt");
	getline(input, tmp);
	cases = atoi(tmp.c_str());	
	map<string, bool> engines;
	for(int l = 1; l <= cases; l++)
	{
		int s, q;
		engines.clear();
		getline(input, tmp);
		s = atoi(tmp.c_str());		
		for(int i = 0; i < s; i++)
		{
			getline(input, tmp);
			engines[tmp] = true;
		}
		getline(input, tmp);
		q = atoi(tmp.c_str());
		int switches = 0;
		int enginesLeft = engines.size();		
		for(int i = 0; i < q; i++)
		{
			string query;
			getline(input, query);
			if(engines[query])
			{
				if(enginesLeft == 1)
				{
					switches++;
					enginesLeft = engines.size();
					for(map<string, bool>::iterator j = engines.begin(); j != engines.end(); j++)
						j->second = true;
				}
				enginesLeft--;
				engines[query] = false;
			}
		}
		output << "Case #" << l << ": " << switches;
		if(l != cases)
			output << endl;
	}
	return 0;
}