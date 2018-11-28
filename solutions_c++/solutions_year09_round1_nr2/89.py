#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int n,m;
int s[25][25];
int w[25][25];
int t[25][25];
int mt[60][60];

int ct(int ta, int i, int j, bool sn) {
	int &t0=t[i][j];
	int &tw=w[i][j];
	int &ts=s[i][j];
	int tt=tw+ts;
	int td=ta-t0;
	if (td<0) td+=((-td)/tt+1)*(tt);
	td=td%tt;
	if (sn) {
		if (td<ts) {
			return ta+1;
		} else {
			return ta+(tt-td)+1;
		}
	} else {
		if (td<ts) {
			return ta+(ts-td)+1;
		} else {
			return ta+1;
		}
	}
}

int main(int argc, char *argv[]) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int c;
	fin>>c;
	for (int nc=0;nc<c;nc++) {
		memset(mt,0,sizeof(mt));
		fin>>n>>m;
		FOR(in,n) {
			FOR(im,m) {
				fin>>s[n-in][im+1];
				fin>>w[n-in][im+1];
				fin>>t[n-in][im+1];
			}
		}
		
		bool change=true;
		while (change) {
			change=false;
			for (int ii=1;ii<=2*n;ii++) {
				for (int jj=1;jj<=2*m;jj++) {
					if (ii==1&&jj==1) continue;
					int t1=0, t2=0;
					if (ii%2) {
						if (mt[ii-1][jj] ||(ii==2&&jj==1)) 
							t1=mt[ii-1][jj]+2;
						if (mt[ii+1][jj]) 
							t2=ct(mt[ii+1][jj],(ii+1)/2,(jj+1)/2,true);
					} else {
						if (mt[ii-1][jj]||(ii==2&&jj==1)) 
							t1=ct(mt[ii-1][jj],(ii+1)/2,(jj+1)/2,true);
						if (mt[ii+1][jj]) 
							t2=mt[ii+1][jj]+2;
					}
					if (t1!=0 && (mt[ii][jj]==0 || t1<mt[ii][jj])) {mt[ii][jj]=t1;change=true;}
					if (t2!=0 && (mt[ii][jj]==0 || t2<mt[ii][jj])) {mt[ii][jj]=t2;change=true;}
					
					t1=0; t2=0;
					if (jj%2) {
						if (mt[ii][jj-1]||(ii==1&&jj==2)) 
							t1=mt[ii][jj-1]+2;
						if (mt[ii][jj+1]) 
							t2=ct(mt[ii][jj+1],(ii+1)/2,(jj+1)/2,false);
					} else {
						if (mt[ii][jj-1]||(ii==1&&jj==2)) 
							t1=ct(mt[ii][jj-1],(ii+1)/2,(jj+1)/2,false);
						if (mt[ii][jj+1]) 
							t2=mt[ii][jj+1]+2;
					}
					if (t1!=0 && (mt[ii][jj]==0 || t1<mt[ii][jj])) {mt[ii][jj]=t1;change=true;}
					if (t2!=0 && (mt[ii][jj]==0 || t2<mt[ii][jj])) {mt[ii][jj]=t2;change=true;}
					
				}
			}
		}
		cerr<<endl;
		cerr<<endl;
		for (int ii=1;ii<=2*n;ii++) {
			for (int jj=1;jj<=2*m;jj++) {
					cerr<<mt[ii][jj]<<"  ";
			}
			cerr<<endl;
		}
		fout<<"Case #"<<nc+1<<": "<<mt[2*n][2*m]<<endl;
	}
	fout.close();
	fin.close();
}
