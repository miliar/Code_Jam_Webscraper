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

ifstream fin ("D.INP");
ofstream fout("D.OUT");
int NumTest, Test, Result;
int k;
string S;

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> k;
	fin >> S;	
}

void Init(){
	Result = S.length();
}

void Solve(){
	vector <int> p;
	for (int i = 0; i < k; i++) p.push_back(i);
	do{
		string Temp = S;
		int Start = 0;
		while (Start < S.length()){
			for (int i = 0; i < k; i++) Temp[Start + i] = S[Start + p[i]];
			Start += k;
		}
		int Now = 1;
		for (int i = 1; i < Temp.length(); i++)
			if (Temp[i] != Temp[i -1]) Now++;
		Result = min(Result, Now);
	}while (next_permutation(p.begin(), p.end()));
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
