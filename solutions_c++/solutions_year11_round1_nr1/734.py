#include<iostream>
using namespace std;

int gcd(int n, int m) {
	if(m==0) return n;
	else return gcd(m, n%m);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T; cin>>T;
	for (int i=1; i<=T; i++) {
		bool flag=false;
		int PD, PG; long long N; cin>>N>>PD>>PG;
		if(PG==0 || PG==100) {
			if(PD==PG) flag=true;
		} else {
			if(100/gcd(PD,100)<=N) flag=true;
		}
	
		cout << "Case #" << i << ": ";
		if(flag) cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}	
	return 0;
}
