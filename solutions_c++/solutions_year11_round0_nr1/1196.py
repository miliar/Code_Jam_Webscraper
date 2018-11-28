#include <iostream>
using namespace std;

int main()
{
	freopen("input1.txt", "rt", stdin);
	freopen("output1.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	int R[100], P[100];
	for(int i = 0; i < T; i++) {
		int N;
		cin >> N;
		
		for (int j = 0; j < N; j++) {
			char C;
			cin >> C;
			R[j] = (C == 'O' ? 0 : 1);
			cin >> P[j];
		}
		
		int step = 0, opos = 1, bpos = 1;
		
		for (int k = 0; k < N; k++) {
			int nexto = -1, nextb = -1;
			for (int k1 = k; k1 < N; k1++) {
				if (R[k1] == 0) {
					if (nexto == -1)
						nexto = P[k1];
				}
				else {
					if (nextb == -1)
						nextb = P[k1];
				}
				if (nexto != -1 && nextb != -1)
					break;
			}
			
			int b = 1;
			while (b == 1) {
				step++;
				if (nexto != -1)	{
					if (opos < nexto) {
						opos++;
					}
					else if (opos > nexto){
						opos--;
					}

					else {
						if (R[k] == 0)
							b = 0;
					}
				}
				if (nextb != -1)	{
					if (bpos < nextb) {
						bpos++;
					}
					else if (bpos > nextb){
						bpos--;
					}
					else {
						if (R[k] == 1)
							b = 0;
					}
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << step << endl;
	}
	
	return 0;
}

