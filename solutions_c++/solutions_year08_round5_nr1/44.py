#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<string>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;

vector<pair<int,int> > tabX, tabY;
int tabD[4][2] = {{0,1},{-1,0},{0,-1},{1,0}};

char vis[6001][6001];
char S[100];

void testcase(int tNum) {

	int minX=3000, maxX=3000, minY=3000, maxY=3000;
	memset(vis,0,sizeof(vis));
	int res = 0;
	
	tabX.clear(); tabY.clear();
	
	int actX=3000, actY=3000, dir=0;
	
	int L;
	scanf("%d",&L);
	while(L--) {
		int num;
		scanf("%s %d",S,&num);
		int len = strlen(S);
		while(num--) FOR(i,0,len) {
			char c = S[i];
			if(c=='L')
				dir++; else if(c=='R')
				dir+=3; else {
				dir %= 4;
				int dX = tabD[dir][0], dY=tabD[dir][1];
				int nX = actX+dX, nY=actY+dY;
				if(dY==0)
					tabX.PB(MP(min(nX,actX),actY)); else 
					tabY.PB(MP(min(nY,actY),actX));
				actX = nX; actY = nY;
				minX <?= nX;
				maxX >?= nX;
				minY <?= nY;
				maxY >?= nY;
			}
		}
	}
	
	sort(tabX.begin(), tabX.end());
	sort(tabY.begin(), tabY.end());
	
	for(int i=1; i+1<tabX.size(); i+=2) if(tabX[i].FI==tabX[i+1].FI) FOR(j,tabX[i].SE,tabX[i+1].SE)
		vis[tabX[i].FI][j] = 1;
	for(int i=1; i+1<tabY.size(); i+=2) if(tabY[i].FI==tabY[i+1].FI) FOR(j,tabY[i].SE,tabY[i+1].SE)
		vis[j][tabY[i].FI] = 1;
		
	FOR(x,minX,maxX+1) FOR(y,minY,maxY+1) { res += vis[x][y]; }
	
	printf("Case #%d: %d\n",tNum,res);
	
	tabX.clear(); tabY.clear();
}

int main() {

	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
