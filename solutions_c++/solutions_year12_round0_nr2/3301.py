#include <iostream>

using namespace std;

int T, N, S, P, score, avg, avgRem, maxDancers;

int main() {
	cin >> T;
	for(int i=1; i<=T; ++i) {
		maxDancers = 0;
		cin >> N >> S >> P;
		cout << "Case #" << i << ": ";
		for(int j=0; j<N; ++j) {
			cin >> score;
			avg = score/3;
			avgRem = score%3;
			
			if(score >= P*3-2) {++maxDancers; /*cout << "(" << score << ") ";*/ continue;}
			if(score >= P*3-4 && S>0 && score>0) {++maxDancers; --S; /*cout << "(" << score << ") ";*/ continue;}
		}
		cout << maxDancers << endl;
	}
	return 0;
}