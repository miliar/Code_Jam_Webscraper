#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int cc;
	fin>>cc;
	int v[41],c1, d[41];
	bool sd[41];
	char cs[64];
	for (int cn=0;cn<cc;cn++) {
		int n;
		fin>>n;
		FOR(i,n) {
			fin>>cs;
			c1=0;
			FOR (j,n) {
				if (cs[j]=='1') c1=j;
			}
			v[i]=c1;
		}
		bool done;
		int aux,res=0;
		do {
			int p=0;
			while (p<n && v[p]<=p) p++;
			if (p==n) break;
			int s=p+1, dest=p;
			while (v[s]>p) s++;
			bool bl=true;
			while (s!=dest) {
				res++;
				if (s-1==p) {
					aux=v[p];v[p]=v[s];v[s]=aux;
					s--; p++;
				} else {
					if (bl) {
						aux=v[s];
						v[s]=v[s-1];
						v[s-1]=aux;
						s--;
					} else {
						aux=v[p];
						v[p]=v[p+1];
						v[p+1]=aux;
						p++;
					}
				}
			}
		} while (true);
		fout<<"Case #"<<cn+1<<": "<<res<<endl;
	}
	fout.close();
	fin.close();
}
