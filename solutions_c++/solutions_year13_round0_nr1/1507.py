#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


const int size = 4;
int ar[size][size];

int solution(int nTest) {
	int cnt = 0;
	For(i, 0, size) {
		For(j, 0, size) {
			ar[i][j] = 0;
		}
	}
	For(i, 0, 4) {
		scanf("%s", buffer);
		For(j, 0, 4) {
			char c = buffer[j];
			if(c == 'X') {
				ar[i][j] = 1;
			} else if(c == 'O') {
				ar[i][j] = 2;
			} else if(c == 'T') {
				ar[i][j] = 3;
			} else {
				cnt++;
			}
		}
	}
	int n = 4;
	int o = 0, x = 0;
	For(i, 0, n) {
		int t = 3;
		For(j, 0, n) {
			t &= ar[i][j];
		}
		if(t & 1) {
			x = 1;
		}
		if(t & 2) {
			o = 1;
		}
	}

	For(j, 0, n) {
		int t = 3;
		For(i, 0, n) {
			t &= ar[i][j];
		}
		if(t & 1) {
			x = 1;
		}
		if(t & 2) {
			o = 1;
		}
	}
	int t = 3;
	For(i, 0, n) {
		t &= ar[i][i];
	}
	if(t & 1) {
		x = 1;
	}
	if(t & 2) {
		o = 1;
	}
	t = 3;
	For(i, 0, n) {
		t &= ar[i][n - 1 - i];
	}
	if(t & 1) {
		x = 1;
	}
	if(t & 2) {
		o = 1;
	}

	if(x && o) {
		puts("Draw");
	} else if(x == 1) {
		puts("X won");
	} else if(o == 1) {
		puts("O won");
	} else if(cnt == 0) {
		puts("Draw");
	} else {
		puts("Game has not completed");
	}



	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		solution(i);
	}

	return 0;
}
	
