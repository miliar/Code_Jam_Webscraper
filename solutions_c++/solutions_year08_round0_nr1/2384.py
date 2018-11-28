#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main()
{
	vector<string> searchEngines;
	int n;
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		int s;
		searchEngines.clear();
		cin>>s;
		char sn[150];
		cin.getline(sn, 150);
		for (int j = 0; j < s; ++j)
		{
			cin.getline(sn, 150);
			searchEngines.push_back(string(sn));
		}
		
		int q;
		cin>>q;
		cin.getline(sn, 150);
		vector< vector<int> > qs(q);

		for (int k = 0; k < q; ++k)
		{
			cin.getline(sn, 150);
			string query(sn);

			int ci = 0;
			for (int l = 0; l < s; ++l)
			{
				if (searchEngines[l] == query)
				{
					ci = l;
				}
				
				if (k != 0)
				{
					qs[k].push_back(qs[k-1][l]);
				}
				else
				{
					qs[k].push_back(0);
				}
			}

			for (int l = 0; l < s; ++l)
			{
				if (l != ci && qs[k][l] > qs[k][ci] + 1)
				{
					qs[k][l] = qs[k][ci] + 1;
				}
			}
			qs[k][ci] = 10000;
		}
		int ret = 10000;
		if (q > 0)
		{
			for (int l = 0; l < s; ++l)
			{
				if (qs[q-1][l] < ret)
				{
					ret = qs[q-1][l];
				}
			}
		}
		else
		{
			ret = 0;
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}