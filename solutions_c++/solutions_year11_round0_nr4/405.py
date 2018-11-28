#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <iostream>
#include <string>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int main(){
	int T;scanf("%d",&T);
	for(int tt=1 ; tt<=T ; tt++){
		int N;scanf("%d",&N);
		double res = 0;
		REP(i,N){
			int x;scanf("%d",&x);
			if(x!=i+1)res += 1;
		}
		printf("Case #%d: %.12f\n",tt,res);
	}
	return 0;
}
