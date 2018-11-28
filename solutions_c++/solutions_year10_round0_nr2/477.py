#define _GLIBCXX_FULLY_DYNAMIC_STRING 1
#undef _GLIBCXX_DEBUG
#undef _GLIBCXX_DEBUG_PEDANTIC
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include "/Users/HOOI/Downloads/bigint-3-0-src/bigint.h"
/* Program uses BigInt from http://sourceforge.net/projects/cpp-bigint/files/C%2B%2B%20BigInt%20Class/Version%202.0/ */
using namespace std;

RossiBigInt gcd(RossiBigInt a, RossiBigInt b){
	if (b==RossiBigInt(0)) return a;
	else return gcd(b,a%b);
}
int main () {
	int C,N;
	string tempinput;
	vector<RossiBigInt> V,W;
	fstream filestr;
	ofstream outstr;
	filestr.open("/Users/HOOI/Downloads/B-large.in");
	outstr.open("/Users/HOOI/Downloads/GoogleCodeJam/BLargeOut.txt");
	filestr >> C;
	cout << "lines: "<<C<<endl;
	for (int i=1;i<=C;i++){ 
		filestr >> N;
		cout << "entries: "<<N<<endl;
		V.clear(); W.clear();
		for (int j=0;j<N;j++){
			filestr >> tempinput; 
			RossiBigInt rin=RossiBigInt(0);
			for (int i=0;i<tempinput.size();i++){
				rin += RossiBigInt(tempinput[i]-'0');
				rin = rin* RossiBigInt(10);
			}
			rin = rin / RossiBigInt(10);
			V.push_back(RossiBigInt(rin));
			cout << "received "<<V[j]<< " for V "<<j<<"."<<endl;
		}
		sort(V.begin(), V.end());
		for (int j=0;j<N-1;j++){ 
			W.push_back(V[j+1]-V[j]);
			cout << "W["<<j<<"] is "<<W[j]<<endl;
		}
		cout << "Done differences."<<endl;
		sort(W.begin(), W.end());
		for (int j=0;j<N-2;j++){
			W[j+1] = gcd(W[j+1], W[j]);
			cout <<"Now W["<<j+1<<"] is "<<W[j+1]<<endl;
		}
		RossiBigInt hcf=W[N-2];
		cout << "hcf is "<<hcf<<endl;
		RossiBigInt res;
		if (V[0]%hcf== RossiBigInt(0)) res=RossiBigInt(0); else res=hcf-V[0]%hcf;
		outstr << "Case #"<<i<<": "<< res <<endl;
		cout << "Case #"<<i<<": "<<res<<endl;
	}			
	filestr.close();
	outstr.close();
	return 0;
}