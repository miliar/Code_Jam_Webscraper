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
const double EPS = 1e-9;
const double PI = acos(-1.0);

char mem[101][101];
int match[101];
int wp[101];
double owp[101];
double oowp[101];


int main(void) {

	int test, cases =0;
	cin >> test;
	while(test--) {
		cases ++;		
		int n;
		cin >> n;
		REP(i,n) REP(j,n)cin >> mem[i][j];

		for(int i=0 ; i<n ; i++) {
			match[i] = 0;
			for(int j=0 ; j<n ; j++) if(mem[i][j] != '.')match[i]++;
			wp[i] = 0.;
			for(int j=0 ; j<n ; j++) if(mem[i][j] == '1' ) wp[i]++;
			
//			cout << i << " " << wp[i]/(double) match[i]<< endl;
		}

		for(int i=0 ; i<n ; i++) {
			owp[i] = 0.;
			for(int j = 0 ; j < n ; j++) if(mem[i][j] != '.'){
				if(mem[j][i] == '1') owp[i] += (wp[j]-1)/((double)match[j]-1);
				else owp[i] += (wp[j])/((double)match[j]-1);
			}
			owp[i] /= ((double)match[i]);
//			cout << i << " " << owp[i] << endl;
		}

		for(int i=0 ; i<n ; i++) {
			oowp[i] = 0.;
			for(int j = 0 ; j < n ; j++) if(mem[i][j] != '.'){
				oowp[i] += owp[j];
			}
			oowp[i] /= ((double)match[i]);
//			cout << i << " " << oowp[i] << endl;
		}

		printf("Case #%d:\n", cases);
		REP(i,n) {
//			cout << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
			printf("%.12lf\n", .25*((double)wp[i])/((double)match[i])+.5*owp[i]+.25*oowp[i]);
		}

	}


	return 0;
}
