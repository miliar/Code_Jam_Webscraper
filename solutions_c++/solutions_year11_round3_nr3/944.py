#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int N, L, H;
int f[101];
int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d %d %d", &N, &L, &H);
		for(int i = 0; i < N; i++)
			scanf("%d", &f[i]);
		int ans, i;
		for(ans = L; ans <= H; ans++){
			for(i = 0; i < N; i++){
				if((ans % f[i] != 0) && (f[i] % ans != 0)){
					break;
				}
			}
			if(i == N)
				break;
		}
		cout << "Case #" << t << ": ";
		if(ans <= H)
			cout << ans;
		else
			cout << "NO";
		if(t < T) cout << endl;

	}

	return 0;
}


