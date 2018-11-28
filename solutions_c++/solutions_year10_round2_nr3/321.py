#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

#define big long long

const int MOD = 100003;
const int MAX = 501;
big comb[MAX][MAX];
void calcCombinations(){
	comb[0][0] = 1;
    for (int i = 1; i <= MAX; i++) {
		comb[i][0] = 1;comb[i][i] = 1;
        for (int j = 1; j < i; j++)
			comb[i][j] = (comb[i-1][j] + comb[i-1][j-1])%MOD;
    }
}

big table[MAX][MAX];
big get(int n, int r){
	if(r == 1)return 1;
	if(table[n][r] != -1)return table[n][r];

	big res = 0;
	for(int rr = r-1 ; rr >= 1 ; rr--){
		int d = n-r-1;
		int c = r-rr-1;
		big choose = comb[d][c];
		big current = get(r, rr);
		current = (choose*current)%MOD;
		res = (res+current)%MOD;
	}
	return table[n][r] = res;
}

int main(){

	calcCombinations();

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	memset(table, -1, sizeof table);
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		int N; cin >> N;
		big res = 0;
		for(int i = 1 ; i < N ; i++)
			res = (res+get(N, i))%MOD;
		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}
