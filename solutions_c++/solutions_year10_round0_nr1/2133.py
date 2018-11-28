#include <fstream>
using namespace std;

bool proveri(int n, int k) {
	unsigned int broj = 1;
	broj <<= n;
	broj--;
	
	if ((k & broj) == broj) return true;
	else return false;
}

void main(int argc, char *argv[]) {
	if (argc!=3) exit(-1);

	ifstream ulaz(argv[1]);
	if (!ulaz) exit(-1);
	ofstream izlaz(argv[2]);
	if (!izlaz) exit(-1);

	int n, k, t;
	ulaz >> t;
	for (int i = 1; i<=t; i++) {
		ulaz >> n >> k;
		izlaz << "Case #" << i << ": ";
		if (proveri(n,k)) izlaz << "ON" << endl;
		else izlaz << "OFF" << endl;
	}
	
	ulaz.close(); izlaz.close();
}