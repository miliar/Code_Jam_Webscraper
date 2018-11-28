#include<iostream>
using namespace std;
#include<algorithm>
#include<queue>
#include<stack>
#include<functional>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<math.h>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>


int h[1000];
int main() {


		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	++T;
	int kase = 0;
	int in;
	while( --T ) {
		int N, L, H;
		cin >> N >> L >> H;
		for(int i = 0 ; i < N ; ++i)
			cin >> h[i];
		int ans = -1;
		for(int i = L ; i <= H ; ++i) {
			bool ok = true;
			for(int j = 0 ; j < N ; ++j) {
				if( i%h[j] == 0 || h[j]%i == 0 );
				else {
					ok = false;
					break;
				}
			}
			if( ok ) {
				ans = i;
				break;
			}

		}
		if( ans == - 1 )
			cout << "Case #" << ++kase << ": NO\n";
		else
			cout << "Case #" << ++kase << ": " << ans << endl;
	}
	return 0;

}