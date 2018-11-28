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

bool rock[200][200];
int dp[200][200], h, w, mod = 10007;

int memo(int r, int c){
	if (r == h && c == w)
		return 1;
	if (r > h || c > w)
		return 0;
	if (rock[r][c])
		return 0;
	int &ret = dp[r][c];
	if (ret != -1)
		return ret;
	ret = 0;
	ret += memo(r + 2, c + 1);
	ret %= mod;
	ret += memo(r + 1, c + 2);
	ret %= mod;
	return ret;
}

int main(){
	ifstream fin("Ds.in");
	ofstream fout("Ds.out");
	int tests, r, a, b;
	fin >> tests;
	FOR (test, tests){
		fin >> h >> w >> r;
		SET(rock, 0);
		FOR (i, r){
			fin >> a >> b;
			rock[a][b] = true;
		}
		SET(dp, 255);
		int ret = memo(1, 1);
		fout << "Case #" << (test + 1) << ": " << ret << endl;
		cout << "Case #" << (test + 1) << ": " << ret << endl;
	}
	system("pause");
	return 0;
}

