#include <iostream>
#include <string>
#include <set>
#include <map>

using namespace std;

int test;

void solve()
{
	long long ans = 0;
	string code;
	cin >> code;
	cerr << code << endl;
	set<int> dig;
	
	for (int i = 0; i < (int)code.length(); i++) dig.insert((int)code[i]);
	
	int base = (int)dig.size(); if (base == 1) base = 2;
	for (int i = 0; i < base; i++) if (i != 1) dig.insert(i);
	
	map<char, int> m;
	m[code[0]] = 1;
	
	for (int i = 0; i < (int)code.length(); i++)
	{
		if (m.count(code[i]) == 0) {
			m[code[i]] = *dig.begin();
			dig.erase(dig.begin());
		}
		ans = ans * base + m[code[i]];
	}
	
	++test;
	cout << "Case #" << test << ": " << ans << endl;
}

int main()
{
	int t;
	cin >> t;
	while(t--) solve();
	return 0;
}