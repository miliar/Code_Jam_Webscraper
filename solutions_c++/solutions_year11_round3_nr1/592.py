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
		int R, C;
		scanf("%d %d ", &R, &C);
		char in[100][100];
		char out[100][100];
		bool ng = false;
		REP(i,R){
			scanf("%s ", in[i]);
			REP(j,C) out[i][j] = '.';
			out[i][C] = '\0';
		}
		REP(i,R){
			REP(j,C){
				if(in[i][j] == '#'){
					if(out[i][j] == '.'){
						if((i+1>=R)||(j+1>=C)){
							ng = true;
							break;
						}
						out[i+0][j+0] = '/';
						out[i+0][j+1] = '\\';
						out[i+1][j+0] = '\\';
						out[i+1][j+1] = '/';
					}
				}else{
					if(out[i][j] != '.'){
						ng = true;
						break;
					}
				}
			}
			if(ng) break;
		}
		printf("Case #%d:\n", ttt);
		if(ng) printf("Impossible\n"); else REP(i,R) printf("%.*s\n", C, out[i]);
	}
	return 0;
}
