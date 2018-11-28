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
const big INF = 1000000000000000ll;

int N, miss[1<<10];
big costs[10][1<<10];

big table[10][10][1<<10];
big get(int r, int b, int i){

	int segmentLength = (1<<(N-r));

	if(segmentLength == 1)
		return b >= miss[i] ? 0 : INF ;
	if(table[r][b][i] != -1)return table[r][b][i];

	//buy
	big best1 = costs[r][i];
	best1 += get(r+1, b+1, 2*i);
	best1 += get(r+1, b+1, 2*i+1);

	//don't buy
	big best2 = 0;
	best2 += get(r+1, b, 2*i);
	best2 += get(r+1, b, 2*i+1);

	big best = best1 <? best2;

	return table[r][b][i] = best;
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> N;
		for(int i = 0 ; i < (1<<N);  i++){
			cin >> miss[i];
			miss[i] = N-miss[i];
		}
		for(int i = N-1 ; i >= 0 ; i--)
			for(int j = 0 ; j < (1<<i) ; j++)
				cin >> costs[i][j];

		memset(table, -1, sizeof table);
		cout << "Case #" << t+1 << ": " << get(0, 0, 0) << endl;
	}

	return 0;
}
