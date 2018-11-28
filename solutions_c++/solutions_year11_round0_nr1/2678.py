#include <iostream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n;

int moves[105];
bool done[105];
char mover[105];

int abs(int x) {
	return x > 0 ? x : -x;
}
int sign(int x) {
	return x > 0 ? 1 : -1;
}

int main() {
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> n;
		
		for0(i, 105) done[i] = false;
				
		for0(i,n)
			cin >> mover[i] >> moves[i];
		
		int oPos = 1, bPos = 1;
		int time = 0;
		
		for0(i,2*n) {
			int nextb = -1, nexto = -1;
			for (int j = i; j < n; j ++) {
				if (!done[nexto] && nexto < 0 && mover[j] == 'O') nexto = j;
				if (!done[nexto] && nextb < 0 && mover[j] == 'B') nextb = j;
			}
			
			if (nextb >= 0 && (nexto == -1 || nextb < nexto)) {
				int dt = abs(moves[nextb] - bPos) + 1;
				done[nextb] = true;
				bPos = moves[nextb];
				if (nexto >= 0) {
					int d0 = moves[nexto] - oPos;
					oPos += abs(d0) < dt ? d0 : sign(d0)*dt;
				}
				time += dt;
			} else if (nexto >= 0) {
				int dt = abs(moves[nexto] - oPos) + 1;
				done[nexto] = true;
				oPos = moves[nexto];
				if (nextb >= 0) {
					int db = moves[nextb] - bPos;
					bPos += abs(db) < dt ? db : sign(db)*dt;
				}
				time += dt;
			} else break;
		}
		
		cout << "Case #" << (kase+1) << ": " << time;
		if (kase != kases-1) cout << endl;
	}
}