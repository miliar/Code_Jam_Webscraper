#include <iostream>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FIN  freopen("file.in" , "r" , stdin)
#define FOUT freopen("file.out" , "w" , stdout)
#define OUT(x)  cout<< #x << "  : " << x <<endl
#define ERR(x)  cout<<"#error: "<< x ; while(1)
#define read(x) scanf("%d",&x)
#define reads(s) scanf("%s",s)
#define write(x) printf("%d",x)
#define writeln(x) printf("%d\n",x);
#define writes(s) printf("%s",s)

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define SZ(x) (int)((x).size())
#define CLR(a) memset((a),0,sizeof (a));
#define ALL(c) (c).begin(), (c).end()
#define ITER(c) __typeof((c).begin())
#define HAS(c, e) (find(ALL(c), (e)) != (c).end())
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define PB(e) push_back(e)
#define MP(a, b) make_pair(a, b)

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef set<int> sint;
typedef pair<int, int> pint;

const double PI = acos(-1.0);
const double EPS = 1e-8;
const int INF = -1u >> 2;
const int MAXN = 1100000;

LL pos, a[MAXN], sum[MAXN], total;
LL dL, L, t, n, c;
bool there;
int main() {
	FIN;
	FOUT;
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		cin >> t >> L >> n >> c;
		for (int i = 0; i < c; ++i)
			cin >> sum[i];
		for (int i = 0; i < n; ++i) {
			a[i] = sum[i % c];
		}
		for (int i = 1; i < n; ++i)
			a[i] += a[i - 1];
		total = a[n - 1] * 2;
		vector<int> s;
		s.clear();

		there = false;
		if (a[0]*2>L) {
			pos = 0;
			there = true;
		} else
		for (int i = 0; i < n - 1; ++i) {
			if (a[i] * 2 <= L && a[i + 1] * 2 > L) {
				there = true;
				pos = i + 1;
				break;
			}
		}
		cout << "Case #" << cas << ": ";
		if (!there) {
			cout << total << endl;
		} else {
			if (pos==0) {
				dL = L;
			} else
			dL = L - a[pos - 1] * 2;
			s.push_back(sum[pos % c] - dL / 2);
			for (int i = pos + 1; i < n; ++i)
				s.push_back(sum[i % c]);
			sort(s.begin(), s.end());
			n = n - pos;
			//			nth_element(s.begin(), s.end()-t, s.end());
			for (int i = n - 1; i >= n - t; --i)
				total = total - s.at(i);
			cout << total << endl;
		}
	}
	return 0;
}
