#include <cstdio>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cstring>
#include <string>


#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long

const int MAXN = 10;

using namespace std;

int N = 4;
int cntline[3][MAXN], cntcol[3][MAXN], cntTline[MAXN], cntTcol[MAXN];
int d1, d2, e;

string A[MAXN];


void clear() {
	for (int i = 0; i <= N; ++i) {
		cntline[1][i] = cntline[2][i] = cntTline[i] = 0;
		cntcol[1][i] = cntcol[2][i] = cntTcol[i] = 0;
	}
	d1 = 0, d2 = e = 0;
}

void preproc() {

	for (int i = 1; i <= N; ++i) 
		for (int j = 0 ; j < N; ++j) {
			cntline[1][i] += (A[i][j] == 'X');
			cntline[2][i] += (A[i][j] == 'O');
			cntTline[i] += (A[i][j] == 'T');
		}
	for (int j = 0 ; j < N; ++j)
		for (int i = 1; i <= N; ++i) {
			
			cntcol[1][j] += (A[i][j] == 'X');
			cntcol[2][j] += (A[i][j] == 'O');
			cntTcol[j]   += (A[i][j] == 'T');
			
			e |= (A[i][j] == '.');
		}
	
	int c1 = 0, c2 = 0, ct = 0;

	for (int i = 1;  i <= N; ++i) {
		if(A[i][i - 1] == 'X')
			++c1;
		if(A[i][i - 1] == 'O')
			++c2;
		if(A[i][i - 1] == 'T')
			++ct;
	}
	if( (c1 + ct == 4 && ct == 1) || c1 == 4)
		d1 = 1;
	if( (c2 + ct == 4 && ct == 1) || c2 == 4)
		d2 = 1;

	c1 = c2 = ct = 0;

	for (int i = 1; i <= N; ++i) {
		if(A[i][N - i] == 'X')
			++c1;
		if(A[i][N - i] == 'O')
			++c2;
		if(A[i][N - i] == 'T')
			++ct;
	}
	if( (c1 + ct == 4 && ct == 1) || c1 == 4)
		d1 = 1;
	if( (c2 + ct == 4 && ct == 1) || c2 == 4)
		d2 = 1;
}
bool win(int sel) {
	for (int i = 1; i <= N; ++i) {
		if( cntline[sel][i] == 4 || (cntline[sel][i] == 3 && cntTline[i] == 1))
			return 1;
		if (cntcol[sel][i - 1] == 4 || (cntcol[sel][i - 1] == 3 && cntTcol[i - 1] == 1))
			return 1;
	}
	if(sel == 1)
		return d1;
	
	if(sel == 2)
		return d2;

	return 0;

}
bool empty() {
	return e;
}
int main() {
	ifstream cin("test.in");
	ofstream cout("test.out");
	
	int T;	
	cin >> T;
	
	for (int test = 1; test <= T; ++test) {
		
		for (int i = 1; i <= N; ++i)
			cin >> A[i] ;
		clear();
		preproc();
		
	//	cout << d1 << " " << d2 << "\n";
		if(win(1)) {
			cout << "Case #" << test << ": " << "X won\n";
		}
		else if(win(2)) {
			cout << "Case #" << test << ": " << "O won\n";	
		}
		else if(empty()) {
			cout << "Case #" << test << ": " << "Game has not completed\n";
		} else {
			cout << "Case #" << test << ": " << "Draw\n";
		}
		
	}
	return 0;
}
