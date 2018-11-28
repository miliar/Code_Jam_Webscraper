#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> a;
int m;
bool fl[50];

bool check(int n)
{
	if (fl[n])
		return false;
	fl[n] = true;
	if (n == 1)
		return true;
	for (int i = 0; i < (int)a.size(); ++i)
	{
		if (a[i] == n)
			return check(i+1);
	}
	return false;
}

void dump()
{
	for (int i = 0; i < (int)a.size(); ++i)
	{
		cout << a[i] << " ";
	}
	cout << endl;
}

int count(int p)
{
	int res = 0;
	a.push_back(m);
	memset(fl, false, sizeof fl);
	if (check(m))
	{
		++res;
		
	}
	a.pop_back();
	for (int i = p; i < m; ++i)
	{
		a.push_back(i);
		res += count(i+1);
		a.pop_back();
	}
	return res;
}
int mem[25] = {
1,
1,
2,
3,
5,
8,
14,
24,
43,
77,
140,
256,
472,
874,
1628,
3045,
5719,
10780,
20388,
38674,
73562,
40265,
68060,
13335,
84884

};
int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		cin >> m;
		cout << "Case #" << test << ": " << mem[m-1] << endl;
	}
	return 0;
}