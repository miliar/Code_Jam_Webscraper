#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <fstream>
#include <map>
using namespace std;

main()
{	
	// read the cycles from prebuilt file
	vector <int> cycles[2000001];
	ifstream fin("data.txt");
	int x;
	while (fin >> x)
	{
		int i = x;
		do
		{
			cycles[i].push_back(x);
			fin >> x;
			if (x == -1) break;
		} while(true);
	}
	
	int t;
	cin >> t;
	
	for (int iIndex = 1; iIndex <= t; iIndex++)
	{
		long long ans = 0;
		int a,b;
		cin >> a >> b;
		
		int done[2000001];
		memset(done,0,sizeof(done));
	
		for (int i = a; i <= b; i++)
		{
			if (done[i]) continue;
			
			int cnt = 0;
			for (int j = 0; j < cycles[i].size(); j++)
			{
				if (cycles[i][j] >= a && cycles[i][j] <= b)
				{
					cnt++;
					done[cycles[i][j]] = 1;
				}
			}
			ans += (cnt*(cnt-1))/2;
		}
		
		cout << "Case #" << iIndex << ": " << ans << "\n";
	}
}				