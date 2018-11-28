#include <cstdio>
using namespace std;

int jeden(){
	int a,b,c; scanf("%d%d%d", &a, &b, &c);
	
	int zlicz = 1;
	long long x = a;
	while(x*c<b){
		x*=c;
		zlicz++;
	}
	int beta = 1;
	int wynik = 0;
	while(beta<zlicz) {beta*=2; wynik++;}
	return wynik;
}

main(){
	int c; scanf("%d", &c);
	for(int i = 1; i<=c; i++) printf("Case #%d: %d\n", i, jeden());
}
