#include <iostream>
#include <list>
#include <fstream>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <deque>
#include <map>
#include <complex>
#include <ctime>
#include <cctype>

using namespace std;

#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)

typedef long long ll;
typedef long double ld;
typedef complex<ld> vec;

typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pb push_back
#define mp make_pair

#define MAXN 5
char A[MAXN][MAXN];

bool is(char a, char b){
	return (a==b) || a=='T' || b=='T';
}

int main(){
	int TEST;
	cin >> TEST;
	
	const int R = 4;
	const int C = 4;
	
	FOR(test,TEST){
		memset(A,0,sizeof(A));
		FOR(i,R) cin >> A[i];
		
		bool seendot = false;
		FOR(i,R) FOR(j,C)
			if (A[i][j] == '.') seendot = true;
		
		bool xwin = false;
		bool owin = false;
		
		FOR(i,R){
			if (is(A[i][0],'X') && is(A[i][1],'X')
				&& is(A[i][2],'X') && is(A[i][3],'X')) xwin = true;
			if (is(A[i][0],'O') && is(A[i][1],'O')
				&& is(A[i][2],'O') && is(A[i][3],'O')) owin = true;
		}
		
		FOR(j,C){
			if (is(A[0][j],'X') && is(A[1][j],'X')
				&& is(A[2][j],'X') && is(A[3][j],'X')) xwin = true;
			if (is(A[0][j],'O') && is(A[1][j],'O')
				&& is(A[2][j],'O') && is(A[3][j],'O')) owin = true;
		}
		
		if (is(A[0][0],'X') && is(A[1][1],'X') && is(A[2][2],'X') && is(A[3][3],'X'))
			xwin = true;
		if (is(A[0][0],'O') && is(A[1][1],'O') && is(A[2][2],'O') && is(A[3][3],'O'))
			owin = true;
			
		if (is(A[0][3],'X') && is(A[1][2],'X') && is(A[2][1],'X') && is(A[3][0],'X'))
			xwin = true;
		if (is(A[0][3],'O') && is(A[1][2],'O') && is(A[2][1],'O') && is(A[3][0],'O'))
			owin = true;
			
		cout << "Case #" << (test+1) <<": ";
		if (owin) cout << "O won" << endl;
		else if (xwin) cout << "X won" << endl;
		else if (seendot) cout << "Game has not completed" << endl;
		else cout << "Draw" << endl;
	}
}













