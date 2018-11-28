#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
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
#include <ctime> 
#include <queue> 
#include <cstring> 
using namespace std;

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		int N, K;
		scanf("%d%d", &N, &K);
		char maps[N+10][N+10];
		for (int i = 0 ; i < N; ++i) scanf("%s", maps[i]);
		char rmap[N+10][N+10];
		for (int i = 0 ; i < N; ++i)
			for (int j = 0 ; j < N; ++j)
				rmap[j][N-i-1] = maps[i][j];
		int tmap[N+10][N+10], sc[N+10];
		for (int i = 0 ; i < N; ++i){
			sc[i] = N-1;
			for (int j = 0 ; j < N; ++j)
				tmap[i][j] = '.';
		}
		for (int i = N-1; i >= 0 ; --i)
			for (int j = 0 ; j < N; ++j)
				if (rmap[i][j] != '.')
					tmap[sc[j]--][j] = rmap[i][j];
		for (int i = 0 ; i < N; ++i)
			for (int j = 0 ; j < N; ++j)
				rmap[i][j] = tmap[i][j];
				/*
		for (int i = 0 ; i < N; ++i, puts(""))
			for (int j = 0 ; j < N; ++j)
				printf("%c", rmap[i][j]);*/
		bool red = 0, blue = 0;
		for (int i = 0 ; i < N; ++i){
			int cntr = 0, cntb = 0;;
			for (int j = 0 ; j < N; ++j){
				cntr = rmap[i][j] == 'R'?(cntr+1):0;
				cntb = rmap[i][j] == 'B'?(cntb+1):0;
				red |= cntr == K;
				blue |= cntb == K;
			}
		}
		for (int i = 0 ; i < N; ++i){
			int cntr = 0, cntb = 0;;
			for (int j = 0 ; j < N; ++j){
				cntr = rmap[j][i] == 'R'?(cntr+1):0;
				cntb = rmap[j][i] == 'B'?(cntb+1):0;
				red |= cntr == K;
				blue |= cntb == K;
			}
		}
		for (int i = 0 ; i < N; ++i)
			for (int j = 0 ; j < N; ++j){
				int px = i, py = j;
				int cntr = 0, cntb = 0;;
				for (; 0<=px&&px<N&&0<=py&&py<N; px++,py++){
					cntr = rmap[px][py] == 'R'?(cntr+1):0;
					cntb = rmap[px][py] == 'B'?(cntb+1):0;
					red |= cntr == K;
					blue |= cntb == K;
				}
			}
		for (int i = 0 ; i < N; ++i)
			for (int j = 0 ; j < N; ++j){
				int px = i, py = j;
				int cntr = 0, cntb = 0;;
				for (; 0<=px&&px<N&&0<=py&&py<N; px++,py--){
					cntr = rmap[px][py] == 'R'?(cntr+1):0;
					cntb = rmap[px][py] == 'B'?(cntb+1):0;
					red |= cntr == K;
					blue |= cntb == K;
				}
			}
		if (red&&blue) puts("Both");
		else if (red) puts("Red");
		else if (blue) puts("Blue");
		else puts("Neither");
	}
	return 0;
}
