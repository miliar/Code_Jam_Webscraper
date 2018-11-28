#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int TS;
	cin >> TS;
	for(int ts=1; ts<=TS; ts++) {
		long long N,PD,PG;
		cin >> N >> PD >> PG;
		bool possible = true;
		if(PG==100 && PD!=100) possible=false;
		else if(PG==0 && PD!=0) possible=false;
		else if(PD==0) possible=true;
		else {
			long long D = 100/__gcd(100LL,PD);
			possible = (D<=N);
		}
		cout << "Case #" << ts << ": " << (possible?"Possible":"Broken") << endl;
	}
}
