#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <fstream>
#include <math.h>
#include <algorithm> 
#include <vector> 
#include <string>

using namespace std;

void main() {
	ifstream fin("A.in");
	ofstream fout("A.out");

	long T; fin >> T;
	for (long l=0; l<T; l++) {
		long n; fin >> n;
		long* a = new long[n];
		long* b = new long[n];
		long long res = 0;
		for (int i=0; i<n; i++) {
			fin >> a[i] >> b[i];
			for (int j=0; j<i; j++) {
				if ( (a[i]<a[j] && b[i]>b[j]) ||
					(a[i]>a[j] && b[i]<b[j] ))
					res++;
			}
		}

		fout << "Case #" << (l+1) << ": ";
		fout << res << endl;
	}

	fin.close(); fout.close();
}