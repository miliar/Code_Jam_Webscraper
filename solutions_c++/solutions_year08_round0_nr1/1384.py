#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)

using namespace std;

vector <string> engine, qu;
int n, m;

int dp[1101][1101];

int memo(int s, int q){
	if (q == m)
		return 0;
	if (engine[s] == qu[q])
		return 1 << 30;
	if (dp[s][q] != -1)
		return dp[s][q];
	int ret = dp[s][q] = 1 << 20;
	int idx = q;
	while (idx < m && engine[s] != qu[idx])
		idx++;
	if (idx == m)
		return dp[s][q] = 0;
	FOR (i, n)
		ret <?= memo(i, idx) + 1;
	return dp[s][q] = ret;
}

int main(){
	int tests;
	ifstream fin("Al.in");
	ofstream fout("Al.out");
	fin >> tests;
	string tmp;
	getline(fin, tmp);
	ffor (test, 1, tests + 1){
		engine.clear();
		qu.clear();
		fin >> n;
		getline(fin, tmp);
		FOR (i, n){
			getline(fin, tmp);
			engine.pb(tmp);
		}
		fin >> m;
		getline(fin, tmp);
		FOR (i, m){
			getline(fin, tmp);
			qu.pb(tmp);
		}
		SET(dp, 255);
		
		int ret = 1 << 30;
		FOR (i, n)
			ret <?= memo(i, 0);
		fout << "Case #" << test <<": " << ret << endl;
		cout << ret << endl;
	}
	system("pause");
	fin.close();
	return 0;
}
