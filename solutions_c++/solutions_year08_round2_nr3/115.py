#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int DIV=1000;
struct D {
	bool f[1000][DIV];
	int c[1000];
	int all[1000];
	int N_;

	void init(int N) {
		N_ = N;
		memset(c, 0, sizeof(c));
		memset(f, 0, sizeof(f));
		memset(all, 0, sizeof(all));
		for (int i=0; i < N; i++) {
			all[i/DIV]++;
		}
	}

	int next(int a, int b) {
		a = a % N_ + 1;
		int xa = (a-1)/DIV;
		int ya = (a-1)%DIV;
		while (b > 0 && ya < all[xa]) {
			if (f[xa][ya]==0) b--;
			ya++;
		}
		if (b > 0) {
			xa = (xa + 1) % 1000;
			while (b > 0 && all[xa]-c[xa] < b) {
				b -= (all[xa]-c[xa]);
				xa = (xa + 1) % 1000;
			}
		}
		if (b > 0) {
			ya = 0;
			while (b > 0 && ya < all[xa]) {
				if (f[xa][ya]==0) b--;
				ya++;
			}
		}
		c[xa]++;
		f[xa][ya-1]=1;
		return xa*DIV+ya;
	}
};

int r[1000000+1];
D d;

int main() {
	ifstream inp("c.in");
	ofstream out("c.out");
	int N;
	inp >> N;
	for (int test=1;test<=N;test++) {
		cout << test << endl;
		out << "Case #" << test << ":";

		int K, n;
		inp >> K >> n;
		memset(r, 0, sizeof(r));
		d.init(K);
		int s = K;
		for (int i = 1; i<= K; i++) {
			int k = d.next(s, i);
			r[k] = i;
			s = k;
		}
		for (int i = 0; i < n; i++) {
			inp >> K;
			out << " " << r[K];
		}
		out << endl;
	}
}

