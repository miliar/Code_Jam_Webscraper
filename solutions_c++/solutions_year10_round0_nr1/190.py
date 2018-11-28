#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)

int main(void) {
	int T;
	cin >> T;
	fu(t,0,T) {
		int N,K;
		cin >> N >> K;
		bool on = (K+1)%(1<<N) == 0;
		cout << "Case #" << t+1 << ": " << (on ? "ON" : "OFF") << endl;
	}
}
