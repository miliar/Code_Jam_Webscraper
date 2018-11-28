#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <ctime>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (int i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

char cmap[30][30];
int H,W,D;
int startx,starty;
int MX,MY;

int cx,cy,ox,oy,dx,dy;
int gone,maxgonesq;

int light() {
//	cout << "light ("<<cx<<","<<cy<<") off ("<<ox<<","<<oy<<")" << endl;
	if(gone*gone > maxgonesq)
		return 0;

	if(dx!=0) { // ox -> MX  <or>  ox -> 0
		int e=(dx>0 ? MX-ox : ox);
		int noy = oy+(dy*e);

		if(cx == startx && cy == starty && e==MX && noy+oy == MY) {
			gone+=e/2;
			if(gone*gone<=maxgonesq)
				return 1;
			else
				return 0;
		}

		if(noy > 0 && noy < MY) {
			gone += e;
			oy=noy;
			if(cmap[cx+dx][cy] == '#') {
				if(dy==0) {
					gone*=2;
					if(gone*gone <= maxgonesq)
						return 1;
					else
						return 0;
				}
				ox=(dx>0 ? MX : 0),dx=-dx;
			}
			else
				ox=(dx>0 ? 0 : MX),cx+=dx;
			return light();
		} else if(noy==0 || noy==MY) {
			gone += e;
			if(cmap[cx+dx][cy+dy] != '#') {
				ox=(dx>0 ? 0 : MX),cx+=dx;
				oy=(dy>0 ? 0 : MY),cy+=dy;
			} else if(cmap[cx+dx][cy] == '#' && cmap[cx][cy+dy] == '#') {
				gone*=2;
				if(gone*gone <= maxgonesq)
					return 1;
				else
					return 0;
			} else if(cmap[cx+dx][cy] == '#' && cmap[cx][cy+dy] != '#') {
				ox=(dx>0 ? MX : 0),dx=-dx;
				oy=(dy>0 ? 0 : MY),cy+=dy;
			} else if(cmap[cx+dx][cy] != '#' && cmap[cx][cy+dy] == '#') {
				ox=(dx>0 ? 0 : MX),cx+=dx;
				oy=(dy>0 ? MY : 0),dy=-dy;
			} else
				return 0;
			return light();
		}
	}


	if(dy!=0) { // oy -> MY  <or>  oy -> 0
		int e=(dy>0 ? MY-oy : oy);
		int nox = ox+(dx*e);

		if(cx == startx && cy == starty && e==MY && nox+ox == MX) {
			gone+=e/2;
			if(gone*gone<=maxgonesq)
				return 1;
			else
				return 0;
		}

		if(nox > 0 && nox < MX) {
			gone += e;
			ox=nox;
			if(cmap[cx][cy+dy] == '#') {
				if(dx==0) {
					gone*=2;
					if(gone*gone <= maxgonesq)
						return 1;
					else
						return 0;
				}
				oy=(dy>0 ? MY : 0),dy=-dy;
			}
			else
				oy=(dy>0 ? 0 : MY),cy+=dy;
			return light();
		}
		else
			cout << "ERROR!!!!!" << endl, exit(0);
	}

	cout << "ERROR2!!!!!" << endl, exit(0);
	return 0;
}


int gcd(int a, int b) {
	return b ? gcd(b,a%b) : a;
}

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cin >> H >> W >> D;
		FOR(y,0,H) FOR(x,0,W){
			cin >> cmap[x][y];
			if(cmap[x][y] == 'X')
				startx = x, starty = y, cmap[x][y]='.';
		}
		int res=0;
		FOR(dX,-D,D+1) FOR(dY,-D,D+1) if((dX || dY) && abs(gcd(dX,dY))==1) {
			if(!dX || !dY) {
				MX = MY = 2;
				maxgonesq = 4*D*D;
			} else {
				MX = 2*abs(dY);
				MY = 2*abs(dX);
				maxgonesq = (4ll*(ll)D*(ll)D*(ll)dX*(ll)dX*(ll)dY*(ll)dY)/((ll)dX*(ll)dX+(ll)dY*(ll)dY);
			}
			dx=dX ? dX/abs(dX) : 0;
			dy=dY ? dY/abs(dY) : 0;
			cx=startx;
			cy=starty;
			ox = MX/2;
			oy = MY/2;
			gone=0;
			int nres = light();
			if(nres) {
			//	cout << "dX=" << dX << ", dY=" << dY << " got " << nres << endl;
			//	cout << "maxgonesq=" << maxgonesq << ", gonesq=" << gone*gone << endl;
			}
			res+=nres;
		}
		cout << "Case #" << ctc << ": ";
		cout << res << endl;
	}
	return 0;
}
