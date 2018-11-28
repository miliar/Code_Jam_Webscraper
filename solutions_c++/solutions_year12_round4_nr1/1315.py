#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <map>
#include <vector>
#include <set>

using namespace std;

long long reach(int N, long long* d, long long* I, long long* f, int sn, int n) {
	if (f[sn*N+n] != 0) return f[sn*N+n];
	long long sw = d[n]+min(d[n]-d[sn], I[n]);
	long long max = sw;
	for (int i=n+1; i<=N; i++) {
		if (sw >= d[i]) {
			long long p = reach(N, d, I, f, n, i);
			f[n*N+i] = p;
			//cout << n << " " << i << " " << p << endl;
			if (p > max) max = p;
		}
		else break;
	}
	f[sn*N+n] = max;
	//cout << sn << " " << n << " " << max << endl;
	return max;
}

int main(int argc, char* argv[]) {
	ifstream fff;
	fff.open(argv[1]);
	int T;
	fff >> T;
	for (int ttt=0; ttt<T; ttt++) {
		cout << "Case #" << ttt+1 << ": ";
		int N;
		fff >> N;
		long long* d = new long long [N+1];
		long long* I = new long long [N+1];
		d[0] = I[0] = 0;
		for (int i=1; i<=N; i++) {
			fff >> d[i] >> I[i];
			//cout << d[i] << " " << I[i] << endl;
		}
		long long D;
		fff >> D;
		
		long long* f = new long long [(N+1)*(N+1)];
		memset(f, 0, (N+1)*(N+1)*sizeof(long long));
		
		if (reach(N, d, I, f, 0, 1) >= D) cout << "YES";
		else cout << "NO";
		cout << endl;
		
		delete[] d;
		delete[] I;
		delete[] f;
	}	
	fff.close();
}
