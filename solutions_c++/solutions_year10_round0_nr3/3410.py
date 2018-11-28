#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for (int cs = 1; cs <= cases; ++cs)
	{
		int r, k, n;
		cin >> r >> k >> n;
		
		//queue<int> groups;
		int groups[n];
		
		for (int i = 0; i < n; ++i)
		{
			cin >> groups[i];
			
			//groups.push(p);
		}
		
		
		int go[n][2]; //[0] -> next index, [1] -> money
		
		for (int i = 0; i < n; ++i)
		{
			int ni = i;
			int m = 0;
			for (int j = 0; j < n; ++j)
			{
				int nx = groups[ni];
				if (m + nx > k) break;
				
				m += nx;
				ni = (ni + 1) % n;
			}
			
			go[i][0] = ni;
			go[i][1] = m;
		}
		
		/*
		for (int i = 0; i < n; ++i)
		{
			cout << "[" << i << "] " << go[i][1] << " -> " << go[i][0] << endl;
		}
		*/
		
		long long m = 0;
		int s = 0;
		
		for (int i = 0; i < r; ++i)
		{
			m += go[s][1];
			s = go[s][0];
		}
		
		/*
		for (int i = 0; i < r; ++i)
		{
			long long tr = 0;
			/*queue<int> readd;
			
			while (!groups.empty() && (tr + groups.front() <= k))
			{
				int p = groups.front();
				groups.pop();
				readd.push(p);
				tr += p;
			}
			
			m += tr;
			
			while (!readd.empty())
			{
				groups.push(readd.front());
				readd.pop();
			}
		}
		*/
		
		cout << "Case #" << cs << ": " << m << endl;
	}
	
	return 0;
}