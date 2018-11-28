#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 1010;
int n,x,s,r,t;
int V[N];
double timeNeeded[N][N]; // time_needed(i,j)ile czasu, jezeli do miejsca i, bede biegl juz j jednostek

main(){
	int z;
	scanf("%d",&z);
	FOR(q,1,z){
		scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
		t = min(t,x);
		int b,e,v;
		REP(i,x)
			V[i] = s;
		REP(i,n){
			scanf("%d %d %d",&b,&e,&v);
			FOR(j,b,e-1)
				V[j] += v;
		}
		int roz = r - s;
		double wyn =0;
		double czas = t;
		sort(V,V+x);
		int ind = 0;
		while((czas > 10e-9) && ind < x){
			if(czas >= 1.0/(V[ind] + roz)){
				czas -= 1.0/(V[ind] + roz);
				wyn += 1.0/(V[ind] + roz);
				ind++;
			}
			else{
				double bieg = czas * (V[ind] + roz);
				wyn += bieg/ (V[ind] + roz);
				wyn += (1.0 - bieg)/(V[ind]);
				ind++;
				break;
			}
		}
		for(int j=ind;j<x;j++){
			wyn += 1.0/V[j];
		}
		printf("Case #%d: %.10lf\n",q,wyn);
	}
	return 0;
}
