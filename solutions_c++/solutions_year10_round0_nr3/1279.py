#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(),a.end()
#define _(a,b) memset((a),b,sizeof(a))

typedef unsigned long long ull;
typedef long long lint;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-9;

int a[1005];
ull w[1005];
int next[1005];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t,T;
	int i,j;
	int R,k,n;

	cin >> T;
	for (t=1; t<=T; t++)
	{
		cin >> R >> k >> n;
		for (i=0; i<n; i++)
			cin >> a[i];
		_(next,0);
		_(w,0);
		for (i=0; i<n; i++)
		{
			ull sum = a[i];
			next[i] = (i + 1) % n;
			j = next[i];
			while (j!=i && sum + a[j] <= k)
			{
				sum += a[j];
				j = (j + 1) % n;
			}
			w[i] = sum;
			next[i] = j;
		}
		
		j = 0;
		ull ans = 0;
		for (i=0; i<R; i++)
		{
			assert(w[j]>0);
			assert(j<n && j>=0);
			ans += w[j];
			j = next[j];
		}
		cout << "Case #" << t << ": " << ans;
		if (t!=T) cout << endl;
	}

	return 0;
}