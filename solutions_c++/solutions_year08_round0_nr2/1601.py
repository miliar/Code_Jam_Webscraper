#include <stdio.h>
#include <stdlib.h>
#include <list>
#include <algorithm>

using namespace std;
enum TypWyc {zAdoB, zBdoA};

class Wycieczka {
	public:
		int pocz;
		int kon;
		TypWyc wyc;
		
		Wycieczka(): pocz(-1), kon(-1), wyc(zAdoB) {}
		
		Wycieczka(int pgodz, int pmin, int kgodz, int kmin, int czas, 
		TypWyc w):
			pocz(pgodz*60+pmin), kon(kgodz*60+kmin+czas), wyc(w) {}
		bool operator < (const Wycieczka &w) const {
//			return(kon < w.kon);
//TESTY
			return(pocz < w.pocz);
		}	

		bool jestOk(const Wycieczka &w) {
			if (wyc == w.wyc) return(false);
			return( kon <= w.pocz);	
		}
		void wypisz() {
			printf("(%d-%d",pocz,kon);
			if (wyc == zAdoB) printf(" zAdoB)");
			else printf(" zBdoA)");
		}
};

bool testuj(const Wycieczka &x, const Wycieczka &y) {
	if (x.wyc == y.wyc) return(false);
	return(x.kon <= y.pocz);	
}

class RekWyc {
	public:
		bool byl;
		Wycieczka wyc;	
	RekWyc(): byl(false) {}
	RekWyc(Wycieczka w): wyc(w), byl(false) {} 
	bool operator < (const RekWyc &r) const {
		return(wyc < r.wyc);
	}	
	void wypisz() {
		printf("[%d ",byl); wyc.wypisz(); printf("]");	
	}
};

RekWyc czasy[300];

class Wynik {
	public:
		int zadob;
		int zbdoa;
		Wynik(): zadob(0),zbdoa(0) {}
		Wynik(int a, int b): zadob(a), zbdoa(b) {}
};

Wynik rozwal(int ile) {
	Wynik wyn;
	int ileZost = ile;
	Wycieczka aktWyc;

	while (ileZost > 0) {
		int poz = 0;
//		printf("Sciezki:\n");
		while (poz < ile) {
			if (!czasy[poz].byl) {
				aktWyc = czasy[poz].wyc;
//aktWyc.wypisz();				
				(aktWyc.wyc == zAdoB) ? ++wyn.zadob : ++wyn.zbdoa;
				czasy[poz].byl = true;
				--ileZost;
				++poz;
				break;
			}	
			++poz;
		}
		// szukamy	
		for (int i = poz; i < ile; ++i) {
			if (!czasy[i].byl && aktWyc.jestOk(czasy[i].wyc)) {
				czasy[i].byl = true;
				aktWyc = czasy[i].wyc;
//aktWyc.wypisz();
				--ileZost;	
			}
		}
//printf("\n");		
	}

	return(wyn);	
}

int main() {
	
	int ileTestow;
	int czas;
	int ileZA, ileZB;
	char linia[300];
		
//	scanf("%d\n",&ileTestow);
	gets(linia);
	ileTestow = atoi(linia);
	for (int t = 0; t < ileTestow; ++t) {
//		scanf("%d\n",&czas);
		gets(linia);
		czas = atoi(linia);
		gets(linia);
//		scanf("%d %d\n",&ileZA,&ileZB);
//		printf("ileZA i ileZB = %s\n",linia);
		sscanf(linia,"%d %d\n",&ileZA,&ileZB);

		int ileCzasow = ileZA + ileZB;
		int poz = 0;
		int gpocz,minpocz,gkon,minkon;
		for (int a = 0; a < ileZA; ++a) {
			gets(linia);
//		printf("czasyZA: %s\n",linia);			
//			scanf("%d:%d %d:%d\n",&gpocz,&minpocz,&gkon,&minkon);
			sscanf(linia,"%d:%d %d:%d\n",&gpocz,&minpocz,&gkon,&minkon);
			czasy[poz++] = RekWyc(Wycieczka(gpocz,minpocz,gkon,minkon,czas,zAdoB));
		}
		for (int b = 0; b < ileZB; ++b) {
			gets(linia);
//		printf("czasyZB: %s\n",linia);			
//			scanf("%d:%d %d:%d\n",&gpocz,&minpocz,&gkon,&minkon);
			sscanf(linia,"%d:%d %d:%d\n",&gpocz,&minpocz,&gkon,&minkon);
			czasy[poz++] = RekWyc(Wycieczka(gpocz,minpocz,gkon,minkon,czas,zBdoA));
		}
		
//		printf("ileZA: %d,  ileZB %d\n",ileZA,ileZB);

		if (ileZA == 0) {
			printf("Case #%d: %d %d\n",t+1,0,ileZB);
			continue;	
		}	
		else
		if (ileZB == 0) {
			printf("Case #%d: %d %d\n",t+1,ileZA,0);
			continue;	
		}

		sort(czasy,czasy+ileCzasow);
/*		
		for (int i = 0; i < ileCzasow; ++i)
			czasy[i].wypisz();	
		printf("\n");
*/		
		Wynik wyn = rozwal(ileCzasow);
		printf("Case #%d: %d %d\n",t+1,wyn.zadob,wyn.zbdoa);
	}

	return(0);
}

