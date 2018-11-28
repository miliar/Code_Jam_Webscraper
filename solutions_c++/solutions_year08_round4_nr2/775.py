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

struct pt{int x,y;};



int main(){
	
	int Kase;
	scanf("%d",&Kase);
	FOR(kase,1,Kase+1){
		int n,m,a;
		scanf("%d",&n);
		scanf("%d",&m);
		scanf("%d",&a);
		
		printf("Case #%d: ",kase);
		int printed=0;
		REP(x1,n+1){
			REP(x2,n+1){
				REP(y2,m+1){
					int rem= a-x1*y2;
					rem=-rem;
					if(rem<0)	continue;
					if(rem && !x2)	continue;
					if((rem==0 && x2==0) || rem%x2==0){
						if(x2==0)	rem=0;
						else	rem/=x2;
						int y1=rem;
						if((x1 || y1) && (x2 || y2) && (x1!=x2 || y1!=y2) && !printed){
							printf("%d %d %d %d %d %d",0,0,x1,y1,x2,y2);
							printed=1;
						}
					}
					
				}
			}
		}
		if(!printed)	printf("IMPOSSIBLE");
		printf("\n");
	}
	return 0;
}
