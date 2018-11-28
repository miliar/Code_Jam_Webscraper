#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i < (n); i++)
#define forn(i,n) forsn(i,0,(n))
#define dforsn(i,s,n) for(int i=(n)-1;i>=(s);i--)
#define dforn(i,n) dforsn(i,0,(n))
#define abs(x) ((x)<0?-(x):(x))

typedef long long tint;

#define INF 100000000

char d[200][200];
int k, w;

bool isvalid(int x, int y) {
	return (x >= 0) && (y >= 0) && (x < w) && (y < w);
}

int dsize(int _k) {
	return _k*_k;
}

int main() {
	tint T;
	cin >> T;
	forn(icase,T) {
		cin >> k;
		cin.ignore();
		
		w = 2*k-1;
		
		forn(i,w+1) forn(j,w+1) d[i][j] = ' ';
		
		forn(y,w) cin.getline(d[y], w+2);
		
		int dmin = INF;
		
		
		forn(cy,w) forn(cx,w) {
			bool cvalid = true;
			
			forn(y2,w) {
				forn(x2,w) {
					if (d[y2][x2] < '0' || d[y2][x2] > '9') continue;
					
					int dx = abs(x2-cx), dy = abs(y2-cy);
					int dcx[4] = {-1, 1, -1, 1};
					int dcy[4] = {-1, 1, 1, -1};
					
					bool valid = true;
					forn(i,4) {
						int nx = cx+dcx[i]*dx;
						int ny = cy+dcy[i]*dy;
						
						if (isvalid(nx, ny) && d[ny][nx] != ' ') {
							/*
							if (icase == 2 && cx == 1 && cy == 1 && x2 == 0) {
								cout << x2 << " " << y2 << " -" << d[y2][x2] << "-" << endl;
								cout << "..." << dx << " " << dy << endl;
								cout << "   " << nx << " " << ny << " " << d[ny][nx] << endl;
								cout << i << endl;
							}
							*/
							
							if (d[y2][x2] != d[ny][nx]) {
								//if (icase == 2 && cx == 1 && cy == 1 && x2 == 0)cout << "INV" << endl;
								valid = false;
								break;
							}
						}
					}
					if (!valid) {
						cvalid = false;
						break;
					}
				}
				if (!cvalid) break;
			}
			
			if (cvalid) {
				int CX = k-1, CY = k-1;
				int newk = k + abs(CX-cx) + abs(CY-cy);
				//if (icase == 2) cout << "NUEVO K " << newk << " -- " << cx << " " << cy << endl;
				dmin = min(dmin, newk);
			}
		}
		
		int sol = dsize(dmin) - dsize(k);
		cout << "Case #" << (icase+1) << ": " << sol << endl;
		
		
	}
	return 0;
}
