#include<cstdio>

long grupy[1123];


int main(){
	long ilosc, przejazdy, pojemnosc, ilosc_grup, poz, pocz_poz, zaladowane;
	long long zysk;
	scanf("%ld", &ilosc);

	for(long i = 1; i <= ilosc; i++){
		scanf("%ld %ld %ld", &przejazdy, &pojemnosc, &ilosc_grup);
		for(long j = 0; j < ilosc_grup; j++)
			scanf("%ld", &grupy[j]);
		grupy[ilosc_grup] = 0; // na wszelki wypadek
		zysk = 0;
		poz = 0;
		while(przejazdy--){
			zaladowane = grupy[poz];
			pocz_poz = poz;
			while(zaladowane <= pojemnosc){
				poz = (poz + 1) % ilosc_grup;
				zaladowane += grupy[poz];
				if(pocz_poz == poz)
					break;
			}
			zaladowane -= grupy[poz];
			zysk += zaladowane;
		}
		printf("Case #%ld: %lld\n", i, zysk);
	}


	return 0;
}
