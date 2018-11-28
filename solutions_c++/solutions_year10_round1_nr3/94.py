#include <iostream>
#include <cmath>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		int A1,A2,B1,B2;
		long long ret=0;
		cin >> A1 >> A2 >> B1 >> B2;
		for(int A=A1; A<=A2; A++) {
			const long double five = 5;
			int y = A*(1+sqrt(five))/2+1;
			int x = A*(sqrt(five)-1)/2;
			if(x>=B1) ret += (min(x,B2)-B1)+1;
			if(y<=B2) ret += (B2-max(B1,y))+1;
		}
		cout << "Case #" << tc << ": " << ret << endl;
	}
}
