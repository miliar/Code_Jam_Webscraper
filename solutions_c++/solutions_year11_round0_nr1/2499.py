#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

int main()
{
    int T, N;
	int t;
	long v1, u1, v2, u2;
	long k;
	char c[120];
	int x[120];
	fin>>T;
    for (int t = 1; t <= T; ++t)
    {
		v1 = u1 = 1;
		v2 = u2 = 0;

		fin>>N;
		for(k=0; k<N; ++k) {
			fin>>c[k]>>x[k];
		}
		for(k=0;k<N;++k) {
			if(c[k] == 'O') {
				v2 += abs(x[k] - v1);
				++v2;
				v1 = x[k];
				if(v2<= u2)
					v2 = u2+1;
			}
			else {
				u2 += abs(x[k]- u1);
				u2++;
				u1 = x[k];
				if(u2<=v2)
					u2 = v2+1;
			}
		}

		fout<<"Case #"<<t<<": ";
		if(v2 < u2) {
			fout<<u2<<endl;
		}
		else {
			fout<<v2<<endl;
		}   
    }
	return 0;
}
