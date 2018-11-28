#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int cc;
	fin>>cc;
	int pows[32];
	pows[0]=1;
	for (int i=1;i<32;i++)
		pows[i]=pows[i-1]*2;
	for (int cn=0;cn<cc;cn++) {
		int k,n;
		fin>>n>>k;
		fout<<"Case #"<<cn+1<<": "<<((k+1)%pows[n]==0?"ON":"OFF")<<endl;
	}
	fout.close();
	fin.close();
}
