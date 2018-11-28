#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int N;
		cin >> N;
		vector<int> C(N);
		int checker = 0, minvalue = INT_MAX, sum = 0;
		for(int i = 0; i < N; ++i){
			cin >> C[i];
			checker ^= C[i];
			minvalue = min(minvalue, C[i]);
			sum += C[i];
		}
		if(checker != 0){
			cout << "Case #" << caseNum << ": NO" << endl;
		}else{
			cout << "Case #" << caseNum << ": " << (sum - minvalue) << endl;
		}
	}
	return 0;
}
