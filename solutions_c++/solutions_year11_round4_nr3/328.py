#include <iostream>
#include <vector>
using namespace std;

vector<bool> isPrime(3000000, true);
vector<int> primes;
void buildprimes() {
	for (int i=2;i<3000000;i++) {
		if (isPrime[i]) {
			primes.push_back(i);
			for (int j=i*2;j<3000000;j+=i)
				isPrime[j] = false;
		}
	}
}

int getbest(long long n) {
	if (n==1) return 1;
	long long a = 0;
	vector<long long> need;
	for (int i=0;i<primes.size();i++) {
		long long v = 1;
		while (v*primes[i] <= n)
			v*=primes[i];
		if (v>1) need.push_back(v);
	}
	sort(need.begin(),need.end());
	for (int i=need.size()-1;i>=0;i--) {
		long long m = need[i];
		if (m==1) continue;
		for (int j=i-1;j>=0;j--) {
			if (need[j]*m <= n) {
				m*=need[j];
				need[j] = 1;
			}
		}
		a++;
	}
	return a;
}

int getworst(long long n) {
	int a = 0;
	for (int i=0;i<primes.size();i++) {
		long long v = primes[i];
		while (v <= n) {
			a++;
			v*=primes[i];
		}
	}
	return a+1;
}
void tc(int i) {
	long long n;
	cin >> n;
	int best = getbest(n);
	int worst = getworst(n);
	cout << "Case #" << i << ": " << (worst - best) << endl;
}
int main() {
	buildprimes();
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
		tc(i);

}