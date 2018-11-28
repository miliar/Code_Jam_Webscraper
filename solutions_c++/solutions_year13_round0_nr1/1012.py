#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>


using namespace std;
const int MODULO = 1000000007; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int,int> Pii;
typedef pair<ll,ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())

bool check(string board[4],char symbol){
	FOR(i,4){
		bool ok = true;
		FOR(j,4){
			if(board[i][j] != symbol && board[i][j] != 'T'){
				ok = false;
				break;
			}
		}
		if(ok) return true;
	}

	FOR(i,4){
		bool ok = true;
		FOR(j,4){
			if(board[j][i] != symbol && board[j][i] != 'T'){
				ok = false;
				break;
			}
		}
		if(ok) return true;
	}

	bool ok = true;
	FOR(i,4){
		if(board[i][i] != symbol && board[i][i] != 'T'){
				ok = false;
				break;
		}
	}
	if(ok) return true;

	ok = true;
	FOR(i,4){
		if(board[i][3-i] != symbol && board[i][3-i] != 'T'){
				ok = false;
				break;
		}
	}
	return ok;
}

string solve(){
	string board[4]; FOR(i,4) cin>>board[i];
	if(check(board,'X')) return "X won";
	if(check(board,'O')) return "O won";

	bool all = true;
	FOR(i,4) FOR(j,4) if(board[i][j] == '.') all = false;

	if(all) return "Draw";
	else return "Game has not completed";
}

int main(){
	int t; cin>>t;
	for(int i = 1; i <= t; i++){
		string ret = solve();
		printf("Case #%d: %s\n",i,ret.c_str());
	}
	return 0;
}
