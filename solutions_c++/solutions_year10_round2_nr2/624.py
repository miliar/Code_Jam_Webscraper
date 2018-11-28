#include<iostream>
#include<fstream>

using namespace std;

bool stize(int x, int b, int v, int t) {
	if (((float)(b-x))/v<=t) return true;
	else return false;
}


int main() {
ifstream ulaz("ulaz.txt");
ofstream izlaz("output.txt");
int c, n, k, b, t, brojSporih, brojBrzih, brojZamena;
int *x;
int *v;

 ulaz>>c;
 for (int i=1; i<=c; i++) {
	 brojSporih=brojBrzih=brojZamena=0;
	 ulaz>>n>>k>>b>>t;
	 x=new int[n];
	 v=new int[n];
	 for(int k=0; k<n; k++) ulaz>>x[k];
	 for(int k=0; k<n; k++) ulaz>>v[k];
	 for(int j=n-1; j>=0; j--) {
		if (stize(x[j], b, v[j], t)) {
			brojBrzih++;
			brojZamena=brojZamena+brojSporih;
			if(brojBrzih==k) break;
		}
		else brojSporih++;
	 }
	 delete x;
	 delete v;
	 izlaz<<"Case #"<<i<<": ";
	 if (brojBrzih<k) izlaz<<"IMPOSSIBLE"<<endl;
	 else izlaz<<brojZamena<<endl;
 }
}