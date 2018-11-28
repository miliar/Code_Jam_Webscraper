#include <iostream>
#include <queue>

using namespace std;

int doCase() {
	queue<int> q;
	
	int R, k, N;
	
	cin >> R >> k >> N;
	
	for(int i = 0; i < N; i++) {
		int v;
		cin >> v;
		q.push(v);
	}
	
	int totalEuros = 0;
	
	for(int i = 0; i < R; i++) {
		int thisTime = 0;
		int groupsRiding = 0;
		while(true) {
			if(groupsRiding >= N)
				break;
			int currGroup = q.front();
			if (currGroup + thisTime > k)
				break;
			thisTime += currGroup;
			q.pop();
			q.push(currGroup);
			groupsRiding++;
		}
		totalEuros += thisTime;
	}
	
	return totalEuros;
}


int main (int argc, char * const argv[]) {

	int T;
	
	cin >> T;
	
	for(int i = 0; i < T; i++) {
		int result = doCase();
		
		cout << "Case #" << (i + 1) << ": " << result << endl;
	}
	
	
    return 0;
}
