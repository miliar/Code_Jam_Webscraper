#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;


int N;
int M;
int a[100];
int b[100];
string s;

int B = 1;
int O = 1;
int R = 0;
int get_step(int x, int y) {
	return abs(x - y);
}
int moveOne(int x, int next, int step2, int time) {
	if (step2 < time) {
		return next;
	}
	if (next < x) {
		return x - time;
	}
	else {
		return x + time;
	}
	return x;	
}

int getRet() {
	B = 1;
	O = 1;
	R = 0;
	int cur = 0;
	int cur1 = 0;
	int cur2 = 0;
	while (cur < M) {
		int next1 = 0;
		for (int i = cur1; i < M; i++)
			if (b[i] == 1) {
				cur1 = i;
				next1 = a[i];
				break;
			}
		int next2 = 0;
		for (int i = cur2; i < N; i++) {
			if (b[i] == 2) {
				cur2 = i;
				next2 = a[i];
				break;
			}
		}
		int step1 = get_step(O, next1);
		int step2 = get_step(B, next2);

		if (b[cur] == 1) {
			R += step1;
			cur1 += 1;
			R += 1;

			O = next1;
			B = moveOne(B, next2, step2, step1 + 1);
			cur += 1;
		} else {
			R += step2;
			cur2 += 1;
			R += 1;

			O = moveOne(O, next1, step1, step2 + 1);
			B = next2;
			cur += 1;
		}
	}
	return R;
}

int main() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> M;
		for (int j = 0; j < M; j++) {
			cin >> s >> a[j];
			if (s.compare("O") == 0)
				b[j] = 1;
			else
				b[j] = 2;
		}

		int ret = getRet();
		cout << "Case #" << i << ": " << ret << endl;
	}
	return 0;
}
