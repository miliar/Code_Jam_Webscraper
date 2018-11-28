#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int main(void){
	ifstream in;    // Input File
	ofstream out;   // Output File
	string in_path; // Path Input File
	int n,s,q;      // values
	string r;
	int erg, z;
	multimap<string,int> qu;

	//cin >> in_path;  
	// Dateien oeffnen
	//in.open(in_path.c_str());
	in.open("C:/Dokumente und Einstellungen/Erler/Desktop/A-large.in");
    out.open("C:/Dokumente und Einstellungen/Erler/Desktop/A-large.out");


	// Daten lesen
	in >> n;

	for(int j=0; j<n; ++j){
		erg = 0;
		z = 0;
		qu.clear();
	
		// Searchengines lesen
		in >> s;
		getline(in,r);
		for (int i=0; i<s; ++i){
			getline(in,r);
		}

		// Querry lesen 
		in >> q;
		getline(in,r);
		for (int i=0; i<q; ++i){
			getline(in,r);
			if(qu.find(r)==qu.end()){
				++z;
				if(qu.size()==s-1){ 
					++erg;
					qu.clear();
				}
				qu.insert(pair<string,int>(r,z));
			}
		}

		// Daten schreiben
		out	<< "Case #"<< j+1 << ": "<< erg << "\n"; 

	}
	
	// Dateien schliessen
	in.close();
	out.close();


return 0;
}