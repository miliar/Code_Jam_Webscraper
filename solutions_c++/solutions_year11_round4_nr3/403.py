#include <iostream>

using namespace std;

int phash[1000000] = {0};
int prime[1000000];
int pcount = 0;

int main (int argc, char const *argv[])
{
	int current = 2;
	phash[0] = phash[1] = phash[2] = 1;
	while (current < 1000000) {
		prime[pcount++] = current;
		for(int i = 1; i * current < 1000000; i++) {
			phash[i*current] = 1;
		}
		while (current < 1000000 && phash[current]) current++;
	}
	int t;
	cin >> t;
	for(int index = 1; index <= t; index++) {
		long long n;
		cin >> n;
		if (n == 1) {
			cout << "Case #" << index << ": " << 0 << endl;
			continue;
		}
		long long ans = 0;
		for(long long i = 0; i < pcount; i++) {
			long long k = prime[i];
			long long j;
			for(j = 0;;j++) {
				k *= prime[i];
				if (k > n) break;
			}
			if (j == 0) break;
			ans += j;
		}
		cout << "Case #" << index << ": " << ans+1 << endl;
	}
	return 0;
}