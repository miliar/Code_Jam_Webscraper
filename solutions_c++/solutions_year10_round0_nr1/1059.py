#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <set>

using namespace std;

typedef unsigned long long LL;
typedef pair<int, int> PII;
#define lowbit(a) ((a) & (-a))
#define two(a) (1 << (a))
vector<PII> g;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		int n, k;
		cin >> n >> k;
		cout << "Case #" << i << ": ";
		n = two(n);
		if(k % n == n - 1)
			cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	return 0;
}