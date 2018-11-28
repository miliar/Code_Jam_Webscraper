#include <iostream>
#include <cstdio>
#include <bitset>

using namespace std;

int main () {
	int T, R, k, N;
	int g[1000]; //g_i
	int n[1000]; //num on ride
	int go[1000]; //goto index (ie sum)
	cin >> T;
	for (int i=0; i<T; i++) {
		cin >> R >> k >> N;
		for (int j = 0; j < N; j++)
			cin >> g[j];
		int num = 0;
		int sum = 0;
		for (int j = 0; j<N; j++) {
			if (j>0) {
				sum-=g[j-1];
				num--;
			}
			while (num<N && g[(j+num)%N]+sum <= k) {
				sum+=g[(j+num)%N];
				num++;
			}
			n[j] = sum;
			go[j] = (j+num)%N;
		}
/*
		for (int j=0; j<N; j++)
			cout << n[j] << " ";
		cout << endl;
		for (int j=0; j<N; j++)
			cout << go[j] << " ";
		cout << endl;
*/
		long euro = 0;
		long index = 0;
		long r = R;
		long loop_sum = 0;
		long loop_len = 0;
		while (r) {
			if (index==0 && r<R && loop_len<r) {
				loop_sum = euro;
				loop_len = R-r;
				euro += loop_sum * (r/loop_len);
				r %= loop_len;
				continue;
			}
			euro += n[index];
			index = go[index];
			r--;
		}


		cout << "Case #" << i+1 << ": " << euro;
		cout << endl;
	}

	return 0;
}
