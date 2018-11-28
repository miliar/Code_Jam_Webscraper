#include <iostream>
using namespace std;
int abs(int x) {return x>0?x:-x;}
int main() {
	int T, k, N, ord[110], loc[110], mv, i, a, buf[2], pos[2];
	char which;
	cin >> T;
	for(k=1;k<=T;k++) {
		cin >> N;
		for(i=0;i<N;i++) {
			cin >> which >> a;
			loc[i] = a;
			ord[i] = which == 'O' ? 1 : 0;
		}
		pos[0] = pos[1] = 1;
		buf[0] = buf[1] = a = 0;
		for(i=0;i<N;i++) {
			mv = abs(loc[i] - pos[ord[i]]) - buf[ord[i]];
			if (mv < 0) mv = 0; mv++;
			buf[1-ord[i]] += mv;
			buf[ord[i]] = 0;
			pos[ord[i]] = loc[i];
			a += mv;
		}
		cout << "Case #" << k << ": " << a << endl;
	}
	return 0;
}
