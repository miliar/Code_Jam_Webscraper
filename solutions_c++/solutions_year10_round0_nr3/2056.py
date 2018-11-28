#include <fstream>
#include <iostream>
using namespace std;
#define MAXGR 1001;

class Grupa {
private:
	__int64 novac;
	int sled;
	
public:
	Grupa(int r, int k, int n, int g[], int index) {
		int prvi = index;
		__int64 putnika = g[index];
		index = (index+1)%n;
		while (putnika < k && prvi!=index) {
			putnika+=g[index];
			index = (index+1)%n;
		}
		if (putnika > k) {
			index = index?(index-1):(n-1);
			putnika-=g[index];
		}
		novac = putnika;
		sled = index;
	}
	int dajsled() { return sled; }
	__int64 dajnovac() { return novac; }
};

__int64 obrada(int r, int k, int n, int g[]) {
	__int64 rez = 0;
	int index = 0;
	Grupa *grupe[1001];
	for (int i = 0; i<n; i++) grupe[i] = new Grupa(r,k,n,g,i);

	for (int i = 0; i<r; i++) {
		rez += grupe[index]->dajnovac();
		index = grupe[index]->dajsled();
	}

	for (int i = 0; i<n; i++) delete grupe[i];
	return rez;
}

void main(int argc, char *argv[]) {
	if (argc!=3) exit(-1);

	ifstream ulaz(argv[1]);
	if (!ulaz) exit(-1);
	ofstream izlaz(argv[2]);
	if (!izlaz) exit(-1);

	int t, r, k, n;
	int g[1001];
	ulaz >> t;
	for (int i = 1; i <= t; i++) {
		ulaz >> r >> k >> n;
		for (int j = 0; j < n; j++) 
			ulaz >> g[j];
		izlaz << "Case #" << i << ": " << obrada(r, k, n, g) << endl;
		cout << "case " << i << " | ";
	}

	ulaz.close(); izlaz.close();
}