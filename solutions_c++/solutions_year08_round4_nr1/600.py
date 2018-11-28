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

const int MAX = 20000;
const int MAXC = 1000000000;

ifstream fin ("A.IN");
ofstream fout("A.OUT");
int NumTest, Test, n, V;
bool Change[MAX], TAnd[MAX];
int Ok[MAX][2];

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> n >> V;
	for (int i = 0; i < MAX; i++)
		for (int j = 0; j < 2; j++) Ok[i][j] = MAXC;
	fill(Change, false);
	fill(TAnd, false);
	
	int g, c;
	for (int i = 1; i <= (n - 1) / 2; i++){
		fin >> g >> c;
		if (g == 1) TAnd[i] = true;
		if (c == 1) Change[i] = true;
	}
	
	for (int i = (n - 1) / 2 + 1; i <= n; i++){
		fin >> g;
		Ok[i][g] = 0;	
	}
}

void Init(){
}

void Solve(){
	for (int i = (n - 1) / 2; i >= 1; i--)
		for (int j = 0; j < 2; j++)
			for (int k = 0; k < 2; k++)
				if (Ok[2 * i][j] != MAXC && Ok[2 * i + 1][k] != MAXC){
					int Temp = Ok[2 * i][j] + Ok[2 * i + 1][k];
					if (TAnd[i]) Ok[i][j & k] = min(Ok[i][j & k], Temp);
					else Ok[i][j | k] = min(Ok[i][j | k], Temp);
					
					if (Change[i]){
						if (TAnd[i]) Ok[i][j | k] = min(Ok[i][j | k], Temp + 1);
						else Ok[i][j & k] = min(Ok[i][j & k], Temp + 1);
					}
				}
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": ";
	if (Ok[1][V] == MAXC) fout << "IMPOSSIBLE";
	else fout << Ok[1][V];
	fout << endl;
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
