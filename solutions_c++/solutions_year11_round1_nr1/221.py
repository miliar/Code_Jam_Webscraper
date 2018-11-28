#include <iostream>
#include <string>
using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd (b, a%b);
}

int lcm(int a, int b) {
	int d = gcd(a,b);
	return (a/d)*b;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		long long N;
		int PD, PG;
		cin >> N >> PD >> PG;
		
		if (N < 0) return 1;
		
		bool pos;
		
		if (PD > 0 && PG == 0) pos = false; //impossible
		else if (PG == 100 && PD < 100) pos = false;
		else if (PD == 0 || PD == 100) pos = true; //play one game and lose/win
		else {
			//PD,PG positive
			//int dG = gcd(100,PG);
			//int dD = gcd(100,PD);
			//int d = gcd(dG,dD);
			
			int D = 100/gcd(100,PD);
			if (D <= N) pos = true;
			else pos = false;
			//cout << PD << endl;
			//cout << D << " " << N << endl;
			
			//int k = dD/d;
			//int D = 100/dD * k;
			
		}
		
		string res;
		if (pos) res = "Possible";
		else res = "Broken";
		
		cout << "Case #" << icase << ": " << res << endl;
	}
	
	return 0;
}
