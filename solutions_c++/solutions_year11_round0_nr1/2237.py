#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

#define ABS(x) (((x)>0)?(x):(-(x)))
#define SGN(x) ((x)/ABS(x))

int cx[2];
queue<int> bt[2];
queue<bool> tr;

int main()
{
	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		cx[0] = cx[1] = 1;
		int n;
		cin >> n;
		for(int i=0; i<n; i++)
		{
			char c;
			int d;
			cin >> c >> d;
			tr.push(c == 'O');
			bt[tr.back()].push(d);
		}
		int ans = 0;
		for(; tr.size(); ans++)
		{
			bool p = false;
			for(int j=0; j<2; j++)
				if(cx[j] != bt[j].front())
					cx[j] += SGN(bt[j].front() - cx[j]);
				else if(tr.front() == j)
					p = true;
			if(p)
			{
				bt[tr.front()].pop();
				tr.pop();
			}
		}
		cout << "Case #" << T << ": " << ans << endl;
	}
	return 0;
}

