#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<cmath>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int i = 0; i < T; i++){
		int N;
		cin >> N;
		int S;
		cin >> S;
		int p;
		cin >> p;
		int t[N];
		for (int j = 0; j < N; j++){
			cin >> t[j];
		}
		int numGood = 0;
		for (int j = 0; j < N; j++){
			if (p == 0) numGood++;
			else if (p*3-2 <= t[j]) numGood++;
			else if (p*3-4 <= t[j] && S > 0 && p*3-4 >= 0){
				numGood++;
				S--;
			}
		}
		cout << "Case #" << i+1 << ": ";
		cout << numGood << endl;
	}
	return 0;
}