#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


string s;

void Load()
{
	cin >> s;
}

void Solve()
{
	s = '0' + s;
	next_permutation(s.begin(), s.end());
	int i;
	i = 0; while (s[i] == '0') i++;
	for (; i < (signed)s.size(); i++) cout << s[i];
	cout << "\n";

}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
