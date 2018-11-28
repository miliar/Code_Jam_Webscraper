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
#include <cstdlib>
#include <fstream>
#include <iomanip>
using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define lg length
#define sz size
#define forn(i,n) for(i=0;i<n;i++)
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
int g[103][103];
int N;
int nodos[103];
int rta = 9999;
//int cmp;
/*void recur(int x) {
	nodos[x] = cmp;
	for(int i=0;i<N;i++) {
		if(nodos[i]==0 && g[x][i]==1) recur(i);	
	}
}*/
void recur(int x, int cmp) {
	//cout<<x<<endl;
	//cin.get();
	nodos[x] = cmp;
	int i,j;
	bool flag;
	for(i=x;i<N;i++) {
		if(nodos[i]==0 && g[x][i]==1) {
			//cout<<"Candidato: "<<i<<endl;
			// Comprobar que no haya problemas:
			flag = true;
			for(j=0;j<N&&flag;j++) {
				if(nodos[j]==cmp && g[i][j]==0) flag = false;	
			}
			if(flag) {
				//cout<<"No problem, recur."<<endl;
				recur(i,cmp);	// Sigo en el mismo chart.
				nodos[i] = 0;
			}
			//else { cout<<"Problems with member."<<endl;}	
		}
	}
	flag = false;
	for(i=0;i<N;i++) {
		if(nodos[i]==0) {
			flag = true;
			break;
		}	
	}
	if(flag) {
		if(cmp+1<rta)
			recur(i,cmp+1);
	}
	else {
		if(cmp<rta) {
			rta = cmp;	
			//cout<<"Rta actual: "<<rta<<endl;
			//for(i=0;i<N;i++) cout<<nodos[i]<<" ";
			//cout<<endl<<"*********************"<<endl;
		}
	
	}
	
	nodos[x] = 0;
}
int main() {
	// Declaracion de variables:
	int T,t;
	int i,j,k;
	int K;
	bool flag;
	vector < vector <int> > p; 
	// Apertura de archivos
	ifstream fin("C.in");
	ofstream fout("C.out");
	
	// Lectura de datos:
	fin>>T;
	for(t=1;t<=T;t++) {
		fout<<"Case #"<<t<<": ";
		fin>>N>>K;
		p.clear();
		p.resize(N);
		for(i=0;i<N;i++) p[i].resize(K);
		for(i=0;i<N;i++) {
			for(j=0;j<K;j++) {
				fin>>p[i][j];
			}	
		}
		for(i=0;i<N;i++) for(j=0;j<N;j++) g[i][j] = 1;
		// Verificar cruces:
		for(i=0;i<N-1;i++) {
			for(j=i+1;j<N;j++) {
				flag = true;
				for(k=0;k<K-1 && flag;k++) {
					if(p[i][k]==p[j][k] || (p[i][k] > p[j][k] && p[i][k+1] < p[j][k+1]) || (p[i][k] < p[j][k] && p[i][k+1] > p[j][k+1]))
						flag = false;			
				}
				// Ultimo punto:
				if(p[i][K-1]==p[j][K-1]) flag = false;
				// Se cruzan:
				if(!flag) {
					g[i][j] = g[j][i] = 0;
				}
			}	
		}
		/*for(i=0;i<N;i++) {
			for(j=0;j<N;j++) cout<<g[i][j]<<" ";
			cout<<endl;
		}
		cin.get();*/
		rta = 9999;
		for(i=0;i<N;i++) nodos[i] = 0;
		recur(0,1);
		fout<<rta<<endl;
	}
	
	//cin.get();
	// Cierro Archivos:
	fin.close();
	fout.close();
return 0;	
}
