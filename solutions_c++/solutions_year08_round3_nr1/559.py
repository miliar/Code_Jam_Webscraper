// iassad - Iyad Assad
// to solve Google code.jam Round 1 - Subround c - Problem a

#include <iostream>
#include <fstream>

using namespace std;

#
void sort(long x[],long length) {
	long k,i;
	for(long j=1;j<length;j++) {
		k=x[j];
		i=j-1;
		while(x[i]<k && i>=0) {
			x[i+1]=x[i];
			i--;
		}
		x[i+1]=k;
	}
}

int main (int argc, char * argv[]) {
	int cases;
	char fn[200];

	if (argc < 2) {
		cout << endl << "Usage: " << endl << endl << argv[0] << " input-filename" << endl << endl;
		return 0;
	}

	ifstream fin(argv[1]);
	sprintf(fn,"%s.output",argv[1]);
	ofstream fout(fn);

	fin >> cases;

	for (int cn=1; cn<=cases; cn++) {
		long p,k,l;
		fin >> p >> k >> l; 

		long * freq = new long[l];

		for (int i=0; i<l; i++)
			fin >> freq[i];

		sort(freq, l);

		long pr = 1;
		long t = 0;
		for (int i=0; i<l; i++) {
			t += freq[i] * pr;
			if ((i+1)%k == 0)
				pr++;
		}

		fout << "Case #" << cn << ": " << t << endl;

		delete [] freq;
	}

	fin.close();
	fout.close();
	
	return 0;
}
