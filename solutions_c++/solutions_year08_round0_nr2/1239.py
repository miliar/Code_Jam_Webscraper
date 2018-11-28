#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
using namespace std;

int str2min(string s){
	int time;
	stringstream strs;

	strs << s;

	time = (strs.get()-'0')*600 + (strs.get()-'0')*60;
	strs.get(); // ':' ueberlesen
	time += (strs.get()-'0')*10 + strs.get()-'0';

	return time;
}

int main(void){
	ifstream in;    // Input File
	ofstream out;   // Output File
	int n,na,nb,t;  // values
	string r;
	int a, b;
	list<int> a_dep, a_arr, b_dep, b_arr;
    list<int>::iterator it1;
	list<int>::iterator it2;
	list<int>::iterator it;

	// Dateien oeffnen
	in.open("C:/Dokumente und Einstellungen/Erler/Desktop/B-large.in");//-attempt2
    out.open("C:/Dokumente und Einstellungen/Erler/Desktop/B-large.out");


	// Daten lesen
	in >> n;

	for(int j=0; j<n; ++j){
		a = -1;
		b = -1;
	
		// Turnaroundtime lesen
		in >> t;

		// NA, NB lesen
		in >> na >> nb;
		getline(in,r); // zeilenende ueberlesen

		//Zeitplan NA lesen
		for (int i=0; i<(2*na); ++i){
			in >> skipws >> r;
			//cout << r << " : "<< str2min(r) << " "; // liefert Zeit in Minuten als int
			//if((i+1)%2==0)cout << "\n";

			if((i+1)%2==1) a_dep.push_back( str2min(r) );
			else {
				b_arr.push_back( str2min(r) + t );
			}
		}

		//Zeitplan NB lesen
		for (int i=0; i<(2*nb); ++i){
			in >> skipws >> r;

			if((i+1)%2==1)b_dep.push_back( str2min(r) );
			else {
				a_arr.push_back( str2min(r) + t );
			}
		}
		
		// sortieren
		a_dep.sort();
		a_arr.sort();
		b_dep.sort();
		a_arr.sort();

		// a berechnen
		for(it1=a_arr.begin(); it1!=a_arr.end(); ++it1){
			for(it2=a_dep.begin(); it2!=a_dep.end(); ++it2){
				if ( *it1 <= *it2 /*&& a_dep.size()>0 && it2!=a_dep.begin()*/ ){
					it = it2;
					if(it2!=a_dep.begin()){ 
						--it2;
						a_dep.erase(it);
					}
					else if(a_dep.size()>1){
						a_dep.pop_front();
					}
					else if(a_dep.size()==1){
						a=0; 
						a_dep.clear(); 
						break;
						break;
					}
					break;
				}
			}
		}
		if(a!=0)a = a_dep.size();

		// b berechnen
		for(it1=b_arr.begin(); it1!=b_arr.end(); ++it1){
			for(it2=b_dep.begin(); it2!=b_dep.end(); ++it2){
				if ( *it1 <= *it2 /*&& a_dep.size()>0 && it2!=b_dep.begin()*/ ){
					it = it2;
					if(it2!=b_dep.begin()){
						--it2;
						b_dep.erase(it);
					}
					else if(b_dep.size()>1){b_dep.pop_front();}
					else if(b_dep.size()==1){b=0; b_dep.clear(); break;break;}	
					break;
				}
			}
		}
		if(b!=0)b = b_dep.size();


		// Daten schreiben
		//cout	<< "Case #"<< j+1 << ": "<< a << " " << b << "\n"; 
		out	<< "Case #"<< j+1 << ": "<< a << " " << b << "\n"; 
		a_dep.clear();
		a_arr.clear(); 
		b_dep.clear();
		b_arr.clear();

	}
	// Dateien schliessen
	in.close();
	out.close();

return 0;
}