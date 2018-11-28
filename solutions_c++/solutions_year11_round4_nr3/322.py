#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

int T;
int primes[1005];
int np[1005];
int kol = 0;

void erat(){
	np[0] = np[1] = true;
	for (int i=2; i<1005; i++){
		if (!np[i]){
			primes[kol++] = i;
			for (int j=i*i; j<1005; j += i){
				np[j] = true;
			}
		}
	}
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	erat();
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		int n;
		cin >> n;
		if (n == 1){
			cout << 0 << endl;
			continue;
		}
		int mn = 0, mx = 1;
		for (int i=0; i<kol; i++){
			if (primes[i] <= n){
				int tec = primes[i];
				mn++;
				while (tec <= n){
					tec *= primes[i];
					mx++;
				}
			}
		}
		cout << mx - mn << endl;
	}
	return 0;
}