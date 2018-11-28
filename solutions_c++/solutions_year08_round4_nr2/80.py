#include <iostream>
using namespace std;

int main() {
	
	int Nx;
	cin >> Nx;
	for(int nx = 1; nx <= Nx; ++nx) {
		cout << "Case #" << nx << ": ";

		int N, M, A;
		cin >> N >> M >> A;
		
		// case 1
		for(int x2 = 0; x2 <= N; ++x2) {
			for(int x3 = 0; x3 <= N; ++x3) {
				for(int y2 = 0; y2 <= M; ++y2) {
					for(int y3 = 0; y3 <= M; ++y3) {
						int A0 = x3*y2-x2*y3;
						if(A0 == A || A0 == -A) {
							cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3;
							goto foundit;
						}
					}
				}
			}
		}
		
		// case 2
		/*for(int x2 = 0; x2 <= N; ++x2) {
			for(int x3 = 0; x3 <= N; ++x3) {
				for(int y1 = 0; y1 <= M; ++y1) {
					for(int y3 = 0; y3 <= M; ++y3) {
						int A0 = -x3*y1-x2*(y3-y1);
						if(A0 == A || A0 == -A) {
							cout << "0 " << y1 << " " << x2 << " 0 " << x3 << " " << y3;
							goto foundit;
						}
					}
				}
			}
		}*/
		
		cout << "IMPOSSIBLE";
		foundit:
		cout << endl;
	}
	
}
