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
		char buf[102];
		int table[100][100];
		int count[100];
		int sum[100];
		double wp[100];
		double owp[100];
		double oowp[100];
		int N;
		scanf("%d ", &N);
		REP(i, N){
			scanf("%s ", buf);
			count[i] = 0;
			sum[i] = 0;
			REP(j, N){
				table[i][j] = buf[j] != '.' ? buf[j] - '0' : -1;
				if(table[i][j] < 0) continue;
				count[i]++;
				sum[i] += table[i][j];
			}
			wp[i] = sum[i] / (double)count[i];
		}
		REP(i, N){
			owp[i] = 0;
			REP(j, N) if(table[j][i] >= 0) owp[i] += (sum[j] - table[j][i]) / (double)(count[j] - 1);
			owp[i] /= count[i];
		}
		REP(i, N){
			oowp[i] = 0;
			REP(j, N) if(table[i][j] >= 0) oowp[i] += owp[j];
			oowp[i] /= count[i];
		}
		printf("Case #%d:\n", ttt);
		REP(i, N) printf("%.12g\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}
