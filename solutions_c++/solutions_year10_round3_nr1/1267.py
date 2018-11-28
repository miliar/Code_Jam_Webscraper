#include <fstream>
using namespace std;

struct Linija {
	int a,b;
};

bool proveri(int a1, int b1, int a2, int b2) {
	int da = a1-a2, db = b1 - b2;
	if ((da < 0) && (db < 0) || (da > 0) && (db > 0)) return false;
	else return true;
}

void main(int argc, char *argv[]) {
	if (argc!=3) exit(-1);

	ifstream ulaz(argv[1]);
	if (!ulaz) exit(-1);
	ofstream izlaz(argv[2]);
	if (!izlaz) exit(-1);
	
	int t;
	ulaz >> t;
	for (int i = 1; i<=t; i++) {
		Linija skup[1000];
		int n, rez = 0;
		ulaz >> n;
		for (int j = 0; j<n; j++) ulaz >> skup[j].a >> skup[j].b;
		for (int j = 0; j<n; j++)
			for (int k = j+1; k<n; k++) {
				if (proveri(skup[j].a, skup[j].b, skup[k].a, skup[k].b)) rez++;
			}
		izlaz << "Case #" << i << ": " << rez << endl;
	}

	ulaz.close(); izlaz.close();
}