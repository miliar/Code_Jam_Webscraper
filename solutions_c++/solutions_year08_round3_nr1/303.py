#include <cmath>
#include <map>
#include <deque>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
typedef long long lint;
using namespace std;
typedef pair<lint, lint> Key;
bool Cmp (const Key &a, const Key &b)
{
	return a.second < b.second;
}
int main()
{	
	lint cases;
	string tmp;
	ifstream input("input.txt");	
	ofstream output("output.txt");
	input >> cases;		
	vector<Key> keys;
	lint p, k, l;
	vector<deque<lint>> pad;
	map<lint, lint> cost;
	for(lint t = 1; t <= cases; t++)
	{		
		input >> p >> k >> l;
		keys.assign(l, Key());
		pad.assign(k, deque<lint>());
		cost.clear();
		for(lint i = 0; i < keys.size(); i++)
		{
			input >> keys[i].second;
			keys[i].first = i;
		}
		sort(keys.rbegin(), keys.rend(), &Cmp);
		for(lint i = 0; i < keys.size(); i++)
		{	

			pad[i % pad.size()].push_back(keys[i].first);
			cost[keys[i].first] = pad[i % pad.size()].size();
		}
		lint ret = 0;
		for(lint i = 0; i < keys.size(); i++)
			ret += cost[keys[i].first] * keys[i].second;
		output << "Case #" << t << ": " << ret << endl;
	}
	return 0;
}