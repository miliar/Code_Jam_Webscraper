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

char buf[502];
int mat[500][500];

bool check(int x, int y, int R, int C, int size){
	int chk_x = 0;
	int chk_y = 0;
	if(size % 2){
		int s = size / 2;
		if( (x - s <  0) ||
			(y - s <  0) ||
			(x + s >= R) ||
			(y + s >= C) ) return false;
		FORe(i,-s,+s){
			FORe(j,-s,+s){
				if( (i == -s && j == -s) ||
					(i == +s && j == -s) ||
					(i == +s && j == +s) ||
					(i == -s && j == +s) ) continue;
				chk_x += mat[x + i][y + j] * i;
				chk_y += mat[x + i][y + j] * j;
			}
		}
	}else{
		int s = size / 2;
		if( (x - s < -1) ||
			(y - s < -1) ||
			(x + s >= R) ||
			(y + s >= C) ) return false;
		FORe(i,1-s,+s){
			FORe(j,1-s,+s){
				if( (i ==1-s && j ==1-s) ||
					(i == +s && j ==1-s) ||
					(i == +s && j == +s) ||
					(i ==1-s && j == +s) ) continue;
				chk_x += mat[x + i][y + j] * (i*2 - 1);
				chk_y += mat[x + i][y + j] * (j*2 - 1);
			}
		}
	}
	return !chk_x && !chk_y;
}

int main(){
	int T;
	scanf("%d ", &T);
	REP1(ttt, T){
		int R, C, D;
		scanf("%d %d %d ", &R, &C, &D);
		REP(i,R){
			scanf("%s ", buf);
			REP(j,C){
				mat[i][j] = buf[j] - '0' + D;
			}
		}
		bool end = false;
		int K = min(R, C);
		for(; K >= 3; K--){
			REP(i,R){
				REP(j,C){
					if(check(i, j, R, C, K)){
						end = true;
						break;
					}
				}
				if(end) break;
			}
			if(end) break;
		}
		if(K >= 3){
			printf("Case #%d: %d\n", ttt, K);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", ttt);
		}
		
	}
	return 0;
}
