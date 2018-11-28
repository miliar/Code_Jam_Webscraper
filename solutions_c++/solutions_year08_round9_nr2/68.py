#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<set>
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

const int INF = 1000003;

int gcd(int a, int b) {
	if(a<0) a=-a;
	if(b<0) b=-b;
	return (b==0)?a:gcd(b,a%b);
}

//==================================
//	Extended Euclid algorithm
//	ax + by = d, where d=gcd(a,b)
//	a >= b!
//	Be careful with int range!
//==================================
int egcd(int a, int b, int &x, int &y) {
	if(b==0) {
		x=1, y=0;
		return a;
	} else {
		int x1, y1;
		int d = egcd(b, a%b, x1, y1);
		x=y1, y=x1-(a/b)*y1;
		return d;
	}
}

int X,Y,aX,aY,bX,bY;

bool isIn(LL x, LL y) {
	return x>=0 && x<X && y>=0 && y<Y;
}

void testcase(int tNum) {
	printf("Case #%d: ",tNum);	
	scanf("%d %d %d %d %d %d",&X,&Y,&aX,&aY,&bX,&bY);
	LL sX,sY;
	scanf("%lld %lld",&sX,&sY);
	
	/*if(tNum==36) {
		printf("%d %d %d %d %d %d %d %d\n",X,Y,aX,aY,bX,bY,sX,sY);
	}*/
	
	if(!isIn(sX,sY)) {
		printf("%d\n",0);
		return;
	}
	
	LL res = 0;
	
	if(abs(aX*bY)==abs(aY*bX)) {
		set<pair<int,int> > S;
		queue<pair<int,int> > Q;
		S.insert(MP(sX,sY));
		Q.push(MP(sX,sY));
		while(!Q.empty()) {
			res++;
			pair<int,int> P = Q.front();
			Q.pop();
			pair<int,int> nP;
			nP = MP(P.FI+aX, P.SE+aY);
			if(S.find(nP) == S.end() && isIn(nP.FI,nP.SE)) {
				S.insert(nP);
				Q.push(nP);
			}
			nP = MP(P.FI+bX, P.SE+bY);
			if(S.find(nP) == S.end() && isIn(nP.FI,nP.SE)) {
				S.insert(nP);
				Q.push(nP);
			}
		}
	} else {
	
		LL pB=0, qB=0, prevP=0, prevQ=0;
		FOR(z,0,INF) {
			
			//while(isIn(sX+(pB-1)*bX, sY+(pB-1)*bY) && pB>0) pB--;
			while(!isIn(sX+pB*bX, sY+pB*bY) && pB<INF) pB++;
			while(!isIn(sX+qB*bX, sY+qB*bY) && qB>=0) qB--;
			while(isIn(sX+(qB+1)*bX, sY+(qB+1)*bY) && pB<INF) qB++;
			if(qB<0 || pB==INF || pB>prevQ) break;
			if(pB<=qB) res += qB-pB+1;
			//printf("z=%d pB=%lld qB=%lld sX=%lld sY=%lld res=%lld\n",z,pB,qB,sX,sY,res);
			sX += aX;
			sY += aY;
			prevP=pB; prevQ=qB;
		}
	}
	printf("%lld\n",res);
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
