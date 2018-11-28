#include <algorithm>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
struct Node {
	int speed;
	double length;
	friend bool operator < (const Node &a, const Node &b) {
		return a.speed < b.speed;
	}
};

int main() {
	int T;
	scanf("%d", &T);
	int X, S, R, m, N;
	Node tmp;
	for (int t = 1; t <= T; t++) {
		scanf("%d %d %d %d %d", &X, &S, &R, &m, &N);
		int b, e, w;
		vector<Node> nn;
		double res = .0;
		int total = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d %d %d", &b, &e, &w);
			tmp.speed =  S + w;
			tmp.length = (double)(e - b);
			total += tmp.length;
			nn.push_back(tmp);
		}
		if (total < X) {
			tmp.speed = (double)S;
			tmp.length = X - total;
			nn.push_back(tmp);
		}
		sort(nn.begin(), nn.end());
		double remain = (double)m;
		for (int i = 0; i < nn.size(); i++) {
			R += nn[i].speed - S;
			if (nn[i].speed < R && remain > .0) {
				double tt = nn[i].length / R;
				if (tt <= remain) {
					res += tt;
					remain -= tt;
				}else {
					double left = nn[i].length - remain * R;
					res += (remain + left / nn[i].speed);
					remain = .0;
				}
			}else 
				res += (nn[i].length / nn[i].speed);
			R -= nn[i].speed - S;
		}
		printf("Case #%d: %.8lf\n", t, res);
		nn.clear();
	}
	return 0;
}
