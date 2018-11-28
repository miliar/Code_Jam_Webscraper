#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

#include <fstream>

using namespace std;

void main()
{
	ifstream f;
	f.open("b-large.in");

	char l[1];
	int cases;
	f >> cases;
	f.getline(l, 1);

	ofstream out;
	out.open("b-large.out");

	for (int tc = 0; tc < cases; ++tc)
	{
		int nrules;
		f >> nrules;

		//cout << "Rules:" << endl;
		map<string, char> rules;
		for (int r = 0; r < nrules; ++r)
		{
			string rule;
			f >> rule;
			string combo = rule.substr(0, 2);
			rules[combo] = rule[2];
			string rev(combo.rbegin(), combo.rend());
			rules[rev] = rule[2];
			//cout << rule << endl;
		}

		//cout << "Opposing:" << endl;
		set<string> opps;
		int nopp;
		f >> nopp;
		for (int o = 0; o < nopp; ++o)
		{
			string opp;
			f >> opp;
			opps.insert(opp);
			string rev(opp.rbegin(), opp.rend());
			opps.insert(rev);
			//cout << opp << endl;
		}

		int ninv;
		f >> ninv;
		string inv;
		f >> inv;

		//cout << "Invoke: " << inv << endl << endl;

		vector<char> es;
		for (size_t i = 0; i < inv.size(); ++i)
		{
			char toInvoke = inv[i];
			if (es.empty())
			{
				es.push_back(toInvoke);
				continue;
			}

			char last = es.back();
			string combo = string(&last, 1) + string(&toInvoke, 1);
			if (rules.find(combo) != rules.end())
			{
				es.pop_back();
				es.push_back(rules[combo]);
				continue; //?
			}

			for (size_t o = 0; o < es.size(); ++o)
			{
				string p = string(&es[o], 1) + string(&toInvoke, 1);
				if (opps.find(p) != opps.end())
				{
					es.clear();
					break;
				}
			}
			if (es.empty()) continue;
			es.push_back(toInvoke);
		}

		out << "Case #" << tc+1 << ": " << "[";
		
		for (size_t a = 0; a < es.size(); ++a)
		{
			out << es[a];
			if (a < es.size()-1)
				out << ", ";
		}
		out << "]" << endl;
	}

	out.close();



}