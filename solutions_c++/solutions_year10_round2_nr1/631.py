#include<iostream>
#include<fstream>

using namespace std;


struct elementDirektorijuma {
	char direktorijum[200];
	elementDirektorijuma* sledeci;
};

int main() {
ifstream ulaz("ulaz.txt");
ofstream izlaz("output.txt");
int t, m, n, brojKomandi;
char linija[200];
elementDirektorijuma  *prvi, *poslednji;
	
	ulaz>>t;
	for(int i=0; i<t; i++) {
		ulaz>>n>>m;
		prvi=NULL;
		brojKomandi=0;
		for(int j=0; j<n; j++) {
		
			ulaz>>linija;
		char znak;
		bool pocetakImena=false;
		int pocetak=0, kraj, trenutno=0;
			
			znak=linija[0];
			while(true){
				

				if(znak=='/') {
					if(pocetakImena) {
						kraj=trenutno-1;
						if (prvi==NULL) {
							prvi=poslednji=new elementDirektorijuma;
							for(int k=0; k<kraj-pocetak+1; k++) {
								poslednji->direktorijum[k]=linija[pocetak+k];
							}
							poslednji->direktorijum[kraj-pocetak+1]='\0';
							poslednji->sledeci=NULL;
						}
						else {
							poslednji->sledeci=new elementDirektorijuma;
							poslednji=poslednji->sledeci;
							for(int k=0; k<kraj-pocetak+1; k++) {
								poslednji->direktorijum[k]=linija[pocetak+k];
							}
							poslednji->direktorijum[kraj-pocetak+1]='\0';
							poslednji->sledeci=NULL;
						}
					}
					else {
						pocetakImena=true;
					}
				}
				znak=linija[++trenutno];
				if (znak=='\0'||znak==EOF) { 
					kraj=trenutno;
					if (prvi==NULL) {
						prvi=poslednji=new elementDirektorijuma;
						for(int k=0; k<kraj-pocetak+1; k++) {
							poslednji->direktorijum[k]=linija[pocetak+k];
						}
						poslednji->direktorijum[kraj-pocetak+1]='\0';
						poslednji->sledeci=NULL;
					}
					else {
						poslednji->sledeci=new elementDirektorijuma;
						poslednji=poslednji->sledeci;
						for(int k=0; k<kraj-pocetak+1; k++) {
							poslednji->direktorijum[k]=linija[pocetak+k];
						}
						poslednji->direktorijum[kraj-pocetak+1]='\0';
						poslednji->sledeci=NULL;
					}
					break;
				}
			}
		}
		for(int k=0; k<m; k++) {
			
			ulaz>>linija;
		char znak;
		bool pocetakImena=false;
		int pocetak=0, kraj, trenutno=0;
		char ime[120];
			
			znak=linija[0];
			while(true){
				

				if(znak=='/') {
					if(pocetakImena) {
						kraj=trenutno-1;
						for(int j=0; j<kraj-pocetak+1; j++) {
							ime[j]=linija[pocetak+j];
						}
						ime[kraj-pocetak+1]='\0';
					elementDirektorijuma *tekuci=prvi;

						while(tekuci) {
							if (!strcmp(tekuci->direktorijum, ime)) break;
							tekuci=tekuci->sledeci;
						}
						if (!tekuci) {
							if (prvi==NULL) {
								prvi=poslednji=new elementDirektorijuma;
								strcpy(poslednji->direktorijum, ime);
								poslednji->sledeci=NULL;
								brojKomandi++;
							}
							else {
								poslednji->sledeci=new elementDirektorijuma;
								poslednji=poslednji->sledeci;
								strcpy(poslednji->direktorijum, ime);
								poslednji->sledeci=NULL;
								brojKomandi++;
							}
						}
					}
					else {
						pocetakImena=true;
					}
				}
				znak=linija[++trenutno];
				if (znak=='\0'||znak==EOF) {
					kraj=trenutno;
					for(int j=0; j<kraj-pocetak+1; j++) {
							ime[j]=linija[pocetak+j];
						}
						ime[kraj-pocetak+1]='\0';
					elementDirektorijuma *tekuci=prvi;

						while(tekuci) {
							if (!strcmp(tekuci->direktorijum, ime)) break;
							tekuci=tekuci->sledeci;
						}
						if (!tekuci) {
							if (prvi==NULL) {
								prvi=poslednji=new elementDirektorijuma;
								strcpy(poslednji->direktorijum, ime);
								poslednji->sledeci=NULL;
								brojKomandi++;
							}
							else {
								poslednji->sledeci=new elementDirektorijuma;
								poslednji=poslednji->sledeci;
								strcpy(poslednji->direktorijum, ime);
								poslednji->sledeci=NULL;
								brojKomandi++;
							}
						}
						break;
				}
			};
		}
		
	izlaz<<"Case #"<<i+1<<": "<<brojKomandi<<endl;	
	}
}