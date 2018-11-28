#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int n;
multiset<int> m, t, p;

int main()
{
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		cin >> n;
		m.clear();
		for(int i=0; i<n; i++)
		{
			int d;
			cin >> d;
			m.insert(d);
		}

		int ans = 0;
		for(ans=n; ans>=1; ans--)
		{
			bool can = true;
			t = m;
			multiset<int> e;
			while(!t.empty())
			{
				int r = *t.begin();
				for(int i=0; i<ans; i++)
				{
					multiset<int>::iterator it = t.find(r+i);
					if(it == t.end())
					{
						multiset<int>::iterator ii = e.find(r-1);
						if(ii == e.end())
						{
							can = false;
							goto hell;
						}
						else
						{
							e.erase(ii);
							e.insert(r+i-1);
							goto next;
						}
					}
					else
						t.erase(it);
				}
				e.insert(r+ans-1);
				next:;
			}

			hell:;
			if(can)
				break;
		}

		cout << "Case #" << T << ": " << ans << endl;
	}
	return 0;
}

