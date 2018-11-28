#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    unsigned int T, N;
    cin >> T;
    for (unsigned int k = 0; k < T; k++){
		cin >> N;
        cout << "Case #" << k+1 << ": ";
		
		int pos_O = 1, pos_B = 1;
		int t_O = 0, t_B = 0;
		for (unsigned int i = 0; i < N; i++){
			char R;
			int P;
			cin >> R >> P;
			if (R == 'B'){
				int diff = pos_B - P; if (diff < 0) diff = -diff;
				t_B = max(t_B + diff+1, max(t_B, t_O)+1);
				pos_B = P;
			} else {
				int diff = pos_O - P; if (diff < 0) diff = -diff;
				t_O = max(t_O + diff+1, max(t_B, t_O)+1);
				pos_O = P;
			}
		}	
		cout << max(t_O, t_B) << endl;
    }
    return 0;
}
