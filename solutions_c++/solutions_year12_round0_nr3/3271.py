#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	ifstream filein("b.in");
	ofstream fileout("b.out");
	int T,i,j,k,index,length, div10;
	long long A, B, n,m,flag;// A<=n<m<=B;
	int pow10[8]={1,10,100,1000,10000,100000,1000000,10000000};
	filein >> T;

	for (i=1; i<=T; i++) {
		flag=0;
		filein >> A >> B;
		length = 1;
		for (n=A;n<=B;n++) {
			while (n>=pow10[length]) length++;
			if (length==1) continue;
		//	fileout << endl<<n << endl;
			for (j=1;j<length;j++){
				m = n / pow10[j] + (n % pow10[j]) * pow10[length-j];
		//		fileout << "m=" << m << ' ';
		//		fileout << m << " " << j << endl;
				if ((m>n) && (m<=B)) {
					flag++;
		//			fileout << "pair: " << n <<' ' << m << endl << endl;
				}
			}
		}
		fileout << "Case #" << i << ": "<< flag;
		if (i<T) fileout << endl;
	}
	return 0;
}