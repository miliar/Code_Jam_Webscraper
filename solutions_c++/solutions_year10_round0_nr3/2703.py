#include <queue>
#include <iostream>

using namespace std;

int main()
{
	int tc;
	int r,k, n;

	cin >> tc;
	for(int t=1; t<=tc; t++)
	{
		cin >> r >> k >> n;
		int ans = 0;
		int seat;
		queue < int > g;
		queue < int > temp;
		int gSize;
		for(int i=0; i<n; i++)
		{
			cin >> gSize;
			g.push(gSize);
		}
		while( r-- )
		{
			
			seat = k;
			while( !g.empty() && seat - g.front() >= 0)
			{
				seat -= g.front();
				ans += g.front();
				temp.push(g.front());
				g.pop();
			}
			while( !temp.empty() )
			{
				g.push(temp.front());
				temp.pop();
			}
		}
		cout << "Case #" << t << ": "<< ans << endl;
		
	}
	return 0;
}
