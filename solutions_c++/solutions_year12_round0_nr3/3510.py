#include <iostream>
#include <vector>
#include <sstream>
#include <set>

using namespace std;

void solve()
{
	string file = "C-small-attempt0";
	freopen((file + ".in").c_str(), "rt", stdin);
	freopen((file + ".out").c_str(), "wt", stdout);

	int T, t, A, B;
	string line;
	cin >> T >> ws;
	t = 1;
	while(T--)
	{
		cout << "Case #" << t++ << ": ";
		cin >> A >> B >> ws;
		set<int> used;
		int y = 0;
		for(int i = A; i < B; i++)
		{
			if(!used.count(i));
			{
				used.insert(i);
				stringstream ss;
				ss << i;
				string s = ss.str();

				set<int> dis;

				for(int j = 1; j < s.length(); j++)
				{
					string r = s.substr(j) + s.substr(0, j);
					int x = atoi(r.c_str());
					if(x >= A && x <= B && !used.count(x)) 
					{
							used.insert(x);
							dis.insert(x);
					}
				}
				int n = dis.size();
				y += n * (n + 1) / 2;
			}
		}
		cout << y << endl;
	}
}