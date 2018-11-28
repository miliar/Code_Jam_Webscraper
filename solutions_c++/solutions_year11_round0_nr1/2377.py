#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n;
		cin >> n;
		int ans = 0;
		int oc = 1, bc = 1;
		char color, cur = 'q';
		int butt;
		int extraO = 0;
		int extraB = 0;
		for(int i = 0; i < n; ++i)
		{
			cin >> color >> butt;
			int t;
			if(color == 'O')
			{
				if(cur != color)
				{
					if(abs(oc - butt) - extraO > 0)
					{
						t = abs(oc - butt) - extraO;
						extraB = t + 1;
					}
					else
					{
						t = 0;
						extraB = 1;
					}
					extraO = 0;
					cur = color;
				}
				else
				{
					t = abs(oc - butt);
					extraB += t + 1;
				}
				oc = butt;
			}
			else
			{
				if(cur != color)
				{
					if(abs(bc - butt) - extraB > 0)
					{
						t = abs(bc - butt) - extraB;
						extraO = t + 1;
					}
					else
					{
						t = 0;
						extraO = 1;
					}
					extraB = 0;
					cur = color;
				}
				else
				{
					t = abs(bc - butt);
					extraO += t + 1;
				}
				bc = butt;
			}
			ans += 1 + t;
		}
		
		cout << "Case #" << Case + 1 <<": " << ans << endl;
	}

	return 0;
}
