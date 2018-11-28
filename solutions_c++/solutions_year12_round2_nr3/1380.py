#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>

typedef unsigned long long ull;

using namespace std;

void build_set(map<ull, ull> &parent, set<ull> &s, ull from)
{
	if (from != 0)
	{
		s.insert(from - parent[from]);
		build_set(parent, s, parent[from]);
	}
}

int main()
{
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		cout << "Case #" << test << ":" << endl;
		map<ull, ull> parent;
		parent[0] = 0;
		int n;
		cin >> n;
		ull a;
		bool found = false;
		for (int i = 0; i < n; ++i)
		{
			cin >> a;
			stack<ull> elements;
			for (map<ull, ull>::iterator it = parent.begin(); it != parent.end(); ++it)
			{
				elements.push(it->first);
			}
			for (; !found && !elements.empty(); elements.pop())
			{
				ull x = elements.top();
				if (parent.count(x + a))
				{
					set<ull> first_set, second_set;
					first_set.insert(a);
					build_set(parent, first_set, x);
					build_set(parent, second_set, x + a);
					for (set<ull>::iterator jt = first_set.begin(); jt != first_set.end(); ++jt)
					{
						if (!second_set.count(*jt))
						{
							cout << *jt << ' ';
						}
						second_set.erase(*jt);
					}
					cout << endl;
					for (set<ull>::iterator jt = second_set.begin(); jt != second_set.end(); ++jt)
					{
						cout << *jt << ' ';
					}
					found = true;
				}
				parent[x + a] = x;
			}
		}
		if (!found)
		{
			cout << "Impossible";
		}
		cout << endl;
	}
	return 0;
}
