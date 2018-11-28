#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	long long cc;
	fin>>cc;
	long long r,k,n;
	long long g[10000];
	long long ig=0,f;
	for (int cn=0;cn<cc;cn++) {
		fin>>r>>k>>n;
		for (long long i=0;i<n;i++)
			fin>>g[i];
		long long eur=0;
		ig=0;
		for (long long i=0;i<r;i++) {
			f=k;
			long long gc=0;
			while (gc<n && f>=g[ig]) {
				eur+=g[ig];
				f-=g[ig];
				ig = (ig+1)%n;
				gc++;
			}
		}
		fout<<"Case #"<<cn+1<<": "<<eur<<endl;
	}
	fout.close();
	fin.close();
}
