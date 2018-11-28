#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAX_N = 10 * 1000 + 10;

int n, d;
int len[MAX_N];
int dis[MAX_N];
int best[MAX_N];

int main(){
	int test_n;
	cin >> test_n;
	for(int test_i = 1; test_i <= test_n; test_i++){
		memset(best, 0, sizeof best);
		cin >> n;
		FOR(i, n)
			cin >> dis[i] >> len[i];
		cin >> d;
		best[0] = dis[0];
		bool can = false;
		FOR(i, n){
			best[i] = min(best[i], len[i]);
			for(int j = i + 1; j < n && dis[i] + best[i] >= dis[j]; j++)
				best[j] = max(best[j], dis[j] - dis[i]);
			if(dis[i] + best[i] >= d)
				can = true;
			
// 			show(best[0]);
// 			show(best[1]);
// 			show(best[2]);
// 			cerr << endl;
		}
		printf("Case #%d: %s\n", test_i, (can ? "YES" : "NO"));
	}
	return 0;
}
