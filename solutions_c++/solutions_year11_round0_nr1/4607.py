#include <iostream>
#include <queue>
#include <map>
using namespace std;
int main(int argc, char *argv[]) {
	int T;
	cin>>T;
	for (int z = 1; z <= T; z++) {
		int N;
		cin>>N;
		queue<pair<int,int> > orange;
		queue<pair<int,int> > blue;
		for (int i = 0; i < N; i++) {
			char c; int button;
			cin>>c>>button;
			if (c == 'O') orange.push(make_pair(i,button));
			else if (c == 'B') blue.push(make_pair(i,button));
		}
		
		int pushed = 0, turn = 1;
		int o_locate = 1, b_locate = 1;
		while (true) {
			// flg
			bool pushed_flg = false;
			// Orange
			if (orange.size() > 0) {
				pair<int,int> tp = orange.front();
				if (tp.second > o_locate) {
					// action
					o_locate++;
				}
				else if (tp.second < o_locate) {
					// action
					o_locate--;
				}
				else if (tp.second == o_locate) {
					if (tp.first == pushed) {
						// pusehd
						pushed++;
						orange.pop();
						pushed_flg = true;
					}
				}
			}
			// Blue
			if (blue.size() > 0) {
				pair<int,int> tp = blue.front();
				if (tp.second > b_locate) {
					// action
					b_locate++;
				}
				else if (tp.second < b_locate) {
					// action
					b_locate--;
				}
				else if (tp.second == b_locate) {
					if (tp.first == pushed && !pushed_flg) {
						// pusehd
						pushed++;
						blue.pop();
					}
				}
			}
			if (pushed == N) break;
			turn++;
		}
		cout<<"Case #"<<z<<": "<<turn<< endl;
	}
	return 0;
}