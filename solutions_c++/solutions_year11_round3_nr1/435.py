#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int T;

int R, C;
char inp[52][52];

void put(int r, int c){
	if (r == R - 1 || c == C - 1) throw(-1);
	if (inp[r][c] != '#') throw(-1);
	if (inp[r+1][c] != '#') throw(-1);
	if (inp[r][c+1] != '#') throw(-1);
	if (inp[r+1][c+1] != '#') throw(-1);
	
	inp[r][c] = '/';
	inp[r][c+1] = '\\';
	inp[r+1][c] = '\\';
	inp[r+1][c+1] = '/';
}

void solve(){
	scanf(" %d%d", &R, &C);
	for (int i=0;i<R;++i){
		scanf(" %s", inp[i]);
	}
	try{
		for (int i=0;i<R;++i){
			for (int j=0;j<C;++j){
				if (inp[i][j] == '#'){
					put(i, j);
				}
			}
		}
		
		for (int i=0;i<R;++i){
			for (int j=0;j<C;++j){
				printf("%c", inp[i][j]);
			}
			printf("\n");
		}
		
	}catch(int e){
		printf("Impossible\n");
	}
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d:\n", tc);
		solve();
	}

	return 0;
}

