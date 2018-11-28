#include <cstdio>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int cases;
int turn;
int na,nb;
string t;

const int MAXT=2005;
int atime[MAXT],btime[MAXT];

int convert(string a) {	return 600*int(a[0]-'0')+60*int(a[1]-'0')+10*int(a[3]-'0')+int(a[4]-'0');}

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	fin>> cases;
	for(int i=0;i<cases;i++) {
		memset(atime,0,sizeof(atime));
		memset(btime,0,sizeof(btime));
		fin >> turn >> na >> nb;
		for(int j=0;j<na;j++) {
			fin >> t;
			atime[convert(t)]--;
			fin >> t;
			btime[convert(t)+turn]++;
		}
		for(int j=0;j<nb;j++) {
			fin >> t;
			btime[convert(t)]--;
			fin >> t;
			atime[convert(t)+turn]++;
		}

		int reta=0;
		int retb=0;
		int suma=0;
		int sumb=0;
		for(int j=0;j<MAXT;j++) {
			suma+=atime[j];
			reta<?=suma;
		}
		for(int j=0;j<MAXT;j++) {
			sumb+=btime[j];
			retb<?=sumb;
		}
		
		fout << "Case #" << i+1 << ": " << -reta << " " << -retb << endl;
	}
	return 0;
}
