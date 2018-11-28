#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <iostream>
#include <string>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int N;
int C[1000];

int popCount(int x){
	int res = 0;
	while(x){
		if(x&1)res++;
		x>>=1;
	}
	return res;
}

int small(){
	int res = -1;
	REP(i,1<<N){
		int p = popCount(i);
		if(0<p&&p<N){
			int sean = 0;
			int patrick = 0;
			int sum = 0;
			REP(j,N){
				if(i>>j&1){
					patrick ^= C[j];
					sum += C[j];
				}
				else{
					sean ^= C[j];
				}
			}
			if(sean==patrick){
				res = max(res,sum);
			}
		}
	}
	return res;
}

int large(){
	int res = -1;
	int xor = 0;
	int sum = 0;
	REP(i,N){
		xor ^= C[i];
		sum += C[i];
	}
	if(xor==0){
		res = sum-C[0];
	}
	return res;
}

int main(){
	int T;scanf("%d",&T);
	for(int tt=1 ; tt<=T ; tt++){
		scanf("%d",&N);
		REP(i,N)scanf("%d",C+i);
		sort(C,C+N);
		//int sres = small();
		int lres = large();
		//if(sres != lres)cerr << "!" << endl;
		printf("Case #%d: ",tt);
		if(lres==-1){
			printf("NO\n");
		}
		else{
			printf("%d\n",lres);
		}
	}
	return 0;
}