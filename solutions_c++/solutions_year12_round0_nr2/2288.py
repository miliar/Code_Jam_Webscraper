#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int T, Case = 0;
int main() {
	cin >> T;
	while(T--) {
        ++Case;
        int Ans = 0, S, N, p;

        cin >> N >> S >> p;

        int Normal = 0, Surprised = 0;

        for(int i = 0; i < N; ++i) {
            int t;
            cin >> t;

            t -= p;
            if(t < 0) continue;
            if(t - (p-1) >= p-1) {
                Normal++;
            } else if(t - (p-2) >= p-2) {
                Surprised++;
            }
        }

        if(Surprised > S) Surprised = S;
        Ans = Normal + Surprised;

        cout << "Case #" << Case << ": " 
             << Ans << endl;
	}
	return 0;
}
