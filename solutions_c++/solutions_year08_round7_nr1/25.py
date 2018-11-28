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

const int MAX = 1000;

ifstream fin ("A1.IN");
ofstream fout("A.OUT");
int NumTest, Test;
int n, Total, Need[MAX];
int List[MAX][MAX];
map <string, int> Index;

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	Index.clear();
	fill(Need, 0);
	Total = 0;
	fin >> n;
	for (int i = 0; i < n; i++){
		string s;		
		fin >> s;
		if (Index.count(s) == 0){
			Index[s] = Total;
			Total++;
		}
		int id = Index[s];
		int t;
		fin >> t;
		for (int j = 0; j < t; j++){
			fin >> s;
			if ('a' <= s[0] && s[0] <= 'z') continue;
			if (Index.count(s) == 0){
				Index[s] = Total;
				Total++;				
			}
			List[id][Need[id]] = Index[s];
			Need[id]++;
		}
	}
}

void Init(){
}

void Solve(){
}

int Cal(int p){
	int Result = Need[p] + 1;
	int SList[Need[p]];
	for (int i = 0; i < Need[p]; i++) SList[i] = Cal(List[p][i]);
	sort(SList, SList + Need[p]);
	for (int i = 0; i < Need[p]; i++) Result = max(Result, SList[i] + Need[p] - 1 - i);
	return Result;
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << Cal(0) << endl;
	cout << Test << endl;
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
