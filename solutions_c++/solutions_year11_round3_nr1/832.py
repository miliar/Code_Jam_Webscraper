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
const int MAXN = 1010;

int n, m;
bool pos;
char c[1000][1000];
int main() {
	FIN;
	FOUT;
	int cases;
	cin>>cases;
	for (int cas = 1; cas <= cases; cas++) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> c[i][j];
		pos = true;
		for (int i = 0; i < n; ++i) {
			if (!pos)
				break;
			for (int j = 0; j < m; ++j)
				if (c[i][j] == '#') {
					if (i != n - 1 && j != m - 1 && c[i + 1][j] == '#' && c[i
							+ 1][j + 1] == '#' && c[i][j + 1] == '#') {
						c[i][j] = '/';
						c[i + 1][j] = '\\';
						c[i][j + 1] = '\\';
						c[i + 1][j + 1] = '/';
					} else {
						pos = false;
						break;
					}
				}
		}
		cout<<"Case #"<<cas<<":"<<endl;
		if (pos) {
			FOR(i,0,n) {
				FOR(j,0,m)
					cout << c[i][j];
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	return 0;
}
