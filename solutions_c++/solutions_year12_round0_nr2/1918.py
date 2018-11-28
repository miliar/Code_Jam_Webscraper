#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

const int MAXN = 100;
const int MAXP = 30;

int highPoint[MAXP][2];
void calcHighPoint()
{
	memset(highPoint, -1, sizeof highPoint);
	for (int a = 0; a <= 10; ++a)
		for (int b = a; b <= a + 2; ++b)
			for (int c = a; c <= a + 2; ++c) {
				int sp = 0;
				if (abs(a - b) == 2 || abs(b - c) == 2 || abs(a - c) == 2)
					sp = 1;
				int sum = a + b + c;
				int high = max(a, max(b, c));
				if (highPoint[sum][sp] < high)
					highPoint[sum][sp] = high;
			}
}

int main()
{
	calcHighPoint();
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		int N, S, p, ti, t[MAXN];
		int answer = 0;
		cin >> N >> S >> p;
		for (int i = 0; i < N; ++i) {
			cin >> ti;
			if (highPoint[ti][0] >= p)
				answer++;
			else if (S > 0 && highPoint[ti][0] < p && highPoint[ti][1] >= p) {
				answer++;
				S--;
			}
		}
		cout << "Case #" << testcase << ": " << answer << endl;
	}
	return 0;
}
