
#include<fstream>
#include <set>

int main() {
	int T = 0;
	std::ifstream fin("GCJ2012_C_IN.txt");
	std::ofstream fout("GCJ2012_C_OUT.txt");
	fin >> T;
	const int pow10[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
	std::set<int> mset;
	
	for (int i = 0; i < T; ++i)	{
		int A = 0, B = 0;
		unsigned long K = 0;
		fin >> A >> B;
		A = (A < 11)? 11 : A;
		
		if (A < B) {
			for (int n = A; n < B; ++n) {
				int p = 1, q = 1, m = 0;
				
				while (n / pow10[q]) {
					++q;
				}
				mset.clear();

				while (n / pow10[p]) {
					int m = (n % pow10[p]) * pow10[q - p] + n / pow10[p];
					if (m > n && m <= B) {
						mset.insert(m);
					}
					++p;
				}
				K += (unsigned long) (mset.size());
			}
		}
		fout << "Case #" << (i + 1) << ": " << K;
		
		if (i < T - 1) {
			fout << std::endl;
		}
	}
	fin.close();
	fout.flush();
	fout.close();
	return 0;
}
