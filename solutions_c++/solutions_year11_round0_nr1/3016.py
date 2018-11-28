//http://code.google.com/codejam/contest/dashboard?c=975485#
#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	ifstream fin("date.in");
	ofstream fout("date.out");
	int to = 0,tb = 0,poso = 1,posb = 1,t = 0,p,test,i,n,k;
	char aux;
	fin>>test;
	for(k = 1; k <= test; k++) {
		fin>>n;
		to = 0;
		tb = 0;
		t = 0;
		poso = 1;
		posb = 1;
		for(i = 1; i <= n ; i++) {
			fin>>aux>>p;
			if(aux == 'O') {
				if(abs(p - poso) - t + to > 0) {
					t += (abs(p - poso) - t + to + 1);
					poso = p;
					to   = t;
				} else {
					t++;
					poso = p;
					to = t;
				}
			} else {
				if(abs(p - posb) - t + tb > 0) {
					t += (abs(p - posb) - t + tb + 1);
					posb = p;
					tb   = t;
				} else {
					t++;
					posb = p;
					tb = t;
				}
			}
		}
		fout<<"Case #"<<k<<": "<<t<<'\n';
	}
}
