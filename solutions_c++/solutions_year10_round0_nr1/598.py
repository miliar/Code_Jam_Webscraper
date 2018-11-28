#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		int N,K;
		cin >> N >> K;
		int mask=(1<<N)-1;
		cout << "Case #" << t << ": " << ((mask&K)==mask?"ON":"OFF") << endl;
	}
}
