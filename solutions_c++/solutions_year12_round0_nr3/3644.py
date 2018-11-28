#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream ifs(argv[1]);
	ofstream ofs("output");

	int T, A, B;
	ifs >> T;
	int N, y;

	for (int i = 1; i <= T; ++i) {
		y = 0;
		ifs >> A >> B;
		int	DIG_111 = 1;
		int DIG_NUM = log10((double)A);
		for (int j = 0; j < DIG_NUM; ++j)
			DIG_111 = DIG_111 * 10 + 1;

		for (int N = A; N <= B; ++N) {
			if (N%DIG_111 != 0) {
				int n = N;
				int LAST = 0;							
				for (int j = 0; j < DIG_NUM; ++j) {
					n = pow((double)10,DIG_NUM)*(n%10) + n/10;				
					if (n >= N && n<=B && N!=n && n != LAST) {
						y++;
						LAST = n;
					 	//cout << N << "-" << n << endl;
					}
				}
			}
		}
            
		ofs << "Case #" << i << ": " << y << endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}
