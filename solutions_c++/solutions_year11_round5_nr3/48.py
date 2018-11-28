//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 100 + 10;

const char move[3][3] = {
	{'\\', '|', '/'},
	{'-' , '#', '-'},
	{'/' , '|', '\\'}
};

int r, c;
char tab[MAX_N][MAX_N];
bool match[MAX_N][MAX_N];

void dfs(int i, int j){
	match[i][j] = true;
	for(int dx = -1; dx <= 1; dx++)
		for(int dy = -1; dy <= 1; dy++){
			if(dx == 0 && dy == 0)
				continue;
			int newi = (i + dx + r) % r;
			int newj = (j + dy + c) % c;
			int nexti = (i + dx + dx + r) % r;
			int nextj = (j + dy + dy + c) % c;
			if(tab[newi][newj] == move[dx + 1][dy + 1] && !match[nexti][nextj])
				dfs(nexti, nextj);
		}
}

int main(){
	int testN;
	cin >> testN;
	FOR(testI, testN){
		scanf("%d %d", &r, &c);
		memset(match, 0, sizeof match);
		FOR(i, r)
			scanf(" %s", tab[i]);
		
		bool bad = false;
		for(int i = 0; i < r && !bad; i++)
			for(int j = 0; j < c && !bad; j++){
				if(match[i][j])
					continue;
				int sum = 0;
				for(int dx = -1; dx <= 1; dx++)
					for(int dy = -1; dy <= 1; dy++){
						if(dx == 0 && dy == 0)
							continue;
						int newi = (i + dx + r) % r;
						int newj = (j + dy + c) % c;
						if(tab[newi][newj] == move[dx + 1][dy + 1])
							sum++;
					}
				if(sum == 0)
					bad = true;
				if(sum == 1){
					for(int dx = -1; dx <= 1; dx++)
					for(int dy = -1; dy <= 1; dy++){
						if(dx == 0 && dy == 0)
							continue;
						int newi = (i + dx + r) % r;
						int newj = (j + dy + c) % c;
						if(tab[newi][newj] == move[dx + 1][dy + 1]){
							tab[newi][newj] = '#';
							break;
						}
						match[i][j] = true;
					}
				}
			}
		if(bad){
			printf("Case #%d: 0\n", testI + 1);
			continue;
		}
		int ans = 1;
		FOR(i, r)
			FOR(j, c)
				if(!match[i][j]){
					dfs(i, j);
					ans = (ans * 2) % 1000003;
				}
		printf("Case #%d: %d\n", testI + 1, ans);
	}
	return 0;
}
