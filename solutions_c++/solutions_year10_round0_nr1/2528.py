#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;

int main() {
ifstream ulaz("A-large.in");
ofstream izlaz("output.txt");
int t, n, k;
	
	ulaz>>t;
	for(int i=0; i<t; i++) {
		ulaz>>n>>k;
		izlaz<<"Case #"<<i+1<<": ";
		if((k+1)%(int)pow(2., (double)n)==0) izlaz<<"ON\n";
		else izlaz<<"OFF\n";
	}
	ulaz.close();
	izlaz.close();
}