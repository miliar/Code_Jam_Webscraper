#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;
typedef pair<int, int> pii;

inline int iabs(int x){ return x < 0 ? -x : x; }

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		int N;
		cin >> N;
		vector<pii> tasks;
		for(int i = 0; i < N; ++i){
			string color;
			int button;
			cin >> color >> button;
			tasks.push_back(pii(button, color == "O" ? 0 : 1));
		}
		int p[2] = { 1, 1 }, t[2] = { 0, 0 };
		int currentTime = 0;
		for(int i = 0; i < N; ++i){
			pii task = tasks[i];
			t[task.second] = max(
				t[task.second] + iabs(p[task.second] - task.first),
				currentTime
			) + 1;
			p[task.second] = task.first;
//			cout << p[0] << "/" << t[0] << ", " << p[1] << "/" << t[1] << endl;
			currentTime = max(t[0], t[1]);
		}
		cout << "Case #" << caseNum << ": " << currentTime << endl;
	}
	return 0;
}
