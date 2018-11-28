#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <cstring>
using namespace std;
#define pb push_back
#define sz size
// Variables globales:
char palabra[20];
vector < vector <char> > v;
int L;
int cont;
map <string,bool> dict; 
// Funcion recursiva:
void recur(int n) {
	if(n==L) {
		palabra[L] = '\0';
		if(dict[palabra]) cont++;
		//cout<<palabra<<endl;		
	}	
	else {
		for(int i=0;i<v[n].sz();i++) {
			palabra[n] = v[n][i];
			palabra[n+1] = '\0';
			if(dict[palabra]==true)
				recur(n+1);	
		}	
	}
}
main () {
	// Declaracion de Variables:
	int D,N;
	char temp[1000];
	bool m[15][100+'a'] = {{false}};
	bool flag;
	int i,j,k;
	// Apertura de archivos:
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	// Lectura de datos:
	fin>>L>>D>>N;
	fin.get();
	for(i=0;i<D;i++) {
		fin.getline(temp,100,'\n');
		for(j=0;j<strlen(temp);j++) {
			m[j][temp[j]] = true;		
		}
		for(j=0;j<strlen(temp);j++) {
			char temp2[1000] = {};
			for(k=0;k<=j;k++) {
				temp2[k] = temp[k];
			}
			temp2[j+1] = '\0';
			dict[temp2] = true;		
		}
	}
	// Algoritmo: 
	for(i=1;i<=N;i++) {
		fout<<"Case #"<<i<<": ";
		fin.getline(temp,1000,'\n');
		// Seperar el string en letras:
		v.clear();
		v.resize(L);
		k=0; // Indica el token.
		j = 0;
		while(j<strlen(temp)) {
			if(temp[j]=='(') {
				for(j=j+1;j<strlen(temp) && temp[j]!=')';j++) {
					if(m[k][temp[j]])
						v[k].pb(temp[j]);	
				}
				j++; // Saltar el parentesis ')'.	
				k++;
			}
			else {
				if(m[k][temp[j]]) {
					v[k].pb(temp[j]);
				}
				j++;
				k++;	
			}	
		}
		// Test Print:
		/*for(j=0;j<L;j++) {
			cout<<"(";
			for(k=0;k<v[j].sz();k++) cout<<v[j][k];
			cout<<")";
		}
		cout<<endl;*/
		// Calcular cantidad de palabras:
		cont = 0; // Para contar cantidad de palabras.
		flag = true;
		for(j=0;j<L&&flag;j++) 
			if(v[j].sz()==0) 
				flag = false;
		if(flag) {
			recur(0);
		}
		fout<<cont<<endl;
	}
	// Respuesta:
	// Cierro archivos:
	fin.close();
	fout.close();
return 0;	
}
