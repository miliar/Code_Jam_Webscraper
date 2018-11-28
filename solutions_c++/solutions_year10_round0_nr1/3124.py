#include <iostream>

using namespace std;

unsigned __int64 CycleTimes(unsigned __int8 N) {
	unsigned __int64 res = 0;

	for (unsigned __int8 i = 1; i <= N; i++)
		res = (res + res + 1);
	return res;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("A-large.in", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

    unsigned __int16 T;
    unsigned __int16 N;
    unsigned __int32 K;
    unsigned __int64 CT;
    
    cin >> T;
    
    for (unsigned __int16 i = 1; i <= T ; i++) {
		cin >> N >> K;
        
		if (K%2 == 0)
			cout << "Case #" << i << ": OFF" << endl;
		else {
            CT = CycleTimes(N);
            
            if ((K%(CT+1) == CT))// || ((K%(CT+1) == 0)))
                cout << "Case #" << i << ": ON" << endl;
            else
                cout << "Case #" << i << ": OFF" << endl;
        }
    }

	return 0;
}

