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

int dp[10][1 << 10], n, m;
string room[10];

bool broken(int idx, int mask){
	FOR (i, n)
		if (mask & (1 << i))
			if (room[idx][i] == 'x')
				return true;
	return false;
}

bool attack(int mask1, int mask2){
	FOR (i, n){
		if (i > 0){
			if (mask1 & (1 << i))
				if (mask1 & (1 << (i - 1)))
					return true;
			if (mask2 & (1 << i))
				if (mask2 & (1 << (i - 1)))
					return true;
		}
	}
	FOR (i, n){
		if (i > 0)
			if (mask1 & (1 << i))
				if (mask2 & (1 << (i - 1)))
					return true;
		if (i < n - 1)
			if (mask1 & (1 << i))
				if (mask2 & (1 << (i + 1)))
					return true;			
	}
	return false;
}

int memo(int idx, int mask){
	if (idx == m)
		return 0;
	int &ret = dp[idx][mask];
	if (ret != -1)
		return ret;
	ret = 0;
	int cnt = 0;
	FOR (i, n)
		if (mask & (1 << i))
			cnt++;

	if (broken(idx, mask))
		cnt = 0;
	FOR (i, 1 << n)
		if (!attack(mask, i))
			ret >?= (cnt + memo(idx + 1, i));
	return ret;
}

int main(){
	ifstream fin("Cs.in");
	ofstream fout("Cs.out");
	int tests;
	fin >> tests;
	FOR (test, tests){
		fin >> m >> n;
		FOR (i, m)
			fin >> room[i];
		int ret = 0;
		SET(dp, 255);
		FOR (i, 1 << n)
			ret >?= memo(0, i);
		fout << "Case #" << (test + 1) << ": " << ret << endl;
		cout << "Case #" << (test + 1) << ": " << ret << endl;
		
	}
	system("pause");
	return 0;
}
