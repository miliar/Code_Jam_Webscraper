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
bool mp[110][110],nxt[110][110];
#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	cin >> N;
	for(int ii = 1 ; ii <= N ; ii++ ) {
		//cin>>c>>n;
		//for(int i = 0 ; i < n; i++)
		//	cin>>arr[i];
		int r;
		cin >> r;
		memset(mp,0,sizeof mp);
		for (int i = 0; i < r; ++i) {
			int x1,x2,y1,y2;
			cin >> x1>>y1>>x2>>y2;
			for (int i = y1; i <= y2; ++i) {
				for (int j = x1; j <= x2; ++j) {
					mp[i][j] = 1;
				}
			}
		}
		bool still = 1;
		int cnt = 0;
		while( still ){
			cnt++;
			memset(nxt,0,sizeof nxt);
			still = 0;
			for (int i = 0; i < 110; ++i) {
				for (int j = 0; j < 110; ++j) {
					if( mp[i][j] && !mp[i-1][j] && !mp[i][j-1] )
						nxt[i][j] = 0;
					else if( !mp[i][j] && mp[i-1][j] && mp[i][j-1] )
						nxt[i][j] = 1;
					else
						nxt[i][j] = mp[i][j];
					if( nxt[i][j] )
						still = 1;
				}
			}
			memcpy(mp,nxt,sizeof nxt);
		}
		printf("Case #%d: ", ii);
		printf("%d",cnt);
		printf("\n");
	}
	return 0;
}
