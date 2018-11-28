#include <iostream>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

char combine[64][64];
bool opposite[64][64];
char elements[128];

void solve(){
		for (int i = 0; i < 64; i++){
			for (int j = 0; j < 64; j++){
				combine[i][j] = '-';
				opposite[i][j] = false;
			}
		}

		int C;
		cin >> C;
		for (int i = 0; i < C; i++){
			cin >> elements;
			combine[elements[0] - 'A'][elements[1] - 'A'] = elements[2];
			combine[elements[1] - 'A'][elements[0] - 'A'] = elements[2];
		}

		int D;
		cin >> D;
		for (int i = 0; i < D; i++){
			cin >> elements;
			opposite[elements[0] - 'A'][elements[1] - 'A'] = true;
			opposite[elements[1] - 'A'][elements[0] - 'A'] = true;
		}

		int N;
		cin >> N;
		cin >> elements;
		vector < char > list;
		for (int i = 0; i < N; i++){
			char temp = elements[i];

			if (list.size() == 0){
				list.push_back(temp);
				continue;
			}

			if (combine[list[list.size() - 1] - 'A'][temp - 'A'] != '-'){
				char toPush = combine[list[list.size() - 1] - 'A'][temp - 'A'];
				list.pop_back();
				list.push_back(toPush);
				continue;
			}

			bool flag = false;
			for (int j = 0; j < list.size(); j++){
				if (opposite[list[j] - 'A'][temp - 'A'] == true){
					list = vector < char > ();
					flag = true;
					break;
				}
			}

			if (flag == false){
				list.push_back(temp);
			}

		}

	cout << "[";
	for (int i = 0; i < (int)list.size() - 1; i++){
		cout << list[i] << ", ";
	}
	if (list.size() > 0){
		cout << list[list.size() - 1];
	}
	cout << "]" << endl;
}

int main(){
	int tests;
	cin >> tests;

	for (int t = 1; t <= tests; t++){
		cout << "Case #" << t << ": ";
		solve();
	}

	return 0;
}
