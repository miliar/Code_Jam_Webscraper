#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int counter=0,A,B;

void recyc (int n) {
	int digits=floor(log10(n)+1);
	int recyc,q,w;
	for (int k=1;k<digits;k++) {
		q=pow(10,k); w=pow(10,digits-k);
		recyc=((n-(n%q))/q)+(n%q)*w;
		if ((n<recyc)&&(recyc<=B)) counter++;
	}
}

int main () {
	ifstream fin ("recycle.in");
	ofstream fout ("recycle.out");
	
	int T,n; fin>>T;
	for (int k=1;k<=T;k++) {
		counter=0;
		fin>>A>>B;
		for (n=A;n-1<B;n++) {
			recyc(n);
		}
		fout<<"Case #"<<k<<": "<<counter<<'\n';
	}
	return 0;
}