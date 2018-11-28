#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int N;
		cin >> N;
		queue<int> orange;
		queue<int> blue;
		queue<pair<char, int> > input;
		for(int n=0; n<N; n++) {
			char col;
			int pos;
			cin >> col >> pos;
			if(col=='O') orange.push(pos);
			else blue.push(pos);
			input.push(make_pair(col, pos));
		}
		int op = 1;
		int bp = 1;
		int i=1;
		for(;;i++) {
			char x = input.front().first;
			// blue
			if(blue.front() == bp) {
				if(x=='B') {
					blue.pop();
					input.pop();
				}
			} else {
				if(blue.front()<bp) bp--;
				if(blue.front()>bp) bp++;
			}
			if(orange.front() == op) {
				if(x=='O') {
					orange.pop();
					input.pop();
				}
			} else {
				if(orange.front()<op) op--;
				if(orange.front()>op) op++;
			}
			if(input.size()==0) break;
		}
		cout << "Case #" << t << ": " << i << endl;
	}
	return 0;
}
