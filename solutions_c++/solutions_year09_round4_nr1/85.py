#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <bitset>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define dbg(x) {cerr << #x << " " << x << endl;}
#define dbgv(x) {cout << "{ "; for(int i = 0; i < (x).size(); ++i) cout << " " << (x)[i]; cout << " }\n";}
const double eps = 1e-9;
const LD pi = 3.1415926535897932384626433832795;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);
		vector<string> a(n);
		vector<int> b(n);
		for(int i = 0; i < n; ++i)
		{
			cin >> a[i];
			//reverse(a[i].begin(), a[i].end());
			for(int j = 0; j < a[i].length(); ++j)
			{
				if(a[i][j] == '1')
				{
					b[i] = j;
				}
			}
			//cout << b[i] << endl;
		}
		int ans = 0;
		for(int i = 0; i < n; ++i)
		{
			for(int j = i; j < n; ++j)
				if(b[j] <= i)
				{
					for(int k = j; k > i; --k)
						swap(b[k], b[k - 1]),
						ans++;
					break;
				}
		}
		cout << "Case #" << z + 1 << ": " << ans << endl;
	}

	return 0;
}