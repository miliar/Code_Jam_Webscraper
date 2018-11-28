#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////


int smat[8][8];
int lmat[8][8];

int N, M;

void solve(int tid) {
	vector<int> choose(N, 0);
	for (int i=0; i<M; ++i) choose[i] = 1;
	sort(choose.begin(), choose.end() );

	
	do {
		vector<int> seq;
		for (int i=0; i<N; ++i) if (choose[i]){
			seq.push_back(i);
		}
		do {
			//check
			bool flag = true;
			for (int i=0; i<M && flag; ++i) {
				for (int j=i+1; j<M && flag; ++j) {
					int x = seq[i];
					int y = seq[j];
					if (lmat[x][y] != smat[i][j]) {
						flag = false;
						break;
					}
				}
			}
			if (flag ) {
				printf("Case #%d: YES\n", tid);
				return;
			}
		}
		while(std::next_permutation(seq.begin(), seq.end() ));
	}
	while(std::next_permutation(choose.begin(), choose.end()) );

	
	
    printf("Case #%d: NO\n", tid);

}

int main() {
	freopen("c:/input.in", "r", stdin); freopen("c:/output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		memset(lmat, 0, sizeof lmat);
		memset(smat, 0, sizeof smat);
		scanf("%d", &N);
		for (int i=0; i<N-1; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			x--;
			y--;
			lmat[x][y] = lmat[y][x] = 1;
		}
		scanf("%d", &M);
		for (int i=0; i<M-1; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			x--;
			y--;
			smat[x][y] = smat[y][x] = 1;
		}
		solve(tid);
	}
	return 0;
}