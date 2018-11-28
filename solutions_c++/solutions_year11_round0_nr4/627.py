#include<scc/simple.h>
int main() {
	int T(in);
	for (int case_=1;  case_<=T;  case_++) {
		cout << "Case #" << case_ << ": ";
		long N(in);
		vlong V(N);   cin >> V;
		vlong VV(V);
		sort(VV.bb, VV.ee);
		long cnt=0;

		for (long i=0;  i<N;  i++) 
			if(V[i] != VV[i]) cnt++;
		cout << cnt;
		cout << endl;
	}
}
