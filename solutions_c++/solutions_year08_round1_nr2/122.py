#include <iostream>
#include <vector>
using namespace std;

struct customer
{
	vector<pair<int, int> > flavours;
	int n;
	int wantMalt;
	
	bool isHappy(int malt[])
	{
		bool happy = false;
		for (int i = 0; i < flavours.size(); i++)
		{
			pair<int, int> f = flavours[i];
			if (malt[f.first] == f.second)
			{
				happy = true;
				break;
			}
		}
		
		return happy;
	}
};

int main()
{
	int cases;
	cin >> cases;
	
	for (int cNum = 1; cNum <= cases; cNum++)
	{
		int nf;
		cin >> nf;
		
		int nc;
		cin >> nc;
		
		customer custs[nc];
		for (int i = 0; i < nc; i++)
		{
			int cnf;
			cin >> cnf;
			custs[i].n = cnf;
			custs[i].wantMalt = -1;
			
			for (int f = 0; f < cnf; f++)
			{
				int f, m;
				cin >> f >> m;
				if (m == 1) custs[i].wantMalt = f;
				custs[i].flavours.push_back(pair<int, int>(f, m));
			}
		}
		
		int malted[nf + 1];
		for (int i = 0; i <= nf; i++) malted[i] = 0;
		
		bool possible = false;
		for (int i = 0; i < nf + 1; i++)
		{
			//See if everyone is now happy
			bool everyoneHappy = true;
			vector<int> unhappy;
			for (int i = 0; i < nc; i++)
			{
				if (!custs[i].isHappy(malted))
				{
					everyoneHappy = false;
					unhappy.push_back(i);
				}
			}
			
			if (everyoneHappy)
			{
				possible = true;
				break;
			}
			
			//People who are unhappy get malted - these people need malted to be happy
			for (int i = 0; i < unhappy.size(); i++)
			{
				int un = unhappy[i];
				int wm = custs[un].wantMalt;
				
				if (wm < 0) continue;
				
				malted[wm] = 1;
			}
		}
		
		
		cout << "Case #" << cNum << ":";
		if (possible)
		{
			for (int i = 0; i < nf; i++)
				cout << " " << malted[i+1];
			cout << endl;
		}
		else
		{
			cout << " IMPOSSIBLE" << endl;
		}
	}
	return 0;
}