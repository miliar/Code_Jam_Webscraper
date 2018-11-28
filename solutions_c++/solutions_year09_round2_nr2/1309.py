#include <iostream>
using namespace std;
int main() { int tmax; cin >> tmax;
	for (int t = 1; t <= tmax; t++) { int N; cin >> N;
		int DD[10]; for(int i=0; i<10; i++) { DD[i] = 0; }

		for (int d = N; d; d = (d-d%10)/10) { if (d%10!=0) DD[d%10]++; }

		while (1) { N++; int dd[10]; for(int i=0; i<10; i++) { dd[i] = DD[i]; }
			for (int d = N; d; d = (d-d%10)/10) { if (d%10!=0) dd[d%10]--; }
			
			bool ok = true; 
			for(int i=0; i<10; i++) { if (dd[i] != 0) ok = false; }
			if (ok) break;
		}

		printf("Case #%d: %d\n",t,N);
	}
}
