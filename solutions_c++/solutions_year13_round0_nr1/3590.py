#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;

string ttt[4];
int test = 1;

void solve() {
	bool O, X;
	O = X = false;

	for(int i=0; i<4; i++) cin >> ttt[i];
	for(int i=0; i<4; i++) {
		int cnt(0);
		bool T = false;
		for(int j=0; j<4; j++) {
			if( ttt[i][j] == 'O' ) cnt++;
			if( ttt[i][j] == 'T' ) T = true;
		}
		if( cnt == 4 || ( cnt == 3 && T ) ) O = true;
		if( O ) break;
	}
	for(int i=0; i<4; i++) {
		int cnt(0);
		bool T = false;
		for(int j=0; j<4; j++) {
			if( ttt[j][i] == 'O' ) cnt++;
			if( ttt[j][i] == 'T' ) T = true;
		}
		if( cnt == 4 || ( cnt == 3 && T ) ) O = true;
		if( O ) break;
	}

	for(int i=0; i<4; i++) {
		int cnt(0);
		bool T = false;
		for(int j=0; j<4; j++) {
			if( ttt[i][j] == 'X' ) cnt++;
			if( ttt[i][j] == 'T' ) T = true;
		}
		if( cnt == 4 || ( cnt == 3 && T ) ) X = true;
		if( X ) break;
	}
	for(int i=0; i<4; i++) {
		int cnt(0);
		bool T = false;
		for(int j=0; j<4; j++) {
			if( ttt[j][i] == 'X' ) cnt++;
			if( ttt[j][i] == 'T' ) T = true;
		}
		if( cnt == 4 || ( cnt == 3 && T ) ) X = true;
		if( X ) break;
	}

	int cnt(0);
	bool T = false; 
	for(int i=0; i<4; i++) {
		if( ttt[i][i] == 'O' ) cnt++;
		if( ttt[i][i] == 'T' ) T = true;
	}
	if( cnt == 4 || ( cnt == 3 && T ) ) O = true;
	
	cnt = 0;
	T = false; 
	for(int i=0; i<4; i++) {
		if( ttt[i][3-i] == 'O' ) cnt++;
		if( ttt[i][3-i] == 'T' ) T = true;
	}
	if( cnt == 4 || ( cnt == 3 && T ) ) O = true;

	cnt = 0;
	T = false; 
	for(int i=0; i<4; i++) {
		if( ttt[i][i] == 'X' ) cnt++;
		if( ttt[i][i] == 'T' ) T = true;
	}
	if( cnt == 4 || ( cnt == 3 && T ) ) X = true;

	cnt = 0;
	T = false; 
	for(int i=0; i<4; i++) {
		if( ttt[i][3-i] == 'X' ) cnt++;
		if( ttt[i][3-i] == 'T' ) T = true;
	}
	if( cnt == 4 || ( cnt == 3 && T ) ) X = true;


	if( O && X ) printf("Case #%d: Draw\n", test++);
	else if( O ) printf("Case #%d: O won\n", test++);
	else if( X ) printf("Case #%d: X won\n", test++);
	else {
		for(int i=0; i<4; i++) for(int j=0; j<4; j++) if( ttt[i][j] == '.' ) {
			printf("Case #%d: Game has not completed\n", test++);
			return;
		}
		printf("Case #%d: Draw\n", test++);
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	while(TC-->0) solve();
	return 0;
}