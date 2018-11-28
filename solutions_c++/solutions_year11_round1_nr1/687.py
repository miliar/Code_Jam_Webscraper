#include <stdio.h>
int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
int main()
{
	int T;
	scanf("%d", &T);
	for(int z = 0; z < T; z++) {
		int Pd, Pg; long long int N;
		scanf("%lld", &N); scanf("%d %d", &Pd, &Pg);
		int a = Pd, b = 100, c = Pg, d = 100;
		for(int i = 0; i < 25; i++) { 
			while(b % primes[i] == 0 && a % primes[i] == 0) { b /= primes[i]; a /= primes[i]; }
			while(d % primes[i] == 0 && c % primes[i] == 0) { d /= primes[i]; c /= primes[i];}
		}
		//Pd==x/D => DPd=x
		int gamesToday = b; int winsToday = (Pd*gamesToday)/100;
		int losesToday = gamesToday-winsToday;
		bool ok = gamesToday > N ? false : true;
		if(ok) {
			// x=dy
			//(Pg)x>=100winsToday
			//(100-Pg)x>=100losesToday => 100x-Pgx>=losesToday
			//100x>=100winsToday+100losesToday
			int x = gamesToday*d*1000;
			if(!((x*Pg)/100 >= winsToday && (x*(100-Pg))/100 >= losesToday)) {
				ok = false;
			}
		}
		printf("Case #%d: %s\n", z+1, ok == true ? "Possible" : "Broken");
		//Pg==y/G => GPg=y
// 80/100=8/10=4/5; 56/100=28/50=14/25
		
//5kDp=x, 25lPg=y
	}
	return 0;
}


