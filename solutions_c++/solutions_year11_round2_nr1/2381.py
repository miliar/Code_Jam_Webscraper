#include <iostream>
#include <fstream>
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
#include <iomanip>
using namespace std;

void swap(long long &a, long long &b) { int temp=a; a=b; b=temp;}

int mcd(long long a, long long b) {
	while(b>0) {
		if(a>b) swap(a,b);
		b = b % a;
	}
	return a;
}

int mcm(long long a, long long b) {
	return a*b/mcd(a,b);
}

int main() {

	ifstream fin("A.in");
	ofstream fout("A.out");

	int T,t,N;
	char v[105][105];
	long long OWP[105][2];
	long long OOWP[105][2];
	long long played[105];
	long long win[105];
	int a;

	fin>>T;
	
	for(t=1;t<=T;t++) {
		fin>>N;

		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				fin>>v[i][j];
			}
		}
		// Test print:
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				cout<<v[i][j];
			}
			cout<<endl;
		}

		// Calcular WP:
		for(int i=0;i<N;i++) {
			played[i] = 0;
			win[i] = 0;
			for(int j=0;j<N;j++) {
				if(v[i][j]!='.') {
					played[i]++; // Cantidad de partidos jugados.
				}
				if(v[i][j]=='1') {
					win[i]++; // Cantidad de partidos ganados.
				}
			}
		}
		// WP[i] = win[i] / played[i].

		// Calcular OWP:
		
		for(int i=0;i<N;i++) {
			OWP[i][0] = 0;
			OWP[i][1] = 1;
			long long count = 0;
			//cout<<"Here i: "<<i<<endl;
			for(int j=0;j<N;j++) {
				//cout<<"Here j: "<<j<<endl;
				if(v[i][j]!='.') {
					count++;
					long long den,num;
					// Suma fracciones:
					den = played[j]-1;
					num = win[j];
					if(v[j][i]=='1') {
						num--; // No considero este juego.
					}
					if(den==0) { den = 1; num = 0; } // Sumar 0.
					cout<<num<<" "<<den<<" "<<OWP[i][0]<<" "<<OWP[i][1]<<endl;
					a = mcm(OWP[i][1],den);
					//cout<<"MCM: "<<a<<endl;
					OWP[i][0] = (a*OWP[i][0])/OWP[i][1] + (a*num)/den;
					OWP[i][1] = a;
					// Reducir:
					if(OWP[i][0]!=0) {
						a = mcd(OWP[i][0], OWP[i][1]);
						//cout<<"MCD: "<<a<<endl;
						OWP[i][0] /= a;
						OWP[i][1] /= a;
					}
				}
			}
			OWP[i][1] *= count;
		}
		cout<<"OWP: "<<endl;
		for(int i=0;i<N;i++) cout<<OWP[i][0]<<" "<<OWP[i][1]<<endl;
		// Calcular OOWP:
		for(int i=0;i<N;i++) {
			OOWP[i][0] = 0;
			OOWP[i][1] = 1;
			long long count = 0;
 			for(int j=0;j<N;j++) {
				if(v[i][j]!='.') {
					count++;
					long long num,den;
					num = OWP[j][0];
					den = OWP[j][1];
					if(den==0) {den = 1; num = 0;}
					
					a = mcm(OOWP[i][1],den);
					OOWP[i][0] = (a*OOWP[i][0])/OOWP[i][1] + (a*num)/den;
					OOWP[i][1] = a;
					// Reducir:
					if(OOWP[i][0]!=0) {
						cout<<"MCD"<<OOWP[i][0]<<" "<<OOWP[i][1]<<endl;
						a = mcd(OOWP[i][0], OOWP[i][1]);
						OOWP[i][0] /= a;
						OOWP[i][1] /= a;
					}
				}
			}
			OOWP[i][1] *= count;
		}
		// Calculo final:
		fout<<"Case #"<<t<<":"<<endl;
		for(int i=0;i<N;i++) {
			double WP = 0.0;
			if(played[i]!=0) WP = (double)win[i]/(double)played[i];
			double OWP1 = 0.0;
			if(OWP[i][1]!=0) OWP1 = (double)OWP[i][0]/(double)OWP[i][1];
			double OOWP1 = 0.0;
			if(OOWP[i][1]!=0) OOWP1 = (double)OOWP[i][0]/(double)OOWP[i][1];
			double RPI = 0.25 * WP + 0.50 * OWP1 + 0.25 * OOWP1;
			  
			fout<<setprecision(12)<<RPI<<endl;
		}
		
		
	}

	return 0;
}
