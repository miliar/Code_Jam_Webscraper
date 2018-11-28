//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned char UCHAR;
using namespace std;

const int N_MAX = 1010;
int a[N_MAX];

int main()
{

#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tst;
	cin >> tst;
	for (int t = 1; t <= tst; ++t)
	{
		int n;
		cin >> n;
		int s = 0, x = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
			s += a[i];
			x ^= a[i];
		}

		cout << "Case #" << t << ": ";
		if (x == 0)
			cout << s - *min_element(a, a + n);
		else
			cout << "NO";
		cout << '\n';
	}

	return 0;
}
