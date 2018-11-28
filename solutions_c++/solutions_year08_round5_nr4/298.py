#include <algorithm>
#include <cstdio>
#include <cmath>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#include <fstream>
#include <sstream>
#include <iostream>

#define fill(a, x)	memset(a, x, sizeof(a))
#define fillv(a, x) for (int i = 0; i < a.size(); i++) a[i] = x;
#define filla(a, x)	for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++) a[i] = x
#define allv(a) a.begin(), a.end()
#define alla(a, n) a, a + n
#define sortv(a) sort(all(a))
#define sorta(a, n) sort(a, a + n)
#define mp make_pair

using namespace std;

const int MAX = 200;
const int BASE = 10007;

ifstream fin ("D.INP");
ofstream fout("D.OUT");
int NumTest, Test;
int n, m, k;
bool Free[MAX][MAX];
int d[MAX][MAX];

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fill(Free, true);
	fin >> n >> m >> k;
	for (int i = 0; i < k; i++){
		int x, y;
		fin >> x >> y;
		Free[x][y] = false;
	}
}

void Init(){
	fill(d, 0);
	d[1][1] = 1;
}

void Solve(){
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			if (Free[i][j]){
				d[i + 1][j + 2] = (d[i + 1][j + 2] + d[i][j]) % BASE;
				d[i + 2][j + 1] = (d[i + 2][j + 1] + d[i][j]) % BASE;
			}
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << d[n][m] << endl;
}

void Done(){
	fout.close();
}

int main(){
	Prepare();
	for (Test = 0; Test < NumTest; Test++){		
		Enter();
		Init();
		Solve();
		PrintResult();
	}
	Done();
//	getchar();
}
