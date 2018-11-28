#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int N, L, H;
		cin >> N >> L >> H;
		int A[10001];
		for(int i=0; i<N; i++)
			cin >> A[i];
		int f;
		for(f=L; f<=H; f++) {
			int i;
			for(i=0; i<N; i++)
				if (A[i] % f != 0 && f % A[i] != 0)
					break;
			if (i == N)
				break;
		}
		cout << "Case #" << t << ": ";
		if (f > H)
			cout << "NO" << endl;
		else
			cout << f << endl;
	}
	return 0;
}

