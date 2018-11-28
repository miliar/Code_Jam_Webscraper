#include <vector>
#include <iostream>
using namespace std;

int pos[2] = {1, 1};
int target[2] = {-1, -1};

int move(int no) {
	if(target[no] != -1 && pos[no] != target[no]) {
		pos[no] += ((pos[no] > target[no]) ? -1 : 1);
	}
}

int get_no(char letter) {
	return (letter == 'b' || letter == 'B') ? 0 : 1;
}

int solve(int case_no) {
	// read the input
	int n;
	vector<pair<int, int> > input;
	cin >> n;
	for(int i = 0; i < n; i++) {
		char letter;
		int pos;
		cin >> letter >> pos;
		input.push_back(pair<int, int>(get_no(letter), pos));
	}
	// prepare the targets
	vector<int> next_target[2];
	for(int no = 0; no < 2; no++) {
		next_target[no].resize(n);
		int p = -1;
		for(int i = n - 1; i >= 0; i--) {
			next_target[no][i] = p;
			if(input[i].first == no)
				p = input[i].second;
		}
		target[no] = p;
		pos[no] = 1;
		// debug
		//for(int i = 0; i < n; i++)
		//	cerr << next_target[no][i] << ' ';
		//cerr << endl;
	}
	// run the simulation
	int time = 0, ind = 0;
	for(; ind < n; time++) {
		//cerr << ind << ' ' << time << ' ' << pos[0] << "->" << target[0] << ' ' << pos[1] << "->" << target[1]<< endl;
		if(pos[input[ind].first] == input[ind].second) {
			target[input[ind].first] = next_target[input[ind].first][ind];
			move(1 - input[ind].first);
			ind++;
		} else {
			move(0);
			move(1);
		}
	}
	cout << "Case #" << case_no << ": " << time << endl;
}

int main() {
	int case_count;
	cin >> case_count;
	for(int i = 1; i <= case_count; i++) {
		solve(i);
	}
	return 0;
}
