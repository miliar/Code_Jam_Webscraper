#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

int Solution(int test)
{
	int n;
	cin >> n;
	int to = 0, poso = 1, tb = 0, posb = 1;
	for(int i = 0; i < n; ++i)
	{
		char c;
		int p;
		cin >> c >> p;
		if(c == 'O')
		{
			to += abs(p - poso) + 1;
			if(tb >= to)
				to = tb + 1;
			poso = p;
		}
		else
		{
			tb += abs(p - posb) + 1;
			if(to >= tb)
				tb = to + 1;
			posb = p;
        }
	}
	cout << "Case #" << test << ": " << max(to, tb) << endl;
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
		Solution(i);
#ifdef debug
	system("@pause");
#endif
	return 0;
}
