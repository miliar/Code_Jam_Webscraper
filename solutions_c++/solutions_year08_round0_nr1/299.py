#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>

using namespace std;

void process_case(){
	int S; cin >> S;

	vector<string> engines(S);
	getline(cin, engines[0]);
	for (int i=0; i<S; i++){
		getline(cin,engines[i]);
	}

	int Q; cin >> Q;
	int occupancy[S];
	for (int k=0; k<S; k++){
		occupancy[k] = 0;
	}

	string e;
	getline(cin,e);
	int ei,j,switches=0;

	for (int i=0; i<Q; i++){
		getline(cin, e);
		for (int f=0; f<2; f++){
		ei = distance(engines.begin(), find(engines.begin(), engines.end(), e));
		occupancy[ei]++;
		for (j=0; j<S; j++){
			if (occupancy[j] == 0) break;
		}
		if (j==S) {
			switches++;
			for (int k=0; k<S; k++){
				occupancy[k] = 0;
			}
		}
		}
	}
	cout << switches << endl;
}

int main() {
	int N;
	cin >> N;
	for (int i=0; i<N; i++){
		cout << "Case #" << i+1 <<": ";
		process_case();
	}
	return 0;
}
