#include <fstream>
#include <algorithm>
#include <iostream>
using namespace std;
int main(){
	int n,i,j,t,p,posb,poso,reso,resb;
	char c;
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");
	in>>t;
	for (i = 1;i<=t;i++){
		in>>n;
		poso = 1;
		posb = 1;
		reso = 0;
		resb = 0; 
		for (j = 1;j<=n;j++){
			in>>c;
			in>>p;
			if (c == 'B'){
				resb += abs(p-posb) +1;
				posb = p; 
				resb = max (resb,reso+1);
			}
			else{
				reso += abs (p-poso) +1;
				poso = p;
				reso = max (reso,resb+1);
			}
		}
		out<<"Case #"<<i<<": "<<max(resb,reso)<<"\n";
	}
}
