#include <map>
#include <deque>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;
typedef vector<pair<int, int>> VI;
typedef vector<VI> VI2;
bool IsSatisfied(const VI2 & c, int customer, int coctail, int malted)
{
	for(int i = 0; i < c[customer].size(); i++)
		if(c[customer][i] == pair<int, int>(coctail, malted))
			return true;
	return false;
}
bool TryBitmask(const VI2 & c, vector<int> & out)
{
	int best = INT_MAX / 4;
	vector<int> fout(out.size());
	vector<int> sat(c.size(), 0);
	bool gotAns = false;
	for(int i = 0; i < (1 << out.size()); i++)
	{
		int totalMalted = 0;
		sat.assign(c.size(), 0);
		int rulez = sat.size();
		for(int j = 0; j < out.size(); j++)
		{
			fout[j] = (i & (1 << j)) != 0;
			totalMalted += fout[j];						 
			for(int k = 0; k < c.size(); k++)
			{
				if(IsSatisfied(c, k, j, fout[j]))
				{
					if(!sat[k])
						rulez--;
					sat[k] = 1;
				}
			}

		}
		if(totalMalted < best && !rulez)
		{
			best = totalMalted;
			out = fout;
			gotAns = true;
		}
	}
	return gotAns;
}

int main()
{	
	int cases;
	string tmp;
	ifstream input("input.txt");	
	ofstream output("output.txt");
	input >> cases;	
	VI2 c;	
	vector<int> out;
	int n, m, t;
	for(int l = 1; l <= cases; l++)
	{		
		input >> n >> m;		
		out.assign(n, 0);
		c.assign(m, VI());		
		for(int i = 0; i < m; i++)
		{
			input >> t;
			c[i].assign(t, pair<int, int>());
			for(int j = 0; j < t; j++)
			{
				input >> c[i][j].first >> c[i][j].second;
				c[i][j].first--;
			}
		}		
		output << "Case #" << l << ":";
		if(TryBitmask(c, out))
		{
			for(int i = 0; i < out.size(); i++)
				output << ' ' << out[i];
		}
		else
			output << " IMPOSSIBLE";
		output << endl;

	}
	return 0;
}