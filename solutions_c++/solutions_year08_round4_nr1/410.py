#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#include <fstream>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
typedef long long LL; using namespace std;
int m, uleaf, val;
int ntype[14000];
int change[14000];
const int inf = 1 << 18;
int dp[14000][2];

int memo(int idx, int tt){
	if (idx > uleaf){
		if (tt == ntype[idx])
			return 0;
		return inf;
	}
	if (dp[idx][tt] != -1)
		return dp[idx][tt];
	
	int &ret = dp[idx][tt];
	ret = inf;
	if (tt == 1){
		if (ntype[idx] == 1){ // and
			ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 1));
			if (change[idx]){
				ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 0) + 1);
				ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 1) + 1);
				ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 1) + 1);
			}
		}
		else{
			ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 0));
			ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 1));
			ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 1));			
			if (change[idx])
				ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 1) + 1);
		}
	}
	else{
		if (ntype[idx] == 0){ // or
			ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 0));
			if (change[idx]){
				ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 0) + 1);
				ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 1) + 1);
				ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 0) + 1);
			}
		}
		else{
			ret = min(ret, memo(2 * idx, 1) + memo(2 * idx + 1, 0));
			ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 1));
			ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 0));
			if (change[idx])
				ret = min(ret, memo(2 * idx, 0) + memo(2 * idx + 1, 0) + 1);
		}
	}
	return ret;
}


int main(){
	ifstream fin("Al.in");
	ofstream fout("Al.out");
	int tests, g, c;
	fin >> tests;
	FOR (test, tests){
		fin >> m >> val;
		uleaf = (m - 1) / 2;
		
		FOR (i, (m - 1) / 2)
			fin >> ntype[i + 1] >> change[i + 1];
		
		ffor (i, (m - 1) / 2, m)
			fin >> ntype[i + 1];
			
		SET(dp, 255);
		int ret = memo(1, val);
		if (ret > m)
			fout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	return 0;
}
