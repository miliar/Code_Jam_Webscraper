#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
int dp[16][1<<11];
bool broken[16][16];
int M,N; 

int doit(int at, int mask){
	if(at==M) return 0;
	int& ref=dp[at][mask];
	if(ref!=-1) return ref; 

	ref=doit(at+1,(1<<N)-1);
	for(int i=mask;i>0;i=(i-1)&mask){
		int nmask=0,seat=0;
		bool good=1;
		for(int j=0; j<N; ++j){
			if(j>0){
				if((i&(1<<j)) && (i&(1<<(j-1)))){
					good=0; 
					break; 
				}
			}
		}
		if(!good) continue;     
		for(int j=0; j<N; ++j){
			if((i&(1<<j))){
				if(broken[at][j]){
					good=0;
					break; 
				}
				if(j+1<N) nmask|=(1<<(j+1));
				if(j>0) nmask|=(1<<(j-1));
				seat++;
			}
		}
		if(good)
			ref=max(ref,seat+doit(at+1,((1<<N)-1)^nmask));
	}
	return ref;
}

int main() {
	int NCASES;
	scanf("%d", &NCASES);
	for (int z=1;z<=NCASES;++z) {
		memset(dp,-1,sizeof dp);
		memset(broken,0,sizeof broken);
		scanf("%d %d", &M,&N);
		for(int i=0;i<M;++i){
			char str[1000];
			scanf("%s", &str);
			for(int j=0; j<N; ++j) if(str[j]=='x')
				broken[M-i-1][N-j-1]=1; 
		}
		printf("Case #%d: %d\n", z,doit(0,(1<<N)-1));
	}
}
