#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int TC,N;
char S[200],ans[200];
long long int A,B;
bool done;

void brute(int x){
	if(done) return;
	if(x == N){
		A = 0;
		for(int i=0;i<N;++i) A += (long long int)(ans[N-1-i]-'0')*(1ll<<i);
		B = sqrt(A);
		if(B*B == A){
			done = 1;
			return;
		}
	}
	else if(S[x] != '?'){
		ans[x] = S[x];
		brute(x+1);
	}
	else{
		ans[x] = '0';
		brute(x+1);
		if(done) return;
		ans[x] = '1';
		brute(x+1);
	}
}

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&TC);
	for(int testcase=1;testcase<=TC;++testcase){
		scanf(" %s",S);
		N = strlen(S);
		memset(ans,0,sizeof(ans));
		done = 0;
		brute(0);
		printf("Case #%d: %s\n",testcase,ans);
	}
}
