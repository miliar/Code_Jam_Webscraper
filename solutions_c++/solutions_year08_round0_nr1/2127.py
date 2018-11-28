#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main ()
{
	int cases, e, q, sw, max, count, pq;
	string s;
	cin>>cases;
	for (int i = 1; i <= cases; ++i)
	{
		vector<string> engines;
		cin>>e;
		getline(cin, s);
		for (int j = 0; j < e; ++j)
		{
			getline(cin, s);
			engines.push_back(s);
		}
		cin>>q;
		getline(cin, s);
		vector<string> queries;
		for (int j = 0; j < q; ++j)
		{
			getline(cin, s);
			queries.push_back(s);
		}
		sw = 0;
		pq = 0;
		while (pq < q)
		{
			max = 0; 
			for (int i = 0; i < e; ++i)
			{
				count = 0;
				for (int j = pq; j < q; ++j)
				{
					if (queries[j] != engines[i]) ++count;
					else break;
				}
				if (count > max) 
				{
					max = count;
				}
			}
			pq += max;
			if (pq < q)++sw;
		}
		cout<<"Case #"<<i<<": "<<sw<<endl;
	}
	return 0;
}
