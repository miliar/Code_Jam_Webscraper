#include <iostream>
#include <vector>
#include <string.h>

int mem[1001][1001][11];

using namespace std;
int C;
int solve(int L, int P) {
	if(L*C>=P) return 0;
	int & result = mem[L][P][C];
	if(result!=-1) return result;
	result = 100000;
	for(int i = L+1; i < P; i++) {
		result = min(result, max(solve(L,i),solve(i,P)));
	}
	result += 1;
	return result;
}

int main () {
	memset(mem,-1,sizeof(mem));
	int T, caso = 1;
	cin >> T;
	while(caso <= T) {
		int result = 0;
		int L,P;
		cin >> L >> P >> C;
		result = solve(L,P);
		cout << "Case #" << caso++ << ": " << result << endl;
	}
	return 0;
}
