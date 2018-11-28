#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int count(int n) {
	n = ((n>>1)&0x55555555) + (n&0x55555555);
	n = ((n>>2)&0x33333333) + (n&0x33333333);
	n = ((n>>4)&0x0F0F0F0F) + (n&0x0F0F0F0F);
	n = ((n>>8)&0x00FF00FF) + (n&0x00FF00FF);
	return ((n>>16)&0x0000FFFF) + (n&0x0000FFFF);
}

int func(int n) {
	int cnt = 0;
	for (int i = 0; i < 1<<(n-2); ++ i) {
		for (int j = 0; j < n-1; ++ j) {
		}
		bool f = true;
		int m = n;
		for (;;) {
			m = count(i&((1<<(m-2))-1))+1;
			if (m == 1) break;
			if (((i>>(m-2))&1)==0) { f=false; break; }
		}
		if (f) ++ cnt;
	}
	return cnt % 100003;
}

int main() {
	string buf;
	getline(cin, buf);
	int T = atoi(buf.c_str());
	for (int i = 1; i <= T; ++ i) {
		int n;
		cin >> n;
		cout << "Case #" << i << ": " << func(n) << endl;
	}
}
