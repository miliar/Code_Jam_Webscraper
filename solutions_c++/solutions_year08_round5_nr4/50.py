#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<stack>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

const int INF = 10007;

int gcd(int a, int b) {
	while(b) { swap(a,b); b%=a; }
	return a;
}

//	Rozszerzony Euklides
//	ax + by = d, gdzie d=gcd(a,b)
//	a >= b!  a,b >= 0 (wpp. bardzo uwazaj)
int egcd(int a, int b, int &x, int &y) { // |d|=gcd(a,b), d=ax+by
    if (!b) { x=1; y=0; return a; }      // |x|<=|b| (b!=0), |y|<=|a| (a!=0)
    else {
        int x1, y1;
        int d=egcd(b, a%b, x1, y1);
        x=y1; y=x1-(a/b)*y1;
        return d;
    }
}

int rev(int a) {
	int x,y;
	egcd(a,INF,x,y);
	while(x<0) x += INF;
	return x;
}

int silnia[100000001];

int numWays(int x, int y) {
	if(x<0 || y<0) return 0;
	if((x+y)%3>0) return 0;
	int numD = (x+y)/3;
	x -= numD; y -= numD;
	if(x<0 || y<0) return 0;
	int a = silnia[x+y];
	int b = rev((silnia[x]*silnia[y])%INF);
	return (a*b)%INF;
}

pair<int,int> tabR[12];

void testcase(int tNum) {

	int n,m,r;
	scanf("%d %d %d",&n,&m,&r);
	
	int res = 0;
	
	FOR(i,0,r) 
		scanf("%d %d",&tabR[i].FI,&tabR[i].SE);
	
	sort(tabR, tabR+r);
	
	FOR(mask,0,1<<r) {
		vector<pair<int,int> > V;
		V.PB(MP(1,1));
		FOR(j,0,r) if(mask&(1<<j)) V.PB(tabR[j]);
		V.PB(MP(n,m));
		int add = V.size()%2;
		int numW = 1;
		FOR(i,0,V.size()-1) {
			int a = numWays(V[i+1].FI-V[i].FI, V[i+1].SE-V[i].SE);
			numW = (numW*a)%INF;
		}
		if(add==0)
			res += numW; else
			res -= numW;
		res = (res+INF)%INF;
	}
	
	printf("Case #%d: %d\n",tNum,res);
	
}

int main() {

	silnia[0] = silnia[1] = 1;
	FOR(i,2,100000001) silnia[i] = (silnia[i-1]*i)%INF;

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
