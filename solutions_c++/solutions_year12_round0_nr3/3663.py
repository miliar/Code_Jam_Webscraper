#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <algorithm>

using namespace std;

int main ()
{
	int t, minv = 2000000, maxv = 0, base = 1;
	cin >> t;
	
	vector< pair<int, int> > v(t);
	vector<int> res(t);
	for(int i = 0; i < t; i++)
	{
		cin >> v[i].first >> v[i].second;
		set< pair<int, int> > myset;
		
		for(int j = v[i].first; j <= v[i].second; j++)
		{
			ostringstream oss;
			oss << j;
			string str= oss.str();
			
			for(int k = 0; k < (int)str.size(); k++)
			{
				string temp = str.substr((int)str.size() - k, k);
				temp += str.substr(0, (int)str.size() - k);
				
				if(temp[0] != '0' && temp != str)
				{
					istringstream iss(temp);
					int tem;
					iss >> tem;
					pair<int, int > p;
					p.first = min(j, tem);
					p.second = max(j, tem);
					if(v[i].first <= p.first && p.second <= v[i].second && myset.find(p) == myset.end())
					{
						myset.insert(p);
						break;
					}
				}
			}
		}
		res[i] = (int)myset.size();
	}

	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": " << res[i] << endl; 
	}
}