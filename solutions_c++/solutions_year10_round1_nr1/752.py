#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;
typedef long long ll;
typedef long double ld;

int N;

string b[55];
int di[] = {-1,-1,-1,0,0,1,1,1};
int dj[] = {-1,0,1,-1,1,-1,0,1};

#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	cin >> N;
	for(int ii = 1 ; ii <= N ; ii++ ) {
		//cin>>c>>n;
		//for(int i = 0 ; i < n; i++)
		//	cin>>arr[i];
		int n,K;
		cin >> n >> K;
		for (int i = 0; i < n; ++i) {
			cin >> b[i];
		}
		vector <string> rot(n,string(n,'.'));
		for (int i = 0; i < n; ++i) {
			int curj = 0;
			for (int j = 0; j < n; ++j) {
				if( b[i][n-j-1] != '.' )
					rot[i][curj++] =  b[i][n-j-1] ;
			}
			//cerr << rot[i] << endl;
		}
		//cerr << endl;
		bool p1 = 0, p2 = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if( rot[i][j] != '.' )
				for (int k = 0; k < 8; ++k) {
					char c = rot[i][j];
					int ni = i;
					int nj = j;
					int tt;
					for (tt = 0; tt < K; ++tt) {
						if( ni < 0 || ni >= n || nj < 0 || nj >= n || rot[ni][nj] != c)
							break;
						ni += di[k];
						nj += dj[k];
					}
					if( tt == K ){
						if( c == 'R' )
							p1 = 1;
						else
							p2 = 1;
					}

				}
			}
		}
		printf("Case #%d: ", ii);
		if( p1 && p2 )
			printf("Both");
		if( p1 && !p2 )
			printf("Red");
		if( !p1 && p2 )
			printf("Blue");
		if( !p1 && !p2 )
			printf("Neither");
		printf("\n");
	}
	return 0;
}

