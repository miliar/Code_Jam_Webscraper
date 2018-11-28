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
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SQ(a) ((a)*(a))
#define EPS 1e-10

#define MAXN 28

int T, N;
int solution;
bool used[MAXN];
int memres[MAXN];

inline bool possible(){
	int curr = N;
	//printf("test possible:");
	//for(int i=0;i<=N;++i){
	//	if(used[i])printf("%d ", i);
	//}
	//printf("\n");
	for(;;){
		// calc rank
		int rank = 0;
		for(int i=0;i<=curr;++i){
			if(used[i]) ++rank;
		}
		//printf("\t curr=%d rank=%d\n", curr, rank);
		if(rank == 1) return true;
		if(!used[rank]) return false;
		curr = rank;
	}
}

inline void setnext(int index){
	if(index == N){
			if(possible()){
				solution++;
				if(solution == 100003){
					solution = 0;
				}
			}
			return;
	}
	used[index] = false;
	setnext(index + 1);
	used[index] = true;
	setnext(index + 1);
}

int main(){
	memset(memres,0,sizeof(memres));
	scanf("%d",&T); 
	for(int t=1;t<=T;++t){
		scanf("%d\n",&N);
		if(memres[N]==0){
			solution = 0;
			memset(used,0,sizeof(used));
			used[N] = true;
			setnext(2);
			memres[N] = solution;
		} else{
			solution = memres[N];
		}
		printf("Case #%d: %d\n", t, solution);
	}
}
