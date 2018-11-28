#include <stdio.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

struct pl{
	long amount;
	int pos;
};

int main(int argc, char *argv[]) {
	int T;
	int G[1000];
	struct pl GG[1000];
	scanf("%d", &T);
	for(int i=1; i<=T; ++i){
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for(int ii=0; ii<N; ++ii){
			scanf("%d", &(G[ii]));
		}
		for(int ii=0; ii<N; ++ii){
			long mass=0;
			int pos=ii;
			for(int j=0; j<N; ++j){
				GG[ii].amount = mass;
				GG[ii].pos = pos;
				if((mass + (long)G[pos]) <= (long)k){
					mass+=(long)G[pos];
					GG[ii].amount = mass;
					GG[ii].pos = pos;
				} else{
					break;
				}
				if((pos+1)<N){
					++pos;
				} else{
					pos=0;
				}
			}
		}
		long MASS=0;
		int POS=0;
		for(int j=0; j<R; ++j){
			MASS+=GG[POS].amount;
			POS=GG[POS].pos;
		}
		printf("Case #%d: %ld\n", i, MASS);
	}
}







