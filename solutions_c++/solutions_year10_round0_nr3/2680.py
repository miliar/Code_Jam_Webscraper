#include <iostream>
#include <queue>

using namespace std;

long calcBenefit(long R, long k, queue<long> groups) {
	long benefit = 0;
	for(long i = 1; i <= R; i++) {
		long alreadyOnBoard = 0;
		queue<long> onBoard;
		while((!groups.empty()) && (groups.front() + alreadyOnBoard <= k)) {
			long tmp = groups.front();
			groups.pop();
			onBoard.push(tmp);
			alreadyOnBoard += tmp;
			benefit += tmp;
		}
		while(!onBoard.empty()) {
			groups.push(onBoard.front());
			onBoard.pop();
		}
	}
	return benefit;
}

int main (int argc, char * const argv[]) {
    // insert code here...
	long T, R, k, N, g;
	
	cin >> T; //number of cases
	
	for(int i = 1; i <= T; i++) {
		cin >> R >> k >> N;
		queue<long> groups;
		for(int j = 1; j <= N; j++) {
			cin >> g;
			groups.push(g);
		}
		
		cout << "Case #" << i<< ": " << calcBenefit(R,k,groups);
		if(i < T) { cout << endl;}
	}
    
    return 0;
}
