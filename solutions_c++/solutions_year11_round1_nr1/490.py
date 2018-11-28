#include <iostream>

using namespace std;


int T;
long long n,n1,n2;

long long gcd(long long a, long long b){
//cerr << a << " " << b << endl;
	if (a < b) return gcd(b, a);
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main(){
	cin >> T;
	for (int _i = 0; _i < T; ++_i){
		cout << "Case #" << _i + 1 << ": ";
		cin >> n >> n1 >> n2;
		int w1 = n1, l1 = 100 - n1;
		int d = gcd(w1, l1);
		w1 /= d;
		l1 /= d;
	
		int w2 = n2, l2 = 100 - n2;
		d = gcd(w2, l2);
		w2 /= d;
		l2 /= d;
		if (l2 == 0){
			if (l1 == 0){
				cout << "Possible\n";
			}
			else{
				cout << "Broken\n";
			}
			continue;
		}
		if (w2 == 0){
			if (w1 == 0){
				cout << "Possible\n";
			}
			else{
				cout << "Broken\n";
			}
			continue;
		}
		if (w1 + l1 <= n) cout << "Possible\n";
		else cout << "Broken\n";
	}
}