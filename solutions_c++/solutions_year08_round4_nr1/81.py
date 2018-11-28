#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	
	int Nx;
	cin >> Nx;
	for(int nx = 1; nx <= Nx; ++nx) {
		cout << "Case #" << nx << ": ";

		// TODO
		int M, V;
		cin >> M >> V;
		
		vector<int> G(M), C(M), A0(M), A1(M);
		int i;
		for(i = 0; i != (M-1)/2; ++i) {
			cin >> G[i] >> C[i];
		}
		for(; i != M; ++i) {
			int W;
			cin >> W;
			if(W) {
				A0[i] = 1000000;
			}
			else {
				A1[i] = 1000000;				
			}
		}
		
		for(i = (M-1)/2-1; i >= 0; --i) {
			A0[i] = 1000000;
			A1[i] = 1000000;
			if(G[i] == 1 || C[i]) A0[i] = min(A0[i], (G[i]!=1) + min(A0[2*i+1], A0[2*i+2]));
			if(G[i] == 0 || C[i]) A0[i] = min(A0[i], (G[i]!=0) + A0[2*i+1] + A0[2*i+2]);
			if(G[i] == 0 || C[i]) A1[i] = min(A1[i], (G[i]!=0) + min(A1[2*i+1], A1[2*i+2]));
			if(G[i] == 1 || C[i]) A1[i] = min(A1[i], (G[i]!=1) + A1[2*i+1] + A1[2*i+2]);
		}
		
		int A = V ? A1[0] : A0[0];
		if(A == 1000000) cout << "IMPOSSIBLE";
		else cout << A;
		
		cout << endl;
	}
	
}
