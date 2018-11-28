#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char * const argv[]) {
	
	ifstream f(argv[1]);
	
	if (!f.fail())
	//while (!f.eof())
	{
		int T,N,K;
		f >> T;
		for (int t = 0; t < T; t++) {
			f >> N;
			f >> K;
			
			unsigned int p = (1 << N) ;
			K = K % p;
			if (K == p-1)
				cout << "Case #" << t+1 << ": ON" << endl;
			else
				cout << "Case #" << t+1 << ": OFF" << endl;
		}
	}
    return 0;
}
