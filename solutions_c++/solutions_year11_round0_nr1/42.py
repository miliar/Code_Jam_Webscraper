#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		int N;
		cin >> N;
		int t1=0, t2=0;
		int p1=1, p2=1;
		for (int i=0;i<N;i++) {
			char x;
			int b;
			cin >> x >> b;

			if (x=='O') {
				int tinc=t1+abs(b-p1);
				t1=max(tinc,t2)+1;
				p1=b;
			}
			if (x=='B') {
				int tinc=t2+abs(b-p2);
				t2=max(tinc,t1)+1;
				p2=b;
			}
		}
		cout << "Case #" << t << ": " << max(t1,t2) << endl;
	}
	
	return 0;
}