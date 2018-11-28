#include <iostream>
#include <list>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int cases, count, C, D, N, i, j;
	string in; //used for input
	string pair;
	
	map<string, char> comb;
	map<string, int> oposites; //0 means nothing, 1 means oposite elements
	string invokeList;
	vector<char> result;
	char current; //current element being invoked
	char toCombine; //element to be combined with
	
	cin >> cases;
	count = 1;
	
	while(count <= cases)
	{
		comb.clear();
		oposites.clear();
		result.clear();
		invokeList.clear();
		
		cin >> C;
		
		for(i=0; i<C; i++)
		{
			cin >> in;
			pair = in.substr(0, 2);
			comb[pair] = in[2];
			reverse(pair.begin(), pair.begin()+2);
			comb[pair] = in[2];
			
		}
		
		cin >> D;
		
		for(i=0; i<D; i++)
		{
			cin >> in;
			oposites[in] = 1;
			reverse(in.begin(), in.end());
			oposites[in] = 1;
		}
		
		cin >> N;
		cin >> invokeList;
		
		for(i=0; i<invokeList.length(); i++)
		{
			
			if(result.size() < 1) //no elements to compare with
			{
				result.push_back(invokeList[i]);
				continue;
			}
			
			current = invokeList[i];
			toCombine = result.back();
			
			
			string s;
			s.append(1, current);
			s.append(1, toCombine);
			
			char resElement1 = comb[s];
			reverse(s.begin(), s.end());
			char resElement2 = comb[s];
			
			if(resElement1 != 0)
			{
				result.pop_back();
				result.push_back(resElement1);
				continue;
			}
			else if(resElement2 != 0)
			{
				result.pop_back();
				result.push_back(resElement2);
				continue;
			}
			else //search for oposites
			{
				for(j = 0; j < result.size(); j++)
				{
					s.clear();
					s.append(1, result[j]);
					s.append(1, current);
					
					if(oposites[s] == 1)
						result.clear();
				}
				if(!result.empty())
					result.push_back(current);
			}
		}
		
		cout << "Case #" << count << ": [";
		
		for(i=0; i<result.size(); i++)
		{
			cout << result[i];
			if(i < result.size()-1)
				cout << ", ";
		}
		
		cout << "]" << endl;
		
		count++;
	}
	
	return 0;
}
