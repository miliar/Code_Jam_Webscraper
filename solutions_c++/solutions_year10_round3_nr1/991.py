#include<iostream>
#include<fstream>

using namespace std;


int main() {
ifstream ulaz("ulaz.txt");
ofstream izlaz("output.txt");
int t, n, brojPreseka;
int *a, *b;

	ulaz>>t;

	for(int i=1; i<=t; i++) {
		ulaz>>n;

		a=new int[n];
		b=new int[n];
		brojPreseka=0;
		for(int j=0; j<n; j++) {
			ulaz>>a[j]>>b[j];
			for(int k=0; k<j; k++) {
				if((a[j]-a[k])*(b[j]-b[k])<0) brojPreseka++;
			}
		}
		izlaz<<"Case #"<<i<<": "<<brojPreseka<<endl;
	}

}