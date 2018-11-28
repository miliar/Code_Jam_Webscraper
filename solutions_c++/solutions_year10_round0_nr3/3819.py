#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(int argc, char* argv) {
	int T;
	cin >> T;
	for(int t=0; t<T; ++t) {
		int R, k, N;
		cin >> R >> k >> N;
		queue<int> que;
		for(int n=0; n<N; ++n) {
			int v;
			cin >> v;
			que.push(v);
		}
		int money = 0;
		for(int r=0; r<R; ++r) {
			int left = k;
			queue<int> que2;
			while(que.size() > 0 && que.front() <= left) {
				que2.push(que.front());
				money += que.front();
				left -= que.front();
				que.pop();
			}
			while(que2.size()>0) {
				que.push(que2.front());
				que2.pop();
			}
		}
		cout << "Case #" << t+1 << ": " << money << endl;
	}
	return 0;
}




