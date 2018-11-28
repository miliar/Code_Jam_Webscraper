#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

int main(){
	ifstream cin ("A-large.in");
	ofstream cout("output.txt");
	int T;
	cin >>T;
	For(q,1,T+1){
		char R;
		int N, P;
		int O = 1, B = 1;
		int tO = 0, tB = 0;
		int t;
		bool isO;
		cin >> N >> R >> P;
		if (isO = (R == 'O'))
			t = O = tO = P;
		else
			t = B = tB = P;
		For(i,1,N){
			cin >> R >> P;
			if (R == 'O'){
				int w = abs(P - O);
				if (!isO)
					if (w + tO < tB){
						tO = tB + 1;
						++t;
					}
					else{
						t += tO + w + 1 - tB;
						tO += w + 1;
					}
				else{
					tO += w+1;
					t += w+1;
				}
				O = P;
			}
			else{
				int w = abs(P - B);
				if (isO)
					if (w + tB < tO){
						tB = tO + 1;
						++t;
					}
					else{
						t += tB + w + 1 - tO;
						tB += w + 1;
					}
				else{
					tB += w+1;
					t += w+1;
				}
				B = P;
			}
			isO = (R == 'O');
		}
		cout << "Case #" << q << ": " << t << endl;
	}
	return 0;
}