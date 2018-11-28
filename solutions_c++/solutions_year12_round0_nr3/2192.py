//============================================================================
// Name        : CodeJam.cpp
// Author      : Daniel Rubio
// Version     : 1.0
// Copyright   : FreeWare
// Description : CodeJam 2011 - Qualification 1
//============================================================================

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <sstream>
using namespace std;

string stringmax;
int maxrot;

string convertInt(int number){
   stringstream ss;
   ss << number;
   return ss.str();
}

string desplaza(string numb,int rot){
	string salida = numb;
	int pos;

	for(int i=0;i<maxrot;i++){
		pos = (rot + i)%maxrot;
		salida[i] = numb[pos];
	}

	return salida;
}

int main(){
	freopen("d:\\Downloads\\C-large.in", "rt", stdin);
	freopen("d:\\Downloads\\C-large.out", "wt", stdout);

	//declaramos variables
	int T;
	int min;
	int max;
	int res;
	bool ok;
	string numeroencontrado;
	string stringnumber;
	vector<string> numeros;
	bool found;


	//repeticiones
	cin >> T ;
	for(int r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";

		res = 0;

		cin >> min >> max;
		stringmax = convertInt(max);
		maxrot = stringmax.length();

		//cerr << endl << "{" << stringmax << "}"<< endl;
		for(int i=min;i<max;i++){
			stringnumber = convertInt(i);
			//cerr << endl << "[" << stringnumber << "]";
			numeros.clear();
			for(int j=1;j<maxrot;j++){
				ok = false;

				//comparamos si es menor
				for(int k=0;k<maxrot;k++){
					if(stringnumber[(j+k)%maxrot] < stringnumber[k]){
						ok = false;
						//cerr << "x";
						break;
					}else if(stringnumber[(j+k)%maxrot] > stringnumber[k]){
						ok = true;
						//cerr << "_";
						break;
					//}else{
						//cerr << "=";
					}
				}
				// si ok comprobamos si es menor que el maximo
				if(ok){
					ok = true;
					for(int k=0;k<maxrot;k++){
						if(stringnumber[(j+k)%maxrot] > stringmax[k]){
							ok = false;
							//cerr << "o";
							break;
						}else if(stringnumber[(j+k)%maxrot] < stringmax[k]){
							ok = true;
							//cerr << "-";
							break;
						//}else{
							//cerr << "?";
						}
					}
				}
				if(ok){
					numeroencontrado = desplaza(stringnumber,j);
					//cerr << "{" <<stringnumber << "," << numeroencontrado << "}";
					found = false;
					for(unsigned int k=0;k<numeros.size();k++){
						//cerr << "%";
						if(numeroencontrado==numeros[k]){
							//cerr << "alert;";
							found = true; break;
						}
					}
					if(!found){
						//cerr << "x";
						numeros.push_back(numeroencontrado);
						res++;
					}
				}
			}
		}

		cout << res << endl;
		cerr << res << endl;

	}
}
