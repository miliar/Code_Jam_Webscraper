#include <simple.h>


int main() {
	int CASES;
	cin  >> CASES;		NL;

	for ( int case_=1;   case_<=CASES ;   case_++)  {

		int R, k, N; 	// rides;  max ppl in ride;  groups
		cin  >> R >> k >> N;	NL
		int G[1000000];
		for (int i=0;  i<N; i++)  cin >> G[i];

		int q = 0, save_q, start_q;  // qeue start
		int sum = 0;
		long earn = 0;
		int g;		

		for (int r=0;  r<R;  r++)  {
			start_q = q;
							//cout << "r:" << r; 
			// fill
			while (1) {
				g = G[q];
				sum += g;		//PR(g)  
				save_q  = q;
				q  =  (q+1) % N;
				if (sum > k) {
					sum -= g;	//PR(sum)  PR(q)
					q = save_q;
					break;
				}
				if (q == start_q)
					break;
			}

							//cout	<< "\t" << earn << " += " << sum << endl;
			earn += sum;
			sum = 0;
		}

		cout << "Case #" << case_ << ": " << earn << endl;
		
		
	}
	return 0;
}
