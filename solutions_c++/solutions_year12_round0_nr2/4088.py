#include <iostream>
#include <fstream>
using namespace std;

#define MIN(a, b) ((a) <= (b) ? (a) : (b))

int main(){
	fstream in("in.txt", fstream::in);
	fstream out("out.txt", fstream::out);
	int T; in >> T;
	for(int t = 0; t < T; t++){
		int N, S, p, *tri;
		in >> N >> S >> p;
		tri = new int [N];
		for(int n = 0; n < N; n++)
			in >> tri[n];
		int norm = 0, surponly = 0;
		for(int n = 0; n < N; n++){
			if( tri[n] >= 3 * p - 2) norm++;
			if((tri[n] >= 2) && (tri[n] <= 28)){
				if((tri[n] == 3 * p - 4) || (tri[n] == 3 * p - 3)) surponly++;
			}
		}
		int res = norm + MIN(S, surponly);
		out << "Case #" << t + 1 << ": " << res << endl;
		delete[] tri;
	}
	return 0;
}
