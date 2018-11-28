#include <iostream>

using namespace std;

int ABS(int a){ return ( a < 0 ? -a : a ); }

int main()
{
	int T, P, N;
	int t_last_O, t_last_B, t_curr, t_d;
	int O, B;

	char k; int spot;

	cin >> T;
	for (int z = 1; z <= T; z++){	
		t_last_O = 0; t_last_B = 0; t_curr = 0;
		O = 1, B = 1;
		cin >> N;
		for (int i = 0; i < N; i++){
			cin >> k >> spot;
			if (k == 'O'){
				t_d = ABS( spot - O );
				if ( t_last_O + t_d + 1 <= t_curr ){
					t_curr++;
					t_last_O = t_curr;
					O = spot;
				}
				else{
					t_curr += ( t_last_O + t_d + 1 ) - t_curr;
					t_last_O = t_curr;
					O = spot;
				}
			}
			else if (k == 'B'){
				t_d = ABS( spot - B );
				if ( t_last_B + t_d + 1 <= t_curr ){
					t_curr++;
					t_last_B = t_curr;
					B = spot;
				}
				else{
					t_curr += ( t_last_B + t_d + 1 ) - t_curr;
					t_last_B = t_curr;
					B = spot;
				}
			}
		}
  		cout << "Case #" << z << ": " << t_curr << endl;
	}
	return 0;
}
