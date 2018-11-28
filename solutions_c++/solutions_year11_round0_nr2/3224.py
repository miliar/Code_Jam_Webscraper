#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T, C, D, N;
	string str;
	int combine[36][36];
	bool opposed[36][36];
	vector<int> list;
	char e;
	int cc;
	bool cleared;

	cin >> T;
	for(int t=1; t<=T; ++t) {
		for(int i = 0; i < 36; ++i)
			for(int j = 0; j < 36; ++j) {
				combine[i][j] = -1;
				opposed[i][j] = false;
			}
		list.clear();
		cin >> C;
		for(int c=1; c <= C; ++c) {
			cin >> str;
			int x = str.c_str()[0] - 'A';
			int y = str.c_str()[1] - 'A';
//			cout << "x " << x << " y " << y << endl;
			combine[x][y] = combine[y][x] = str.c_str()[2] - 'A';
		}
		cin >> D;
		for(int d=1; d <= D; ++d) {
			cin >> str;
			int x = str.c_str()[0] - 'A';
			int y = str.c_str()[1] - 'A';
			opposed[x][y] = opposed[y][x] = true;
		}
		cin >> N;

		for(int n = 1; n <= N; ++n) {
			cin >> e;
			int x = e - 'A';
			cleared = false;
			if(!list.empty()){
				cc = combine[x][list.back()];
				if(cc != -1) {
					list.pop_back();
					list.push_back(cc);
					continue;
				}
				for(unsigned i = 0; i < list.size(); ++i) {
					if(opposed[list[i]][x]) {
						list.clear();
						cleared = true;
						break;
					}
				}
			}
			if(!cleared)
				list.push_back(x);
		}

		cout << "Case #"<< t << ": [";
		for(unsigned i = 0; i < list.size(); ++i) {
			if(i)
				cout << ", ";
			cout << char(list[i] + 'A');
		}
		cout << "]" << endl;
	}
	return 0;
}
