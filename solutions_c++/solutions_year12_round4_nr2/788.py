#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

typedef complex<double> P;

double random(){
	return (double)rand()/RAND_MAX;
}

void solve(){
	double EPS = 1e-9;
	int N,W,L;
	scanf("%d%d%d",&N,&W,&L);
	vector<pair<double,int> > r(N);
	REP(i,N){
		scanf("%lf",&r[i].first);
		r[i].second = i;
	}
	sort(ALL(r));
	reverse(ALL(r));
	vector<P> pos(N,P(0,0));
	while(true){
		int i=1;
		for(; i<N ; i++){
			double y = random()*L;
			double x = random()*W;
			pos[i] = P(x,y);
			int j = 0;
			
			for(;j<i ; j++){
				double len = abs(pos[j]-pos[i]);
				double rad = r[i].first+r[j].first;
				if(len<rad+EPS)break;
			}
			if(j!=i)break;
		}
		if(i==N)break;
	}
	vector<P> res(N);
	REP(i,N)res[r[i].second] = pos[i];

	REP(i,N){
		printf("%.3f %.3f",res[i].real(),res[i].imag());
		printf("%c",(i==N-1?'\n':' '));
	}
}

int main(){
	int T;
	cin >> T;
	srand(215);
	REP(tt,T){
		printf("Case #%d: ",tt+1);
		solve();
	}
	return 0;
}

