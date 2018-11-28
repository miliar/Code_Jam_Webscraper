#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <list>
#include <vector>

#define REP(i,n) for (int i = 0; i < n; i++)
#define FOR(i,n,m) for (int i = n; i <= m; i++)
#define FORD(i,n,m) for (int i = n; i >= m; i--)
#define FOREACH(a,c) for (typeof((c).begin()) a = (c).begin(); a != (c).end(); a++)

typedef long long int LL;
//typedef set<int> SI;
//typedef list<int> LI;

int T;

int main(){
	scanf ("%d", &T);
	REP(x,T){
		int N;
		scanf("%d", &N);
		int cx=0, cy=0, cz=0;
		int wx=0, wy=0, wz=0;
		REP(i,N){
			int x,y,z,vx,vy,vz;
			scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
			cx += x; cy += y; cz += z;
			wx += vx; wy += vy; wz += vz;
		}
		double SW = wx*wx+wy*wy+wz*wz; double t = 0;
		if (SW != 0)
			t = double(-wx*cx - wy*cy - wz*cz)/double(wx*wx+wy*wy+wz*wz);
		t = t >= 0 ? t : 0; 
		double Sx, Sy, Sz;
		Sx = cx + t*wx;
		Sy = cy + t*wy;
		Sz = cz + t*wz;
		double S = sqrt(Sx*Sx+Sy*Sy+Sz*Sz)/double(N);
		printf ("Case #%d: %.8lf %.8lf\n",x+1, S,  t);

	}
	return 0;
}
