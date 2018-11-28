#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int cc;
	fin>>cc;
	int d[100][100];
	for (int cn=0;cn<cc;cn++) {
		cerr<<cn;
		int k,q;
		fin>>k;
		q=k;
		int i=0, j=0, m=0,n=0;
		for (int l=0;l<k*k;l++) {
			fin>>d[i][j];
			i--;
			if (i<0 || j+1==k) {
				if (m<k-1) {
					m++;
					i=m;
					j=0;
				} else {
					i=k-1;
					n++;
					j=n;
				}
			} else {
				j++;
			}
		}
		
		int nq=q,res=0,i1,j1,i2,j2;
		bool sim=true;
		while (true) {
			for (int ii=0;ii<nq-q+1;ii++) {
				for (int jj=0;jj<nq-q+1;jj++) {
					sim=true;
					// verificar sim
					for (int i=0;i<nq;i++) {
						for (int j=0;j<nq;j++) {
							int i1=i-ii, i2=j-ii;
							int j1=j-jj, j2=i-jj;
							if (i1<0||i2<0||j1<0||j2<0) continue;
							if (i1>=q||i2>=q||j1>=q||j2>=q) continue;
							if (d[i1][j1]!=d[i2][j2]) {
								sim=false;
								break;
							}
						}
						if (!sim) break;
					}
					if (!sim) continue;
					for (int i=0;i<nq;i++) {
						for (int j=0;j<nq;j++) {
							int i1=i-ii, i2=nq-1-j-ii;
							int j1=j-jj, j2=nq-1-i-jj;
							if (i1<0||i2<0||j1<0||j2<0) continue;
							if (i1>=q||i2>=q||j1>=q||j2>=q) continue;
							if (d[i1][j1]!=d[i2][j2]) {
								sim=false;
								break;
							}
						}
						if (!sim) break;
					}
					if (sim) break;
				}
				if (sim) break;
			}
			if (sim) break;
			res+=2*nq+1;
			nq++;
		}
		fout<<"Case #"<<cn+1<<": "<<res<<endl;
	}
	fout.close();
	fin.close();
}
