#include <iostream>
#include <cmath>
#include <map>
#include <list>
#include <string>

using namespace std;


int main()
{
	int T;
	cin >> T;
	
	
	for(int t = 0; t < T; t++)
	{
		map<string, string> comb;
		map<string, int> opp;
		list<char> final;

		comb.clear();
		opp.clear();
		final.clear();

		
		int C;
		int D;
		int N;

		cin >> C;
		for(int c = 0; c < C; c++)
		{
			string temp;
			cin >> temp;
			comb[temp.substr(0, 2)] = temp.substr(2,1);

		}
		cin >> D;
		for(int d = 0; d < D; d++)
		{
			string temp;
			cin >> temp;
			opp[temp] = 1;
		}

		cin >> N;
		for(int n = 0; n < N; n++)
		{
			char current;
			cin >> current;

			string att1;
			string att2;

			att1.push_back(current);			
			if(final.size() > 0)
			{
				att1.push_back(*final.rbegin());
				att2.push_back(*final.rbegin());
			}
			att2.push_back(current);

			if(comb[att1] != "")
			{
				final.pop_back();
				final.push_back(comb[att1][0]);
			}
			else
			if(comb[att2] != "")
			{
				final.pop_back();
				final.push_back(comb[att2][0]);
			}
			else
				final.push_back(current);

			list<char>::reverse_iterator iter = final.rbegin();
			char demo = *iter;
			iter++;

			for(;iter != final.rend() ;iter++)
			{
				string test1;
				string test2;
				test1.push_back(demo);
				test1.push_back(*iter);
				test2.push_back(*iter);
				test2.push_back(demo);

				if(opp[test1] == 1 || opp[test2] == 1)
				{
					final.clear();
					break;
				}
			}


		}
		cout << "Case #"  << t+1 << ": [";

		for(list<char>::iterator iter = final.begin(); iter != final.end(); iter++)
		{
			list<char>::iterator check = iter;
			if(++check == final.end())
				cout << *iter;
			else
				cout << *iter << ", ";
		}

		cout << "]" << endl;
	}
	return 0;
}