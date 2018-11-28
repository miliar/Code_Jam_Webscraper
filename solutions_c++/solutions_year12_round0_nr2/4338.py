#include <iostream>
#include <algorithm>

using namespace std;

int scores[100];

int main(){
	int T;
	cin >> T;
	int cas = 1;
	while(T--){
		int N, S, p;
		cin >> N >> S >> p;
		for(int i = 0; i < N; ++i){
			cin >> scores[i];
		}
		sort(scores, scores+N);

		int minGood = 3*p-2;
		if(p == 0) minGood = 0;
		int minSupGood = 3*p-4;
		if(p == 0) minSupGood = 0;
		if(p == 1) minSupGood = 1;
		int numSupGood = 0;
		int numGood = 0;
		for(int i = 0; i < N; ++i){
			if(scores[i] >= minGood) numGood++;
			else if(scores[i] >= minSupGood) numSupGood++;
		}
		numSupGood = (S <= numSupGood)? S:numSupGood;
		cout << "Case #" << cas << ": " << (numSupGood+numGood) << endl; 
		cas++;
	}
}

