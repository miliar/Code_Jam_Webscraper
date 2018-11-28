#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<queue>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

struct state {
	int x,y;
	int aX,aY,aD;
	int bX,bY,bD;
	state(): x(0), y(0), aX(0), aY(0), aD(0), bX(0), bY(0), bD(0) { }
};

int tabD[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

int sToI(const state&A) {
	int res = 0;
	res += A.x; res <<= 4;
	res += A.y; res <<= 5;
	res += (A.aX+1); res <<= 5;
	res += (A.aY+1); res <<= 2;
	res += A.aD; res <<= 5;
	res += (A.bX+1); res <<= 5;
	res += (A.bY+1); res <<= 2;
	res += A.bD;
	return res;
}

state iToS(int k) {
	state res;
	res.bD = k&3; k >>= 2;
	res.bY = (k&31)-1; k >>= 5;
	res.bX = (k&31)-1; k >>= 5;
	res.aD = k&3; k >>= 2;
	res.aY = (k&31)-1; k >>= 5;
	res.aX = (k&31)-1; k >>= 5;
	res.y = k&15; k >>= 4;
	res.x = k&15; k >>= 4;
	return res;
}

map<int,int> M;
priority_queue<pair<int,int> > Q;
char tab[20][20];
int n,m;

bool isIn(int x, int y) {
	return x<n && x>=0 && y<m && y>=0;
}

void tryAdd(const state &s, int val) {
	//printf("tryAdd x=%d y=%d\n",s.x,s.y);
	int num = sToI(s);
	//printf("num=%d\n",num);
	map<int,int>::iterator it=M.find(num);
	if(it==M.end()) {
	//	printf("A\n");
		M.insert(MP(num,val));
		Q.push(MP(-val,num));
	} else if(it->SE>val) {
	//	printf("B\n");
		M[num] = val;
		Q.push(MP(-val,num));
	}
}

void testcase(int tNum) {

	M.clear();
	while(!Q.empty()) Q.pop();
	
	scanf("%d %d",&n,&m);
	FOR(i,0,n) scanf("%s",tab[i]);
	
	int eX, eY, sX, sY;
	FOR(i,0,n) FOR(j,0,m) if(tab[i][j]=='X') {
		eX = i;
		eY = j;
		tab[i][j] = '.';
	} else if(tab[i][j]=='O') {
		sX = i;
		sY = j;
		tab[i][j] = '.';
	}
	
	state start;
	start.x=sX; start.y=sY;
	int vS = sToI(start);
	Q.push(MP(0,vS));
	M.insert(MP(vS,0));
	
	int res = -1;
	
	while(Q.size()) {
		int num=Q.top().SE;
		int val=M[num];
		Q.pop();
		if(val==-1) continue;
		M[num] = -1;
		state s = iToS(num);
		//printf("x=%d y=%d ax=%d ay=%d ad=%d bx=%d by=%d bd=%d val=%d\n",s.x,s.y,s.aX,s.aY,s.aD,s.bX,s.bY,s.bD,val);
		if(s.x==eX && s.y==eY) {
			res = val;
			break;
		}
		FOR(d,0,4) {
			int nX=s.x+tabD[d][0], nY=s.y+tabD[d][1];
			if(isIn(nX,nY) && tab[nX][nY]=='.') {
				state next = s;
				next.x = nX; next.y = nY;
				tryAdd(next,val+1);
			}
			if(s.aX==nX && s.aY==nY && s.aD==d && (s.bX!=0 || s.bY!=0 || s.bD!=0)) {
				state next = s;
				next.x = s.bX; next.y = s.bY;
				int nD = (next.bD+2)%4;
				next.x += tabD[nD][0]; next.y += tabD[nD][1];
				tryAdd(next,val+1);
			}
			while(isIn(nX,nY) && tab[nX][nY]=='.') {
				nX += tabD[d][0];
				nY += tabD[d][1];
			}
			if(true) {
				state next = s;
				next.aX = nX; next.aY = nY; next.aD = d;
				tryAdd(next,val);
				next = s;
				next.bX = nX; next.bY = nY; next.bD = d;
				tryAdd(next,val);
			}
		}
	}
	
	printf("Case #%d: ",tNum);
	
	if(res==-1) 
		printf("THE CAKE IS A LIE\n"); else
		printf("%d\n",res);
	
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
