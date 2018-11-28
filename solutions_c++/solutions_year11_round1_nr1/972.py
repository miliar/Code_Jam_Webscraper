#include <iostream>

using namespace std;
typedef long long ll;

ll gcd(ll n, ll m){
	if(n < m){ return gcd(m, n); }
	if(m == 0){ return n; }
	return gcd(m, n % m);
}

int main(){
	int T;
	cin >> T;
	for(int caseNum = 1; caseNum <= T; ++caseNum){
		ll n;
		int pd, pg;
		cin >> n >> pd >> pg;
		bool answer = false;
/*		if(pd == 0){
			answer = (pg != 100);
		}else{
			ll ds = pd / gcd(100, pd);
			ll d = ds * 100 / pd;
		cout << ds << endl;
			if(d <= n && !(pd != 100 && pg == 100)){ answer = true; }
		}*/
		if(pd != 100 && pg == 100){
		}else if(pd != 0 && pg == 0){
		}else if(pd == 0){
			answer = true;
		}else if(n >= 100){
			answer = true;
		}else{
			for(int d = 1; d <= n; ++d){
				if(d * pd % 100 == 0){
					answer = true;
					break;
				}
			}
		}
		cout << "Case #" << caseNum << ": " << (answer ? "Possible" : "Broken") << endl;
	}
	return 0;
}
