

#include<iostream>
using namespace std;

int main() {

	FILE* ifp, *ofp;
	ifp = freopen("A-large.in", "r", stdin);
	ofp = freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {

		int N, K;
		cin >> N >> K;
		int tk, p2 = ((1 << N) - 1);

		tk = K & p2;
		cout << "Case #" << i << ": " /*<< N << " " << K << " "*/;
		if(tk == p2) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}

	fclose(ofp);
	fclose(ifp);
	return 0;
}
