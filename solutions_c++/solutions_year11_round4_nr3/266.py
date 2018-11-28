#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int main() {
	int T;

	cin >> T;
	vector<long long> primes;
	for (int t=1;t<=T;t++) {


		cout << "Case #" << t << ": ";
		long long N;
		cin >> N;
		int pindex=0;
		long long spread=N>1;
		for (long long p=2;p*p<=N;p++) {
			// is this prime??
			if (pindex<primes.size()) {
				if (primes[pindex]!=p) {
					continue;
				}
				else pindex++;
			}
			else {
				bool prime=true;
				for (int i=0;i<primes.size();i++) {
					if (p%primes[i]==0) {prime=false;break;}
					if (primes[i]*primes[i]>p) break;
				}
				if (!prime) continue;
				primes.push_back(p);
				pindex++;
			}
			//cout << "prime " << p << endl;
			// what is the maximum p^x<=N
			long long P=p*p;
			while (P<=N) {
				spread++;
				P*=p;
			}
		}
		cout << spread;
		cout << endl;
	}
	return 0;
}