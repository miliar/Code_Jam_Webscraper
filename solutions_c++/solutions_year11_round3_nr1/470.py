//80081TU
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 10E-9;
const double PI = acos(-1.0);



int main () {

	int test;
	cin >> test;
	for(int t=1 ; t<=test ; t++) {
	
		int c, r;
		cin >> r >> c;
		vector<string> mem;
		string str;
		REP(i, r) {
			cin >> str;
			mem.PB(str);
		}

		bool valid = true;
		for(int i=0 ; i<r && valid; i++) {
			for(int j=0 ; j<c && valid ; j++) {
				if(i<r-1 && j<c-1) {
					if(mem[i][j] == '#' && mem[i][j+1] == '#' && mem[i+1][j] == '#' && mem[i+1][j+1] == '#') {
						mem[i][j] = '/';
						mem[i][j+1] = '\\';
						mem[i+1][j] = '\\';
						mem[i+1][j+1] = '/';
					} else if(mem[i][j]=='#') valid = false;
				} else if(mem[i][j] == '#'){
					valid = false;
				}
			}
		}
		printf("Case #%d:\n", t);
		if(!valid) {
			printf("Impossible\n");
		}else {
			REP(i, r) {
				cout << mem[i] << endl;
			}
		}
	
	}

	return 0;
}





