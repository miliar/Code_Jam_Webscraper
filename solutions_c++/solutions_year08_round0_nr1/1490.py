#include <iostream> 
#include <string>
#include <map>
#include <set>

using namespace std;

typedef set<string> sset;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int dp[100][1000] = {{0}};
		
		int s;
		cin >> s;		
		
		map<string, int> engines;
		int marks[100];
		string engine;
		
		sset remain, source;
		
		for (int j = 0; j < s; j++)
		{
			while ( getline(cin, engine, '\n'), engine.empty() ) ;
			engines[engine] = j;
			
			source.insert(engine);
		}
		
		remain = source;
		
		int changes = 0;
		
		int q;
		cin >> q;
		for (int j = 0; j < q; j++)
		{
			while ( getline(cin, engine, '\n'), engine.empty() ) ;
			int idx = engines[engine];
			
			remain.erase(engine);
			if (remain.size() == 0)
			{
				changes++;
				remain = source;
				remain.erase(engine);
			}
			
			for (int k = 0; k < idx; k++)
				marks[k]++;
			marks[idx] = 0;
			for (int k = idx + 1; k < s; k++)
				marks[k]++;
		}
		
		cout << "Case #" << i + 1 << ": " << changes << endl;
	}
	return 0;
}
