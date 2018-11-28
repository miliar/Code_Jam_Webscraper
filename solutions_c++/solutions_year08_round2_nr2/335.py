#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int aibe[2000];

bool isPrime(int a) {
	for(int i = 2; i*i <= a; i++) if(a%i == 0) return false;
	return true;
}

vector<int> sets[1001];

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	vi primes;
	for(int i = 2; i <= 1000; i++) if(isPrime(i)) primes.pb(i);
	for(int test = 1; test <= tests; test++) {
		int A, B, P;
		cin >> A >> B >> P;
		memset(aibe, 0, sizeof(aibe));
		for(int i = A; i<=B; i++) aibe[i] = i - A;
		for(int i = A; i <= B; i++) {
			for(int j = i + 1; j <= B; j++) {
				bool taip = false;
				fr(k, primes.sz) if(primes[k] >= P && i%primes[k]==0 && j%primes[k] == 0) taip = true;
		//		if(taip) cout << i << ' ' << j << endl;
				if(taip) {
					int temp = min(aibe[i], aibe[j]);
					int a = aibe[i], b = aibe[j];
					for(int k = A; k <= B; k++) if(aibe[k] == a || aibe[k] == b) aibe[k] = temp;	
				}
			}
		}
		vector<int> s;
		for(int i = A; i<=B; i++) s.pb(aibe[i]);
		sort(s.begin(), s.end());
		s.resize(unique(s.begin(), s.end()) - s.begin());
		cout << "Case #" << test << ": " << s.sz << endl;
	}
	return 0;
}
