#include "scc/cj.h"		// http://github.com/lvv/scc
//#include "lvv/lvv.h"


int main() {
	size_t tt(in);  NL;

	for(size_t t=1;  t<=tt;  t++)  {
		cout << "Case #" <<  t << ": ";
		long A(in), B(in);

		str s; 
		ostringstream oss;
		oss << A;
		long N = oss.str().size();
										// __ A, B, N;
		long ten[10] {1,10,100,1000,10000,100000, 1000000, 10000000, 100000000, 1000000000};
		vlong save;
		long cnt = 0;
	

		for (long x = A;  x <= B;   x++) {

			save.clear();
			for (long n=1;   n <= N-1;   n++)  {

					long h = x / ten[n];
					long H = h * ten[n];
					long l = x - H;
					long L = l * ten[N-n];
					long X = L+h;

											
					if ( X <= B  &&  x < X  &&  X >= A  &&  find(+save,-save,X)==-save)  {
						cnt++;
						save << X; 
										// cerr <<  "++  ";
					} 					// else cerr <<  "--  ";
										// PR7(n,x,h,H,l,L,X);
			}
		}
		__ cnt;
	}
}
