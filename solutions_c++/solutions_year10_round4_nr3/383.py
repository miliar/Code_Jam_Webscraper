#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>
#include <set>
#include <iostream>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define SZ(u) ((int)u.size())
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

inline bool isDigit(char a) { return '0' <= a && a <= '9'; }

int R, N;
vvi Board[2];

bool isValid(int r, int c) { return 0 <= r && r < N && 0 <= c && c < N; }
void pre_process();
void input();
void process();

int main()
{
	int t, T;
	//scanf("%d", &T);
	cin >> T;
	pre_process();

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
		fflush(stdout);
	}
	return 0;
}

void pre_process() {
}
void input() {
	int i, j, k;
	int x1, y1, x2, y2;
	cin >> R;
	N = 100;
	
	Board[0] = vvi(N, vi(N, 0));
	
	fr (i, R) {
		cin >> x1 >> y1 >> x2 >> y2;
		x1--, y1--, x2--, y2--;
		for (j = x1; j <= x2; j++) for (k = y1; k <= y2; k++) {
			Board[0][j][k] = 1;
		}
	}
}

bool isVac(int t, int r, int c) {
	return isValid(r, c) && Board[t][r][c];
}

void process() {
	int i, j;
	int T = 0, UT, res = 0;
	bool flag;
	
	do {
		UT = T;
		T = !T;
		res++;
		
		Board[T] = vvi(N, vi(N, 0));
		flag = false;
		fr (i, N) fr (j, N) {
			if (isVac(UT,i,j) && (isVac(UT, i-1, j) || isVac(UT, i, j-1))) {
				Board[T][i][j] = 1;
				flag = true;
			}
			
			if (!isVac(UT,i,j) && isVac(UT, i-1, j) && isVac(UT, i, j-1)) {
				Board[T][i][j] = 1;
				flag = true;
			}
		}
	} while(flag);
	
	printf("%d\n", res);
}