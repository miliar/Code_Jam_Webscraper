// C2.cpp

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define maxn 1000010

int w[maxn];

int bsearch(int c){
	int lo,hi,md;
	lo=1; hi=c;
	while (lo<hi){
		md=(lo+hi)/2;
		if (w[md]<=c) lo=md+1;
		else hi=md;
	}
	return hi;
}

void init(){
	w[1]=2;
	w[2]=4;
	for (int i=3;i<maxn;i++){
		w[i]=bsearch(i)+i;
	}
}

int solve(int cas){
	int a1,a2,b1,b2;
	int i;
	long long ret=0;
	scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
	for (i=a1;i<=a2;i++){
		if (b1>=w[i]) ret+=b2-b1+1;
		else if (b2>=w[i]) ret+=b2-w[i]+1; 
	}
	for (i=b1;i<=b2;i++){
		if (a1>=w[i]) ret+=a2-a1+1;
		else if (a2>=w[i]) ret+=a2-w[i]+1;
	}
	printf("Case #%d: %I64d\n",cas,ret);
}

int main(){
	int t,cas;
	init();
//	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}
