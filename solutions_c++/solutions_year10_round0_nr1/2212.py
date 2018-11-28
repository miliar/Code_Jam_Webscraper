#include<iostream>
#include<cstring>

using namespace std;

int main() {
    int T;
    cin >> T; 
    for (int t = 1; t <= T; ++t) {
	int N, K;
	cin >> N >> K;
	bool power[N], state[N];
	memset(power, false, sizeof(power));
	memset(state, false, sizeof(state));
	power[0] = true;
	for (int snap = 0; snap < K; ++snap) {
	    state[0] = !state[0];
	    for (int i = 1; i < N; ++i) {
		if (power[i]) state[i] = !state[i];
		power[i] = (power[i-1] && state[i-1]);
	    }
	}
	cout << "Case #" << t << ": " << (power[N-1]&&state[N-1]?"ON":"OFF") << endl;
    }
}
