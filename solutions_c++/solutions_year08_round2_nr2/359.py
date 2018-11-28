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

const int MAX = 10000;

ifstream fin("B.INP");
ofstream fout("B.OUT");
int NumTest, Test, A, B, P, Father[MAX], Result;

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> A >> B >> P;	
}

void Init(){
	filla(Father, -1);
	Result = B - A + 1;
}

bool Prime(int p){
	if (p < 2) return false;
	for (int i = 2; i <= sqrt(p); i++)
		if (p % i == 0) return false;
	return true;
}

int Find(int u){
	while (Father[u] > 0) u = Father[u];
}

void Union(int u, int v){
	int x = Father[u] + Father[v];
	if (Father[u] < Father[v]){
		Father[v] = u;
		Father[u] = x;
	}
	else{
		Father[u] = v;
		Father[v] = x;
	}
}

void Solve(){
	for (int i = P; i <= B; i++)
		if (Prime(i)){
			vector<int> List;
			int Temp = i;
			while (Temp <= B){
				if (Temp >= A) List.push_back(Temp);
				Temp += i;
			}
			for (int j = 0; j < List.size(); j++)
				for (int k = j + 1; k < List.size(); k++){
					int u = Find(List[j]);
					int v = Find(List[k]);
					if (u != v){
						Result--;
						Union(u, v);
					}
				}
		}
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": " << Result << endl;
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
}
