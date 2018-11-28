#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

LL ar[3][3];
int per[][3] = {
{0,0,0},
{1,1,1},
{2,2,2},
{0,1,2},
{0,2,1},
{1,0,2},
{1,2,0},
{2,0,1},
{2,1,0}
};

int main()
{
	ios_base::sync_with_stdio(0);
	int NCase;
	cin>>NCase;
	REP(ncase,NCase) {
		int n,a,b,c,d,X,Y,m;
		cin>>n>>a>>b>>c>>d>>X>>Y>>m;
		int xi=X,yi=Y;
		REP(i,3) REP(j,3) ar[i][j]=0;
		REP(i,n) {
			int xj=xi%3; if(xj<0) xj+=3;
			int yj=yi%3; if(yj<0) yj+=3;
			ar[xj][yj]++;
			xi=((LL)a*(LL)xi+ (LL)b) % (LL)m;
			if(xi<0) xi+=m;
			yi=((LL)c*(LL)yi+ (LL)d) % (LL)m;
			if(yi<0) yi+=m;
		}

		LL result=0;
		REP(i,4) REP(j,9) {
			if(i<3 && j>3) continue;
			//cout<<per[i][0]<<per[j][0]<<" "<<per[i][1]<<per[j][1]<<" "<<per[i][2]<<per[j][2]<<" "<<endl;
			if(i>=3 || j>=3)
				result+=
					ar[per[i][0]][per[j][0]]*
					ar[per[i][1]][per[j][1]]*
					ar[per[i][2]][per[j][2]]
			;
			else if((ar[per[i][1]][per[j][1]]-1)>0 && (ar[per[i][2]][per[j][2]]-2)>0) {
				result+=
					(ar[per[i][0]][per[j][0]]*
					(ar[per[i][1]][per[j][1]]-1)*
					(ar[per[i][2]][per[j][2]]-2))/6
			;}
		}

		cout<<"Case #"<<ncase+1<<": "<<result<<endl;
	}

  return 0;
}

