#include <iostream>

using namespace std;

int gcd(int a, int b){
	return a%b ? gcd(b,a%b) : b;
}

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		int N, PD, PG; cin >> N >> PD >> PG;
		if(PD == 0){
			if(PG == 100) printf("Case #%d: Broken\n", test);
			else          printf("Case #%d: Possible\n", test);
		} else if(PD == 100){
			if(PG == 0) printf("Case #%d: Broken\n", test);
			else        printf("Case #%d: Possible\n", test);
		}
		else if(PG == 0){
			if(PD != 0) printf("Case #%d: Broken\n", test);
			else        printf("Case #%d: Possible\n", test);
		}
		else if(PG == 100){
			if(PD != 100) printf("Case #%d: Broken\n", test);
			else          printf("Case #%d: Possible\n", test);
		}
		else {
			if(N < 100/gcd(100,PD)) printf("Case #%d: Broken\n", test);
			else                    printf("Case #%d: Possible\n", test);
		}
	}
}