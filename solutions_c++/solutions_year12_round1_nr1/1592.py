#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int T,A,B;

float productoria (float a[], int n) {
	float k=1;
	for (int j=0;j<=A-n-1;j++) {
		k*=a[j];
	}
	return k;
}

int main () {
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	fin>>T;
	float p[99999],k[100000];
	int j;
	for (int x=1;x<=T;x++) {
		fin>>A>>B;
		for (j=0;j<=A-1;j++) {
			fin>>p[j];
		}
		for (j=0;j<=A-1;j++) {
			k[j]=(productoria(p,j)*(B-(A-2*j)+1))+((1-productoria(p,j))*((B-(A-2*j)+1)+B+1));
		}
		k[A]=2+B;
		sort (k,k+A+1);
		fout<<"Case #"<<x<<": "<<k[0]<<"\n";
	}
	return 0;
}