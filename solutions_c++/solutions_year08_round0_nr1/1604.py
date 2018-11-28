#include <stdio.h>
#include <stdlib.h>

int ileTestow = 0;
int ilePrzeg = 0;
int ileZap = 0;	
char linia[123];
long przeg[123], zapyt[1234];

long hash(char *tekst) {
	long pom = 1;
	long wartosc = 0;

	while (*tekst) 
		wartosc += wartosc ^ (*tekst++ ^ pom++);
	return(wartosc);
}

int wynik() {
	int wyn = 0;
//	long ost = -1;
//	long naj = -1;
	int aktPoz = 0;
	int tmpPoz = -1;
	int najwyzPoz = -1;
	
	while (1) {
	for (int i = 0; i < ilePrzeg; ++i) {
		tmpPoz = -1;
		for (int j = aktPoz; j < ileZap; ++j)
			if (przeg[i] == zapyt[j]) {
				tmpPoz = j;
				break;
			} 
			if (tmpPoz == -1) return(wyn);
			if (tmpPoz > najwyzPoz) 
				najwyzPoz = tmpPoz;
	}
	
	++wyn;
	aktPoz = najwyzPoz;
	} // while true
	return(wyn);
}

int main() {
	
//	scanf("%d",&ileTestow);
	gets(linia);
	ileTestow = atoi(linia);
	
	for (int i = 0; i < ileTestow; ++i) {
//		scanf("%d",&ilePrzeg);
		gets(linia);
		ilePrzeg = atoi(linia);
		for (int j = 0; j < ilePrzeg; ++j) {
			gets(linia);
//			scanf("%s",linia);
//		printf("przeg: %s\n",linia);
//			printf("%s <=> %ld\n",linia,hash(linia));
			przeg[j] = hash(linia);
		}
	
	
//		scanf("%d",&ileZap);
		gets(linia);
		ileZap = atoi(linia);
		for (int j = 0; j < ileZap; ++j) {
//			scanf("%s",linia);
			gets(linia);
			zapyt[j] = hash(linia);	
//		printf("zap: %s\n",linia);
		}
		
		printf("Case #%d: %d\n",i+1,wynik());
		
	} //for ileTestow
	
	
	return(0);	
}
