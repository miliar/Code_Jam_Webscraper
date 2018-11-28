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

const int MAX = 15;

ifstream fin ("C.INP");
ofstream fout("C.OUT");
int NumTest, Test;
int n, m;
int d[MAX][1 << MAX];
char Free[MAX][MAX];

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) fin >> Free[i][j];
}

void Init(){
	fill(d, 0);
}

bool Student(int p, int i){
	return p & (1 << i);
}

void Solve(){
	for (int i = 1; i <= n; i++)
		for (int p = 0; p < (1 << m); p++){
			bool Ok = true;
			for (int j = 0; j < m; j++)
				if (Student(p, j) && Free[i - 1][j] == 'x'){
					Ok = false;
					break;
				}
			if (!Ok) continue;
			for (int j = 0; j < m - 1; j++)
				if (Student(p, j) && Student(p, j + 1)){
					Ok = false;
					break;
				}
			if (!Ok) continue;
						
			for (int p0 = 0; p0 < (1 << m); p0++){
				Ok = true;
				for (int j = 0; j < m; j++)
					if (Student(p, j)){
						if (j > 0 && Student(p0, j - 1)){
							Ok = false;
							break;
						}
						if (j < m - 1 && Student(p0, j + 1)){
							Ok = false;
							break;
						}
					}			
				if (!Ok) continue;
				
				int Num = 0;
				for (int j = 0; j < m; j++)
					if (Student(p, j)) Num++;									
				d[i][p] = max(d[i][p], d[i - 1][p0] + Num);
			}
		}
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << *max_element(d[n], d[n] + (1 << m)) << endl;
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
