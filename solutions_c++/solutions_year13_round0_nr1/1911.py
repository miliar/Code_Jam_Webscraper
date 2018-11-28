#define _HAS_CPP0X 0
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
template<class T> T Abs(T x) { return x < 0 ? -x : x; }
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


char d[5][5];

bool eqq(char c, char dc){
	return c == dc || dc == 'T';
}
bool hasWon(char c){
	bool ok_diag1 = true;
	bool ok_diag2 = true;
	for (int i = 0; i < 4; i++){
		bool ok_hor = 1;
		bool ok_ver = 1;
		if (!eqq(c, d[i][i])){
			ok_diag1 = false;
		}
		if (!eqq(c, d[i][3 - i])){
			ok_diag2 = false;
		}
		for (int j = 0; j < 4; j++){
			if (!eqq(c, d[i][j])){
				ok_hor = 0;
			}
			if (!eqq(c, d[j][i])){
				ok_ver = 0;
			}			
		}
		if (ok_hor || ok_ver){
			return true;
		}
	}
	return ok_diag1 || ok_diag2;	
}
bool hasEmpty(){
	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 4; j++){
			if (d[i][j] == '.'){
				return true;
			}
		}
	}
	return false;
}
void Go(){
	for (int i = 0; i < 5; i++){
		gets(d[i]);
	}	
	if (hasWon('X')){
		printf("X won");
	}
	else if (hasWon('O')){
		printf("O won");
	}
	else if (hasEmpty()){
		printf("Game has not completed");
	}
	else{
		printf("Draw");
	}
}

int main(){
	const string task = "A";
	const string folder = "gcj/2013/qual";
	const int attempt = -1;
	const bool dbg = 0;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		if (attempt < 0)
			ss << folder << '/' << task << "-large";
		else
			ss << folder << '/' << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	static char tt[128];
	gets(tt);
	int t;
	sscanf(tt, "%d", &t);
	FOR(i, t){		
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}