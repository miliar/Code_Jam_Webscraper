#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <numeric>
#include <fstream>
using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define lg length
#define sz size
#define forn(i,n) for(i=0;i<n;i++)
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
bool abc[26+'a'] = {false}; 
char ss[1000];
typedef pair <char,int> ci; 
typedef pair <int, int> ii;
vector <ci> v;
char *css = "welcome to code jam";
int rta;
vector < vector < ii > > letras;
// Funcion recursiva:
void recur(int current, int max , int accum) {
	if(current==19) {
		rta += accum;
		//cout<<"Accum: "<<accum<<endl;
	}
	else {
		int ind = css[current]; // Letra a buscar.
		cout<<css[current]<<endl;
		for(int i=0;i<letras[ind].sz();i++) {
			if(max<letras[ind][i].first) {
				recur(current+1,letras[ind][i].first,(letras[ind][i].second*accum)%10000);
			}	
		}	
	}	
}
main () {
	// Declaracion de Variables:
	int i,j,k,t;
	int T;
	char temp [1000];
	// Inicializacion:
	abc['w'] = abc['e'] = abc['l'] = abc['c'] = abc['o'] = abc['m'] = abc['t'] = abc['d'] = abc['j'] = abc['a'] = true;
	// Letras utiles:
	// Apertura de archivos:
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small.out");
	// Lectura de datos:
	fin>>T;
	fin.get();
	for(t=1;t<=T;t++) {
		k = 0;
		//cout<<"Caso: "<<t<<endl;
		fout<<"Case #"<<t<<": ";
		fin.getline(temp,1000,'\n');
		// Eliminar letras que no sirven:
		for(i=0;i<strlen(temp);i++) {
			if(temp[i] == ' ' || abc[temp[i]]) {
				ss[k] = temp[i];
				k++;
			}	 
		}
		ss[k] = '\0';
		//cout<<ss<<endl;
		// Comprimir:
		k = 0;
		v.clear();
		letras.clear();	
		letras.resize(150);	
		while(k<strlen(ss)) {
			i = k;
			while(i<strlen(ss) && ss[i]==ss[i+1]) i++;	
			v.pb(ci(ss[k],i-k+1));
			k = i+1;
		}
		// Crear estructura letras:
		for(i=0;i<v.sz();i++) {
			letras[v[i].first].pb(ii(i,v[i].second));	
		}
		/*for(i=0;i<19;i++) {
			cout<<css[i]<<endl;
			for(j=0;j<letras[css[i]].sz();j++) cout<<letras[css[i]][j].first<<" -- "<<letras[css[i]][j].second<<endl; 	
		}*/
		// Buscar cantidad de substrings:
		rta = 0;
		recur(0,-1,1);
		if(rta<1000) fout<<"0";
		if(rta<100) fout<<"0";
		if(rta<10) fout<<"0";
		fout<<rta<<endl;
	}
	// Cierro archivos:
	fin.close();
	fout.close();
return 0;	
}
