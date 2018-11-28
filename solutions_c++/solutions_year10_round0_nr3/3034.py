#include <iostream>

using namespace std;

int main() {
	#ifndef ONLINE_JUDGE
		freopen("C-small-attempt1.in", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	unsigned __int16 T;
    
    cin >> T;

	unsigned __int16 R;
	unsigned __int32 k; unsigned __int32 chels;
	unsigned __int64 N;

	unsigned __int16 head;
	unsigned __int32 a[1000];
	unsigned __int64 res = 0;
	int counter;

	for (unsigned __int16 i = 1; i <= T ; i++) {
		res = 0;
		cin >> R >> k >> N;

		for (unsigned __int16 j = 0; j < N; j++)
			cin >> a[j];
		
		head = 0;
		for (unsigned __int16 j = 1; j <= R; j++) {
			chels = 0;
			counter = 1;
			while (((chels + a[head]) <= k) && (counter <= N)) {
				chels += a[head];
				if (head == (N-1))
					head = 0;
				else
					head++;
				counter++;
			}
			res += chels;
		}

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
