#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++) {
		int N;
		cin >> N;
		int cnt=0;
		for(int i=1; i<=N; i++) {
			int x;
			cin >> x;
			cnt += (x!=i);
		}
		cout << "Case #" << tc << ": " << cnt << endl;
	}
}
