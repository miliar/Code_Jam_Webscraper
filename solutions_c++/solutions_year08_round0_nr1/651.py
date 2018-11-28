#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	string t;
	for (int i = 0; i < N; i++)
	{
		int S = 0;
		cin >> S;
		getline(cin, t);
		map<string, int> s2i;
		for (int j = 0; j < S; j++)
		{
			string engineName;
			getline(cin, engineName);
			s2i[engineName] = j;
		}

		vector<int> changeCount(S);
		fill(changeCount.begin(), changeCount.end(), 0);

		int Q = 0;
		cin >> Q;
		getline(cin, t);
		for (int j = 0; j < Q; j++)
		{
			string query;
			getline(cin, query);
			
			int ind = s2i[query];
			int max = 2000;
			for (int k = 0; k < S; k++)
			{
				if (ind == k)
					continue;
				if (changeCount[k] < max)
					max = changeCount[k];
			}
			changeCount[ind] = max + 1;
		}
		
		cout << "Case #" << (i+1) << ": " << (*min_element(changeCount.begin(), changeCount.end())) << endl;
	}
	return 0;
}

