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

const double EPS = 0.0000000001;

ifstream fin ("B.INP");
ofstream fout("B.OUT");
int NumTest, Test;
int N, M, A;
bool Result;
int SaveX1, SaveY1, SaveX2, SaveY2, SaveX3, SaveY3;

void Prepare(){
	fin >> NumTest;
}

void Enter(){
	fin >> N >> M >> A;
}

void Init(){
	Result = false;
}

void Solve(){
	for (int x1 = 0; x1 <= N; x1++)
		for (int x2 = x1; x2 <= N; x2++)
			for (int x3 = x2; x3 <= N; x3++)
				for (int y1 = 0; y1 <= M; y1++)
					for (int y2 = 0; y2 <= M; y2++){
						double y3 = A - (x2 - x1) * (y1 + y2) - (x3 - x2) * y2 - (x1 - x3) * y1;
						y3 /= (x1 - x2);
						if (abs(y3 - (int)y3) <= EPS && 0 <= y3 && y3 <= M){
							Result = true;
							SaveX1 = x1;
							SaveY1 = y1;
							SaveX2 = x2;
							SaveY2 = y2;
							SaveX3 = x3;
							SaveY3 = (int)y3;
							return;
						}
					}
}

void PrintResult(){
	fout << "Case #" << Test + 1 << ": ";
	if (!Result) fout << "IMPOSSIBLE";
	else fout << SaveX1 << " " << SaveY1 << " " << SaveX2 << " " << SaveY2 << " " << SaveX3 << " " << SaveY3;
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
		cout << Test << endl;
	}
	Done();
//	getchar();
}
