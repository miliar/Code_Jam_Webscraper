#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iostream>
#include <limits.h>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SQ(a) ((a)*(a))
#define EPS 1e-10

#define MAXN 50

typedef struct chick {
	int pos, speed;
	bool operator<(const chick other) const {
		return pos > other.pos;
	}
} chick;

chick chicks[MAXN];

//double arrivalTime[MAXN];
bool ok[MAXN];

int main(){
	int C, N, K, B, T;
	int mins;
	scanf("%d",&C); 
	for(int t=1;t<=C;++t){
		scanf("%d %d %d %d\n",&N,&K,&B,&T);
		mins = 0;
		
		// read pos
		for(int i=0;i<N;++i){
			scanf("%d",&(chicks[i].pos));
		}
		// read speed
		for(int i=0;i<N;++i){
			scanf("%d",&(chicks[i].speed));
		}
		
		sort(chicks,chicks+N);
		//printf("");
		
		// calc arrival time
		int ok_cnt = 0;
		for(int i=0;i<N;++i){
			double arrivalTime = (B - chicks[i].pos) / (double) chicks[i].speed;
			ok[i] = (arrivalTime <= (T + EPS));
			if(ok[i]) ++ ok_cnt;
		}
		
		//printf("ok_cnt: %d\n", ok_cnt);
		
		if(ok_cnt >= K){
			// calc number of swaps needed
			int arrived = 0;
			int index = 0;
			while(arrived < K){
				while(!ok[index]) ++index;
				//printf("\t next to make it:%d\n", index);
				mins += (index - arrived);
				++arrived;
				++index;
			}
		
			printf("Case #%d: %d\n", t, mins);
		} else{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
}
