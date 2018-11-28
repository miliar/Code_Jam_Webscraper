// for MinGW g++ 3.4.5
#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";

		string S;
		cin >> S;

		int digits = S.length();

		int n[20];
		for (int i = 0; i < digits; i++) {
			n[i] = S[i]-'0';
		}
		
		int d[10];
		for (int i = 0; i < 10; i++) {
			d[i] = 0;
		}
		for (int i = 0; i < digits; i++) {
			d[n[i]]++;
		}
		d[0]++;
		int ten2base[10];
		int base2ten[10];
		for (int i = 0; i < 10; i++) {
			ten2base[i] = 0;
			base2ten[i] = 0;
		}
		int base = 0;
		for (int i = 0; i < 10; i++) {
			if (d[i]) {
				ten2base[i] = base;
				base2ten[base] = i;
				base++;
			}
		}
		d[0]--;
		
		for (int i = 0; i < digits; i++) {
			n[i] = ten2base[n[i]];
		}

		int x = digits - 2;
		while(x >= 0 && n[x] >= n[x+1]) --x;
		if (x < 0) {
			x = 0;
			digits++;
			for (int i = digits - 1; i > 0; i--)	n[i] = n[i-1];
			n[0] = 0;
		}
		for (int i = 0; i < 10; i++) {
			d[i] = 0;
		}
		for (int i = x; i < digits; i++) {
			d[n[i]]++;
		}

		int n_next = n[x];
		while (d[++n_next] == 0);
		n[x++] = n_next;
		d[n_next]--;
		int y = 0;
		while (x < digits) {
			while(d[y] == 0)	y++;
			n[x++] = y;
			d[y]--;
		}

		for (int i = 0; i < digits; i++) {
			cout << base2ten[n[i]];
		}
		cout << endl;
	}
}
