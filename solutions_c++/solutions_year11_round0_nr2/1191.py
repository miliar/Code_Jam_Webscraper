#include <iostream>
using namespace std;

//int main()
int main (int argc, char * const argv[]) 
{
	freopen("input2.txt", "rt", stdin);
	freopen("output2.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	char combine[36][3];
	char opposed[28][2];
	char target[100];
	for(int i = 0; i < T; i++) {

		int C;
		cin >> C;
		for (int j = 0; j < C; j++) {
			cin >> combine[j][0] >> combine[j][1] >> combine[j][2];
		}
		
		int D;
		cin >> D;
		for (int j = 0; j < D; j++) {
			cin >> opposed[j][0] >> opposed[j][1];
		}
		
		int N;
		cin >> N;
		int ptr = 0;
		for (int j = 0; j < N; j++) {
			char m;
			cin >> m;//source[j];
			
			int combined = 0;
			//	combine
			if (ptr > 0) {
				for (int k = 0; k < C; k++) {
					if ((m == combine[k][0] && target[ptr-1] == combine[k][1]) ||
						(m == combine[k][1] && target[ptr-1] == combine[k][0]))	{
						target[ptr-1] = combine[k][2];
						combined = 1;
						break;
					}
				}
			}
			
			//	oppose
			int clear = 0;
			if (combined == 0) {
				for (int k = 0; k < ptr && clear == 0; k++) {
					for (int l = 0; l < D && clear == 0; l++) {
						if ((m == opposed[l][0] && target[k] == opposed[l][1]) ||
							(m == opposed[l][1] && target[k] == opposed[l][0])) {
							clear = 1;
							break;
						}
					}
				}
				if (clear == 1)
					ptr = 0;
			}
			
			if (combined == 0 && clear == 0) {
				target[ptr++] = m;
			}
		}
		
		
		cout << "Case #" << i+1 << ": [";
		
		for (int k = 0; k < ptr; k++) {
			cout << target[k];
			if (k != ptr-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	
	return 0;
}

