#include <iostream>
#include <vector>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int L, t, N, C;
		cin >> L >> t >> N >> C;
		vector<int> a(C);
		for(int i = 0; i < C; ++i){ cin >> a[i]; }
		int sum = 0;
		for(int i = 0; i < C; ++i){ sum += a[i]; }
		sum *= N / C;
		for(int i = N % C - 1; i >= 0; --i){ sum += a[i]; }
	}
	return 0;
}
