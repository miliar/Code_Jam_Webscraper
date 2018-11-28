#include <iostream>
#include <queue>

using namespace std;

struct operation {
	int pos, order;
	operation(int pos, int order): pos(pos), order(order) {}
};

inline int idx(char c) {
	return c == 'O';
}

inline int abs(int x) {
	return x < 0 ? -x : x;
}

int T;
int main() {
	cin >> T;
	for (int t = 1; t <= T; t ++) {
		int pos[] = {1, 1};
		queue<operation> operations[2];
		int N;
		cin >> N;
		int res = 0;
		for (int i = 0; i < N; i ++) {
			char c;
			int button;
			cin >> c >> button;
			operations[idx(c)].push(operation(button, i));
		}
		int time = 0;
		int order = 0;
		while (true) {
			if (operations[0].empty() && operations[1].empty()) {
				break;
			}
			time ++;
			int nextOrder = order;
			for (int i = 0; i < 2; i ++) {
				if (operations[i].empty()) {
					continue;
				}
				operation& o = operations[i].front();
				if (o.pos == pos[i]) {
					if (order == o.order) {
						nextOrder ++;
						operations[i].pop();
					}
				} else if (o.pos < pos[i]) {
					pos[i] --;
				} else {
					pos[i] ++;
				}
			}
			order = nextOrder;
		}
		cout << "Case #" << t << ": "<< time << "\n";
	}
}