#include <iostream>
#include <fstream>

using namespace std;

int N,L,H;
const int maxn = 128;
int notes[maxn];

void input() {
	cin >> N >> L >> H;
	for (int i=0;i<N;i++)
		cin >> notes[i];
}

bool check(int x) {
	for (int i=0;i<N;i++)
		if (!(((notes[i] % x) == 0) || ((x % notes[i]) == 0))) return false;
	return true;
}

void solve() {
	for (int i=L;i<=H;i++)
		if (check(i)) {
			cout << i;
			return;
		}
	cout << "NO";
}

int main() {
	
	int t,T;
	
	cin >> T;
	
	for (int t=1;t<=T;t++) {
		input();
		cout << "Case #" << t << ": ";
		solve();
		cout << "\n";
	}
	
	return 0;

}