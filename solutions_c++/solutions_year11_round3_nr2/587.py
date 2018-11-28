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

int arr[1000000];
bool boosts[1000000];

int calc(int t, int N){
	int ret = 0;
	REP(i,N){
		if(boosts[i]){
			if(ret >= t){
				ret += arr[i];
			}else if(t - ret < arr[i]){
				ret += arr[i] + (t - ret) / 2;
			}else{
				ret += arr[i] * 2;
			}
		}else{
			ret += arr[i] * 2;
		}
	}
	return ret;
}

int main(){
	int T;
	scanf("%d ", &T);
	REP1(ttt, T){
		int L, t, N, C;
		scanf("%d %d %d %d ", &L, &t, &N, &C);
		REP(i,C){
			scanf("%d ", arr + i);
			for(int j = i + C; j <= N; j += C) arr[j] = arr[i];
			boosts[i] = false;
		}
		int ret = 0x7FFFFFFF;
		for(int u = L; u >= 0; --u){
			switch(u){
			case 0:
				ret = min(ret, calc(t, N));
				break;
			case 1:
				REP(i,N){
					boosts[i] = true;
					ret = min(ret, calc(t, N));
					boosts[i] = false;
				}
				break;
			case 2:
				REP(i,N-1){
					FOR(j,i+1,N){
						boosts[i] = boosts[j] = true;
						ret = min(ret, calc(t, N));
						boosts[i] = boosts[j] = false;
					}
				}
				break;
			}
		}
		printf("Case #%d: %d\n", ttt, ret);
	}
	return 0;
}
