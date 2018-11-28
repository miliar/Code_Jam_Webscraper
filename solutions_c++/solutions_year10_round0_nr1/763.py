#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;



int main()
{
	/*int start = 0;
	for(int i = 0; i < 100; ++i)
	{
		cout << bitset<15>(start) << endl;
		int p = 0;
		while(start & (1 << p))
			p++;
		start ^= ((1 << (p + 1)) - 1);
	}
	return 0;
	*/
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for(int z = 0; z < t; ++z)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		int need = (1 << n) - 1;
		
		if(k == need || (k + 1) % (need + 1) == 0)
			printf("Case #%d: ON\n", z + 1);
		else
			printf("Case #%d: OFF\n", z + 1);

		
	}
	return 0;
}
#endif