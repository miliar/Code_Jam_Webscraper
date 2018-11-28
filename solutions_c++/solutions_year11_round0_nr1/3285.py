#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#pragma comment(linker, "/STACK:134217728")

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

int dp[105][105][105]; //posO, posB, idx
int marked[105][105][105];


vector<pair<int,int> > B, O;
int maior;
int turn[111], pos[111];
int N;

int a[] = {-1,0,1};

int solve(){
	queue<pair<int,pair<int,int> > >bfs;
	int ret = 0x3f3f3f3f;
	bfs.push(make_pair(0, make_pair(1,1) ) );
	memset(marked,0,sizeof marked);
	memset(dp,0x3f, sizeof dp);
	dp[1][1][0] = 0;
	while(!bfs.empty()){
		int idx = bfs.front().first, i = bfs.front().second.first, j = bfs.front().second.second;
		bfs.pop();
		if(marked[i][j][idx])continue;
		marked[i][j][idx] = 1;
		if(idx == N){
			ret = min(ret, dp[i][j][idx]);
			continue;
		}
		if(turn[idx] && i == pos[idx]){
			for(int jj = 0; jj < 3; jj++)if(j+a[jj] > 0 && j+a[jj] <= maior){
				int kk = 1+dp[i][j][idx];
				if(kk < dp[i][j+a[jj]][idx+1]){
					dp[i][j+a[jj]][idx+1] = kk;
					bfs.push(make_pair(idx+1, make_pair(i, j+a[jj])));
				}
			}
		}else if(!turn[idx] && j == pos[idx]){
			for(int ii = 0; ii < 3; ii++)if(i+a[ii] > 0 && i+a[ii] <= maior){
				int kk = 1+dp[i][j][idx];
				if(kk < dp[i+a[ii]][j][idx+1]){
					dp[i+a[ii]][j][idx+1] = kk;
					bfs.push(make_pair(idx+1, make_pair(i+a[ii], j)));
				}
			}
		}else{
			for(int ii = 0; ii < 3; ii++)if(i+a[ii] > 0 && i+a[ii] <= maior){
				for(int jj = 0; jj < 3; jj++)if(j+a[jj] > 0 && j+a[jj] <= maior && (a[ii] || a[jj]) ){
					int kk = 1+dp[i][j][idx];
					if(kk < dp[i+a[ii]][j+a[jj]][idx]){
						dp[i+a[ii]][j+a[jj]][idx] = kk;
						bfs.push(make_pair(idx, make_pair(i+a[ii], j+a[jj])));
					}
				}
			}
		}
	}
	return ret;
}
/*
int solve(int i, int j, int idx){
	printf("solve(%d, %d, %d)\n", i,j,idx);
	int &ret = dp[i][j][idx];
	if(ret != -1)return ret;
	if(idx == N)return ret = 0;
	ret = 0x3f3f3f3f;
	if(turn[idx] && i== pos[idx]){
		int indice;
		for(int jj = 0; jj < 3; jj++)if(j+a[jj] > 0 && j+a[jj] <= maior){
			int kk = 1+solve(i,j+a[jj],idx+1);
			if(kk < ret){
				indice = jj;
				ret = kk;
			}
		}
	}else if(!turn[idx] && j == pos[idx]){
		int indice;
		for(int ii = 0; ii < 3; ii++)if(i+a[ii] > 0 && i+a[ii] <= maior){
			int kk = (1+solve(i+a[ii],j, idx+1));
			if(kk < ret){
				indice = ii;
				ret = kk;
			}
		}
	}else
		for(int ii = 0; ii < 3; ii++)if(i+a[ii] > 0 && i+a[ii] <= maior){
			for(int jj = 0; jj < 3; jj++)if(j+a[jj] > 0 && j+a[jj] <= maior && (a[ii] || a[jj]) ){
				ret = min(ret, 1+solve(i+a[ii], j+a[jj], idx));
			}
		}
	return ret;
}
*/
int read(){
	scanf("%d", &N);
	char c[5];
	maior = 0;
	for(int i = 0; i < N; i++){
		char c[5];
		scanf("%s %d", c, &pos[i]);
		maior = max(maior, pos[i]);
		if(c[0] == 'B'){
			turn[i] = 1;
		}else turn[i] = 0;
	}
	return 1;
}

void process(){
	printf("%d\n", solve());
}
// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d: ", i);
		process();
		fprintf(stderr, "ok(%d)\n", i);
	}
	return 0;
}
// END CUT HERE 
