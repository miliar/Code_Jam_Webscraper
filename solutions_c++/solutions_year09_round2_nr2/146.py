#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-9; 
const double PI = acos(-1.0);

void Go()
{
	string s;
	cin >> s;
	if (!next_permutation(s.begin(), s.end()))
	{
		int p = s.find_first_not_of('0');
		if (p == -1)
		{
			s.insert(s.begin() + 1, '0');
		}
		else
		{
			swap(s[0], s[p]);
			s.insert(s.begin() + 1, '0');
			sort(s.begin() + 1, s.end());
		}
	}
	cout << s;
}

void main()
{
	const string A = "B";
	//const string B = "small";
	const string B = "large";
#ifndef _DEBUG
	freopen((A + "-" + B + ".in").c_str(), "r", stdin);
	freopen((A + "-" + B + ".out").c_str(), "w", stdout);
#endif
	
	int nn;
	cin >> nn;
	for (int jj = 1; jj <= nn; jj++)
	{
		cout << "Case #" << jj << ": ";
		Go();
		cout << endl;
	}

}
