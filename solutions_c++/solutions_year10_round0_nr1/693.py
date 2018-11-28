#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef long long ll;
int main(){
	assert(freopen("A-large.in","rt",stdin)==stdin);
	assert(freopen("A-large.out","wt",stdout)==stdout);
	int T,Case;
	ll n,k;
	assert(scanf("%d",&T)==1);
	for(Case=1;Case<=T;Case++){
		assert(scanf("%lld%lld",&n,&k)==2);
		printf("Case #%d: ",Case);
		k=k+1;
		if((k%(1LL<<n))==(0LL)) printf("ON\n"); else printf("OFF\n");
	}
	return 0;
}
//---
//+--
//-+-
//++-
//--+
//+-+
//-++

//47=16*3-1
