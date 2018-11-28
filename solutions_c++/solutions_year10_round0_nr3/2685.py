#include <iostream>
#include <vector>

using namespace std;

int main() {

      int T=0;
      long long R=0;
      long long k =0;
      int N=0;
      vector<long long> vecGrp;
      long long s=0;
      int index=0;
      long long c=0;
      long long mny=0;
      int count = 0;

      long long gR = 0;

      cin >> T;
	
      for(int i=0; i<T; i++) {

	    cin >> R;
	    cin >> k;
	    cin >> N;

	    vecGrp.clear();

	    for(int j=0; j<N; j++) {
		  cin >> s;
		  vecGrp.push_back(s);
	    }

	    index = 0;
	    mny = 0;
	    gR = 0;

	    for(long long m=0; m<R; m++) {

		  c=0;

		  count = 0;

		  while(c <= k) {

			c = c + vecGrp[index];

			if( c <= k) {
			      index++;
			      if(index == N) index = 0;

			      count++;
			      if(count == N) break;
			}

		  }

		  if(count == N) {
			if(index == 0)
			      gR = m+1;
		  }

		  if(count != N || c > k ) {
			if(index == 0) gR = m+1;
			c = c - vecGrp[index];
		  }
		  mny = mny + c;

		  if(gR > 0) break;

	    }

	    if(gR > 0) {

		  mny = mny * (R/gR);

		  int rem = R%gR;

		  for(long long m=0; m<rem; m++) {

			c=0;

			count = 0;

			while(c <= k) {

			      c = c + vecGrp[index];

			      index++;
			      if(index == N) index = 0;

			      count++;
			      if(count == N) break;

			}

			if(count != N || c > k ) {
			      if(index == 0) {
				    index = N-1;
			      }
			      else index--;
			      c = c - vecGrp[index];
			}
			mny = mny + c;
		  }
	    }

	    cout << "Case #" << (i+1) << ": " << mny << endl;

      }
}
