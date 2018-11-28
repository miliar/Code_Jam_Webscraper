#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define REP(i, n) for (long long i = 0; i < n; i++)
#define FOR(i, a, b) for (long long i = a; i <= b; i++)
#define FORD(i, a, b) for (long long i = a; i >= b; i--)

long long sl[1111];
long long memo[1111];
long long income[1111];
long long r, capa, n;
long long res;

void process() {
	if (r == 0) return;
	
	FOR(i, 1, n) memo[i] = -1;
	res = 0;
	
	long long f1, f2;
	
	long long first = 1;
	for (long long i = 1; ; i++) {
		
		if (memo[first] == -1) memo[first] = i;
		else {
			f1 = memo[first];
			f2 = i;
			break;
		}
		
//		cout << "Round " << i << " " << first << endl;
		
		long long j = first;
		long long cnt = 0;
		while (true) {
			if (cnt + sl[j] <= capa) {
				cnt += sl[j];
				j++;
				if (j == n + 1) j = 1;
				if (j == first) break;
			} else break;
		}	
		first = j;
		income[i] = cnt;
	}
	
//	cout << f1 << " " << f2 << endl;
	
	for (long long i = 1; i < f1; i++) {
		res += income[i];
		if (i == r) return;
	}
	long long lap = 0;
	for (long long i = f1; i < f2; i++) {
		lap += income[i];
		if (i == r) {
			res += lap;
			return;
		}
	}
//	cout << res << endl;
//	cout << lap << endl;
	for (long long i = r; i >= f2; i--) {
		if ((i - f1 + 1) % (f2 - f1) == 0) {
			long long v = (i - f1 + 1) / (f2 - f1);
//			cout << i << " " << v << endl;
			res += v * lap;
			long long x = f1;
			for (long long j = i + 1; j <= r; j++) {
				res += income[x++];
			}
			break;
		}
	}
}

int main() {
	freopen("c-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	long long test;
	cin >> test;	
	FOR(i, 1, test) {
		cin >> r >> capa >> n;
		FOR(j, 1, n) cin >> sl[j];
		
		process();
		
		cout << "Case #" << i << ": " << res << endl;
	}
	
	
	return 0;
}
