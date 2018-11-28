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
#define filla(a, x)	for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++) a[i] = x
#define all(a) a.begin(), a.end()
#define sort(a) sort(all(a))
#define mp make_pair

using namespace std;

const int MAX = 1000;
const int MAXC = 1000000000;

ifstream fin("A.in");
ofstream fout("A.OUT");
int Test, NumTest, S, Q;
string Name[1000], Query[1000];
int Cost[MAX][100];

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> S;
	getline(fin, Name[0]);	
	for (int i = 0; i < S; i++) getline(fin, Name[i]);
			
	fin >> Q;
	getline(fin, Query[0]);
	for (int i = 0; i < Q; i++) getline(fin, Query[i]);
}

void Init(){
	for (int i = 0; i < Q; i++)
		for (int j = 0; j < S; j++) Cost[i][j] = MAXC;
}

void Solve(){
	for (int i = 0; i < S; i++)
		if (Name[i] != Query[0]) Cost[0][i] = 0;
		
	for (int i = 1; i < Q; i++)
		for (int j = 0; j < S; j++)
			if (Query[i] != Name[j]){
				Cost[i][j] = Cost[i - 1][j];
				for (int k = 0; k < S; k++)
					Cost[i][j] = min(Cost[i][j], Cost[i - 1][k] + 1);
			}
}

void PrintResult(){
	if (Q == 0) fout << "Case #" << Test + 1 << ": " << 0 << endl;
	else fout << "Case #" << Test + 1 << ": " << *min_element(Cost[Q - 1], Cost[Q - 1] + S) << endl;
}

void Done(){
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
