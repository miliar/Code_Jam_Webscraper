#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) ((x) * (x))
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
#define eps 1e-7
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;

char v[10][10];

bool X() {
	f(i, 0, 4) {
		bool d = true;
		f(j, 0, 4) if (v[i][j] != 'X' && v[i][j] != 'T') d = false;
		if (d) return true;
		
		d = true;
		f(j, 0, 4) if (v[j][i] != 'X' && v[j][i] != 'T') d = false;
		if (d) return true;
	}
	bool d = true;
	f(i, 0, 4) if (v[i][i] != 'X' && v[i][i] != 'T') d = false;
	if (d) return true;	
	
	d = true;
	f(i, 0, 4) if (v[i][3-i] != 'X' && v[i][3-i] != 'T') d = false;
	if (d) return true;	
		
	return false;
}
bool O() {
	f(i, 0, 4) {
		bool d = true;
		f(j, 0, 4) if (v[i][j] != 'O' && v[i][j] != 'T') d = false;
		if (d) return true;
		
		d = true;
		f(j, 0, 4) if (v[j][i] != 'O' && v[j][i] != 'T') d = false;
		if (d) return true;
	}
	bool d = true;
	f(i, 0, 4) if (v[i][i] != 'O' && v[i][i] != 'T') d = false;
	if (d) return true;	
	
	d = true;
	f(i, 0, 4) if (v[i][3-i] != 'O' && v[i][3-i] != 'T') d = false;
	if (d) return true;	
		
	return false;
}

bool acabou() {
	f(i,0,4) f(j,0,4) if (v[i][j] == '.') return false;
	return true;
}

int main() {
	int n; cin >> n;
	
	for (int caso = 1; caso <= n; caso++) {
		printf("Case #%d: ", caso);
		for (int i =0;i < 4; i++) scanf(" %s", v[i]);
	
		if (X()) printf("X won\n");
		else if (O())printf("O won\n"); 
		else if (acabou()) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}
