#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FORe(i,a,b)	for(int i=(a);i<=(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define REP1(i,b)	FORe(i,1,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FROMTO(it,b,e)	for(LET(it,(b));it!=(e);++it)
#define FOREACH(it,c)	FROMTO(it,(c).begin(),(c).end())

int main(){
	int T;
	scanf("%d ", &T);
	REP1(ttt, T){
		int X, S, R, t, N;
		scanf("%d %d %d %d %d ", &X, &S, &R, &t, &N);
		vector<pair<int, int> > arr;
		int x0 = X;
		REP(i,N){
			int B, E, w;
			scanf("%d %d %d ", &B, &E, &w);
			arr.push_back(make_pair(w, E - B));
			x0 -= E - B;
		}
		arr.push_back(make_pair(0, x0));
		sort(ALL(arr));
		double run_able = t;
		double ret = 0;
		FOREACH(it, arr){
			if(run_able > 0){
				double run_time = it->second / (double)(R + it->first);
				if(run_time < run_able){
					ret += run_time;
					run_able -= run_time;
				}else{
					ret += run_able + (it->second - run_able * (R + it->first)) / (double)(S + it->first);
					run_able = 0;
				}
			}else{
				ret += it->second / (double)(S + it->first);
			}
		}
		printf("Case #%d: %.9f\n", ttt, ret);
	}
	return 0;
}
