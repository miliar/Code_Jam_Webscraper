#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;
string s, t;

void Load()
{
	cin >> s;
}

void Solve(int Test)
{
	int i;
	t = s;
	cout << "Case #" << Test << ": ";
	if (next_permutation(t.begin(), t.end()) == 0)
	{
		t += '0';
		sort(t.begin(), t.end());
		int i;
		int zeroes = 0;
		for (i = 0; i < t.size(); i++)
		{
			if (t[i] == '0')
				zeroes++;
			else break;
		}
		cout << t[i] << string(zeroes, '0') << t.substr(i + 1, t.size() - i + 1) << "\n";
	}
	else
	{
		cout << t << "\n";
	}
}


#define file "b"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	nextLine();
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}