#include <iostream>
#include <string>
#include <vector>
using namespace std;

int w[600][600];
int wac[600][600];

int area(int r, int c, int r2, int c2) {
	return wac[r2][c2]-wac[r][c2]-wac[r2][c]+wac[r][c];
}

int main(void) {
	int T;
	cin >> T;
	for(int tc=1; tc<=T; tc++) {
		int R,C,D;
		cin >> R >> C >> D;
		for(int r=0; r<R; r++)
			for(int c=0; c<C; c++) {
				char x;
				cin >> x;
				w[r][c]=x-'0';
			}
		memset(wac, 0, sizeof(wac));
		for(int r=0; r<R; r++) {
			for(int c=0; c<C; c++) {
				wac[r+1][c+1] = wac[r][c+1]+wac[r+1][c]-wac[r][c]+w[r][c];
				//cout << wac[r+1][c+1] << " ";
			}
			//cout << endl;
		}

		int bestK=0;
		for(int K=max(R,C); K>=3; K--) {
			for(int r=0; r+K<=R; r++)
				for(int c=0; c+K<=C; c++) {
					//int top = area(r,c,r+K/2,c+K)-w[r][c]-w[r][c+K-1];
					//int bottom = area(r+K-K/2,c,r+K,c+K)-w[r+K-1][c]-w[r+K-1][c+K-1];
					//if(r==1 && c==1 && K==5) cout << top << "," << bottom << endl;
					//if(top!=bottom) continue;
					//int left = area(r,c,r+K,c+K/2)-w[r][c]-w[r+K-1][c];
					//int right = area(r,c+K-K/2,r+K,c+K)-w[r][c+K-1]-w[r+K-1][c+K-1];
					//if(left!=right) continue;
					int cr=0;
					int cc=0;
					for(int r1=r; r1<r+K; r1++)
						for(int c1=c; c1<c+K; c1++) {
							if(r1==r && c1==c) continue;
							if(r1==r+K-1 && c1==c) continue;
							if(r1==r && c1==c+K-1) continue;
							if(r1==r+K-1 && c1==c+K-1) continue;
							cr += (2*r1-2*r-(K-1))*w[r1][c1];
							cc += (2*c1-2*c-(K-1))*w[r1][c1];
						}
					if(cr || cc) continue;
					//cout << r << " " << c << " " << K << endl;
					//if(r==1 && c==1 && K==5) cout << left << "," << right << endl;
					bestK=K;
				}
			if(bestK) break;
		}
		cout << "Case #" << tc << ": ";
		if(bestK) cout << bestK;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
}
