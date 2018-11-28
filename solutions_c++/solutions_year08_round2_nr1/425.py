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

const int MAX = 1000000;

ifstream fin("A.INP");
ofstream fout("A.OUT");
int NumTest, Test;
long long X[MAX], Y[MAX], Result, n;

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	long long A, B, C, D, M;
	fin >> n >> A >> B >> C >> D >> X[0] >> Y[0] >> M;
	for (int i = 1; i < n; i++){
		X[i] = (A * X[i - 1] + B) % M;
		Y[i] = (C * Y[i - 1] + D) % M;
	}
}

void Init(){
	Result = 0;
}

void Solve(){
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			for (int k = j + 1; k < n; k++)
				if ((X[i] + X[j] + X[k]) % 3 == 0 && (Y[i] + Y[j] + Y[k]) % 3 == 0) Result++;
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << Result << endl;
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
