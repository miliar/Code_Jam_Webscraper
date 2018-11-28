#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

//#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define cs c_str()
#define pb push_back
#define sz size()
#define INF (int)1e9+1

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

bool fn(int x1, int y1, int x2, int y2){
	if(x1<x2)	return 1;
	if(x1==x2 && y1<=y2)	return 1;
	return 0;
}

int main(){
	int kase=1,N=0;scanf("%d",&N);
	for(;kase<=N;kase++){
		LL ans=0;
		LL a[3][3]={0};
		LL n, A, B, C, D, x0, y0, M;
		scanf("%Ld %Ld %Ld %Ld %Ld %Ld %Ld %Ld",&n ,&A, &B, &C, &D, &x0, &y0, &M);
		LL X = x0, Y = y0;
		a[X%3][Y%3]++;
		FOR(i,1,n){
		 	X = (A * X + B) % M;
  			Y = (C * Y + D) % M;
 		 	a[X%3][Y%3]++;
		}
		REP(x1,3){
			REP(x2,3){
				int x3= (9-(x1+x2))%3;
				REP(y1,3){
					REP(y2,3){
						int y3= (9-(y1+y2))%3;
						if(!(fn(x1,y1,x2,y2) && fn(x2,y2,x3,y3)))	continue;
						if(x1==x3 && y1==y3 ){if(a[x1][y1]>=3)	ans+= (a[x1][y1]*(a[x1][y1]-1)*(a[x1][y1]-2))/6;}
						else if(x1==x2 && y1==y2 ){if(a[x1][y1]>=2)	ans+= (a[x1][y1]*(a[x1][y1]-1))/2*a[x3][y3];}
						else if(x2==x3 && y2==y3){ if(a[x2][y2]>=2)	ans+= (a[x2][y2]*(a[x2][y2]-1))/2*a[x2][y2];	}
						else	{cerr<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<"ans+="<<(a[x1][y1]*a[x2][y2]*a[x3][y3])<<endl;ans+= (a[x1][y1]*a[x2][y2]*a[x3][y3]);}
					}
				}
			}
		}
		cerr<<endl<<endl;
		printf("Case #%d: %Ld\n", kase, ans);
	}


	return 0;
}
