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
#define mp make_pair

using namespace std;

const int MAX = 1000;

ifstream fin("B.IN");
ofstream fout("B.OUT");
int Test, NumTest, T, nA, nB, ResultA, ResultB;
pair<int, int> TimeA[MAX], TimeB[MAX];
bool FreeA[MAX], FreeB[MAX];

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> T;
	fin >> nA >> nB;
	for (int i = 0; i < nA; i++){
		string s;
		fin >> s;
		TimeA[i].second = ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';		
		
		fin >> s;
		TimeA[i].first  = ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';
	}
	
	for (int i = 0; i < nB; i++){
		string s;
		fin >> s;
		TimeB[i].second = ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';		
		
		fin >> s;
		TimeB[i].first  = ((s[0] - '0') * 10 + s[1] - '0') * 60 + (s[3] - '0') * 10 + s[4] - '0';
	}	
}

void Init(){
	sort(TimeA, TimeA + nA);
	sort(TimeB, TimeB + nB);
	filla(FreeA, true);
	filla(FreeB, true);
}

void Solve(){
	ResultA = 0;
	ResultB = 0;
	for (int i = 0; i < nA; i++){
		ResultA++;
		for (int j = nB - 1; j >= 0; j--)
			if (FreeB[j] && TimeA[i].second >= TimeB[j].first + T){
				FreeB[j] = false;
				ResultA--;
				break;
			}
	}
	
	for (int i = 0; i < nB; i++){
		ResultB++;
		for (int j = nA - 1; j >= 0; j--)
			if (FreeA[j] && TimeB[i].second >= TimeA[j].first + T){
				FreeA[j] = false;
				ResultB--;
				break;
			}
	}		
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << ResultA << " " << ResultB << endl;
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
