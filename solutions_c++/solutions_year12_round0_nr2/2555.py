#include <iostream>

using namespace std;

int max(int a, int b) {return (a>b?a:b);}

int main (void) {
	int T = 0;
	cin >> T;
	for (int t = 1; t<=T; ++t) {
		int N, S, p;
		int d = 0;
		cin >> N >> S >> p;
		int easy = -1, min = 0;
		switch (p) {
			case 0:
				easy = min = -1; break;
			case 1:
				easy = 1; min = 1; break;
			default:
				easy = 3*(p-1) + 1;
				min = 3*p-4;
			break;
		}
		for (int i = N; i>0; --i) {
			int x;
			cin >> x;
			if (x >= easy) d++;
			if (x < min) N--;
		}
		int y = d+S;
		if (y > N) y = N;
		cout<<"Case #"<<t<<": "<<y<<endl;
	}
	return 0;
}
