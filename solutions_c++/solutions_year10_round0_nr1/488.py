#include <iostream>
using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;
	for(int tt=1;tt <=T;++tt) {
		ll N ,K;
		cin >> N >> K;
		ll z = (1 << N);
		cout << "Case #" << tt;
		if(K % z == (1<<N)-1) {
			cout  << ": ON";
		} else {
			cout  << ": OFF";
		}
		cout << endl;
	}
	return 0;
}
