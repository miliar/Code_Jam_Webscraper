#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int n; cin >> n;
    for (int x = 1; x <= n; ++x)
    {
	string dummy;
	int s; cin >> s; getline(cin, dummy);
	map<string, int> sm;
	for (int i = 0; i < s; ++i)
	{
	    string ss;
	    getline(cin, ss);
	    sm.insert(make_pair(ss, i));
	}
	int q; cin >> q; getline(cin, dummy);
	int y = 0;
	vector<bool> v(s);
	for (int i = 0; i < s; ++i)
	    v[i] = false;
	int u = 0;
	for (int j = 0; j < q; ++j)
	{
	    string qq;
	    getline(cin, qq);
	    typeof(sm.find(qq)) p = sm.find(qq);
	    if (p != sm.end() && !v[p->second]) {
		if (u == s - 1) {
		    for (int i = 0; i < s; ++i)
			v[i] = false;
		    u = 0;
		    ++y;
		}
		v[p->second] = true;
		++u;
	    }
	}
	cout << "Case #" << x << ": " << y << endl;
    }
    return 0;
}
