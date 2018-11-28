#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool test(int x, vector<int> notes) {
	int m;
	for(int i=0; i < notes.size(); i++) {
		if(x > notes[i]) {
			m = x % i;
		} else {
			m = i % x;
		}
		if(m != 0) {
			return false;
		}
	}
	return true;
}

int solve(int N, int L, int H, vector<int> notes) {
	for(int i=L; i < H+1; i++) {
		bool harmony = test(i, notes);
		if(harmony) {
			return i;
		}
	}
	return 0;
}
int main() {
	int T;
	int N, L, H;
	vector<int> notes;
	cin >> T;
	for(int i=0; i < T; i++) {
		cin >> N >> L >> H;
		notes.clear();
		for(int j=0; j < N; j++) {
			int temp;
			cin >> temp;
			notes.push_back(temp);
		}
		bool ret = solve(N,L,H, notes);
		printf("Case #%d: ",i+1);
		cout << ret << endl; 
	}
}