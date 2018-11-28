#include <iostream>
#include <fstream>
#include <string>
using namespace std;
typedef unsigned int C_N;
#define D_ALG 30

ifstream impfile;
string IMPFN = "C-large.in";
ofstream outpfile;
string OUTPFN = "C-large.out";
C_N		T;
C_N		t;
C_N		N;
//C_N		NUM;
C_N		num;

void CASE () {
	//cout << "==void CASE ()" << endl;
	//char	stop;
	C_N		i;
	C_N		j;
	C_N		num;
	C_N		small;
	C_N		Seans;
	bool	bin[N][D_ALG];
	bool	parity[D_ALG];
	bool	YN;
	for (i = Seans = 0, impfile >> num, small = num; i < N; i++, impfile >> num) {
		small = num<small?num:small;
		Seans += num;
		for (j = 0; j < D_ALG; j++, num /= 2) {
			bin[i][j] = num%2;
			//cout << bin[i][j];
		}
		//printf("\n");
	}
	for (j = YN = 0; j < D_ALG; j++) {
		for (i = parity[j] = 0; i < N; i++) {
			if (bin[i][j]) {
				//printf (" ");
				parity[j] = !parity[j];
				}
		}
		YN |= parity[j];
		//printf ("%d", parity[j]?1:0);
		/*if (parity[i]) {
			break;
		}*/
	}
	//printf ("\n");
	//cin >> stop;
	//printf ("Case #%d: ", t+1);
	outpfile << "Case #" << t+1 << ": ";
	if (!YN) {
		//printf ("%d", Seans - small);
		outpfile << Seans-small;
	} else {
		//printf ("NO");
		outpfile << "NO";
	}
	//printf ("\n");
	outpfile << "\n";
	N = num;
	//cout << "N = " << N << endl;
}

void TEST (C_N T) {
	cout << "==void TEST ()" << endl;
	outpfile.open(OUTPFN.c_str());
	for (t = 0, impfile >> N; t < T; t++) {
		CASE();
	}
	outpfile.close();
}

int main () {
	cout << "==int main ()" << endl;
	impfile.open(IMPFN.c_str());
	impfile >> T;
	TEST(T);
	impfile.close();
	cout << "End of Program" << endl;
	return 0;
}
