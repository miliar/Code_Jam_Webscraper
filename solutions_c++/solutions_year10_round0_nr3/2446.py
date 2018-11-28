#include<fstream>
#include<iostream>

using namespace std;


int main() {
ifstream ulaz("C-small-attempt1.in");
ofstream izlaz("output.txt");
unsigned _int64 zarada, r, k, red[1000], preostaloMesta;
int t, sledeci, n, preostaloGrupa;
	
	ulaz>>t;
	for(int i=0; i<t; i++){
		ulaz>>r>>k>>n;
		zarada=0;
		sledeci=0;
		for(int i=0; i<n; i++) ulaz>>red[i];
		for(unsigned _int64 j=0; j<r; j++){
		bool imaMesta=true;
		bool imaGrupa=true;
			
			preostaloGrupa=n;
			preostaloMesta=k;
			while(imaMesta&&imaGrupa){
				if(red[sledeci]<=preostaloMesta){
					preostaloMesta-=red[sledeci];
					zarada+=red[sledeci];
					sledeci=(sledeci+1)%n;
					if(--preostaloGrupa==0) imaGrupa=false;
				}
				else imaMesta=false;
			}
		}
		izlaz<<"Case #"<<i+1<<": "<<zarada<<'\n';
	}
	ulaz.close();
	izlaz.close();
}
