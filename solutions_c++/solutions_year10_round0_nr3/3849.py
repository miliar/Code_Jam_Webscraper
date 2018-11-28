#include <iostream>
#include <vector>
using namespace std;


int main () {
	int t, vegades, numGrups, voltes, posicio, cont;
        long long int suma, gent;
	cin >> t;
	vector<int> grup;
	for(int tt=0; tt<t; tt++) {
		suma = voltes = posicio = cont = 0;
		cin >> vegades >> gent >> numGrups;
		grup = vector<int> (numGrups);
		for(int i=0; i<numGrups; i++)
			cin >> grup[i];
		for(int r=0; r<vegades; r++) {
			while(suma + grup[posicio] <= gent and ++cont <=numGrups) {
				suma += grup[posicio];
				posicio++;
				if(posicio == numGrups) {
					voltes++;
					posicio = 0;
				}
			}
			suma = cont = 0;
			cout << "Vegada: " << r << ", poscicio: " << posicio << " i " << voltes << " voltes" << endl;
		}
		
		suma = gent = 0;
		for(int i=0; i<numGrups; i++)
			suma += grup[i];
		for(int i=0; i<posicio; i++)
			gent += grup[i];
		cout << "Case #" << tt+1 << ": " << suma*voltes+gent << endl;
	}
}
