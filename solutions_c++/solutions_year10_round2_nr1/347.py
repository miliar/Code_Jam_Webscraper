#include <string>
#include <string.h>
#include <iostream>
#include <set>
using namespace std;

set<string> s;
string dir[128];
int n, m;
int cnt;

void Proceed(string dir, bool calc)
{
	string d = "";
	int L = 0;
	int R = 1;
	while(L < dir.length())
	{
		while(R < dir.length() && dir[R] != '/')
			R++;
		d += dir.substr(L, R - L);
		if(calc)
		{
			if(s.find(d) == s.end())
				cnt++;
		}
		s.insert(d);
		L = R;
		R++;
	}
}

void Solve()
{
	s.clear();
	cnt = 0;
	cin >> n >> m;
	for(int i = 0; i < n; i++)
	{
		string tmp;
		cin >> tmp;
		Proceed(tmp, false);
	}
	for(int i = 0; i < m; i++)
	{
		string tmp;
		cin >> tmp;
		Proceed(tmp, true);
	}
	cout << cnt << endl;
}

int main()
{
	freopen("d:\\input.in", "r", stdin);
	freopen("d:\\output.out", "w", stdout);
	int T;
	cin >> T;
	for(int rr = 1; rr <= T; rr++)
	{
		cout << "Case #" << rr << ": ";
		Solve();
	}
	return 0;
}