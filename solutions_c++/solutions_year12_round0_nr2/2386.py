#include "scc/cj.h"		// http://github.com/lvv/scc


int main() {
	size_t tt(in);  NL;

	for(size_t t=1;  t<=tt;  t++)  {
		cout << "Case #" <<  t << ": ";
		long N(in); 
		long S(in); 
		long P(in); 
		vlong T = in(N);
		sort(+T,-T);
		NL;
							//__ "\nS: ", S; __ "P: ", P; __ T;

		long cnt=0;
		
		while (!T) {
			if ((T++ / 3 ) + (T++ %3?1:0) >= P) {
							//_ "I:", T++;
				cnt++;
				T--;
							//__ T, cnt;
			} else {
				break;
			}
		}


		while (!T  &&  S-->0) {
			long a = (T++ +1)/3;
			if (a >= 1  && a >= P-1) {
							//_ "II:", T++;
				cnt++;
				T--;
							//__ T, a, S, cnt;
			} else {
				break;
			}
		}

		__ cnt;

	}
}
