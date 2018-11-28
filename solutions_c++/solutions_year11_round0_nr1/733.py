#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
#include <map>
using namespace std;


int main()
{
	int CN;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> CN;
	for (int c = 0; c < CN; ++c)
	{

		int btime = 0, bpos = 1, otime = 0, opos = 1;
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			char r;
			int t;
			cin >> r >> t;
			if (r == 'B')
			{
				btime = max(otime+1, btime+abs(bpos-t)+1);
				bpos = t;
			}
			else
			{
				otime = max(btime+1, otime+abs(opos-t)+1);
				opos = t;
			}
		}
		cout << "Case #" << c+1 << ": " << max(otime, btime) << endl;
	}
}