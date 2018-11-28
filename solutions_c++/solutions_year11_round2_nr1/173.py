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
#include <list>
#include <ctime>
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
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }


int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);

		vector< string > a(n);
		for(int i = 0; i < n; ++i)
			cin >> a[i];

		vector< int > ones(n), zeros(n);
		vector< double > wp(n);
		vector< double > owp(n);
		vector< double > oowp(n);

		for(int i = 0; i < n; ++i)
			ones[i] = count(a[i].begin(), a[i].end(), '1');
		for(int i = 0; i < n; ++i)
			zeros[i] = count(a[i].begin(), a[i].end(), '0');
		for(int i = 0; i < n; ++i)
			wp[i] = ones[i] / LD(ones[i] + zeros[i]);

		for(int i = 0; i < n; ++i)
		{
			LD sum = 0.0;
			int cnt = n - 1;
			for(int j = 0; j < n; ++j) if(j != i)
			{
				if(a[j][i] == '0')
					sum += (wp[j] * (ones[j] + zeros[j]) - 0) / LD(ones[j] + zeros[j] - 1);
				else if(a[j][i] == '1')
					sum += (wp[j] * (ones[j] + zeros[j]) - 1) / LD(ones[j] + zeros[j] - 1);
				else
					cnt--;
			}
			owp[i] = sum / LD(cnt);
		}
		
		
		for(int i = 0; i < n; ++i)
		{
			LD sum = 0.0;
			int cnt = 0;
			for(int j = 0; j < n; ++j) if(i != j)
				if(a[i][j] != '.')
					sum += owp[j],
					cnt++;
			oowp[i] = sum / LD(cnt);
		}

		cout << "Case #" << z + 1 << ":" << endl;
		cout.precision(9);
		cout.setf(ios::fixed);
		for(int i = 0; i < n; ++i)
			cout << wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25 << endl;
	}
	return 0;
}
#endif

