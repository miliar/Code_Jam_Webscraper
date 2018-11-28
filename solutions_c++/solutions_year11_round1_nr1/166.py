#include <iostream>
#include <vector>
#include <set>
#include <assert.h>
#include <map>
#include <string>
#include <cstdio>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

#define For(i,a,b) for(int i=a;i<b;i++)
#define rep(i,x) For(i,0,x)
#define foreach(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); ++i)
#define F first
#define S second
#define sz(x) ((int)(x).size())
#define SQ(x) ((x)*(x))
#define mp make_pair
#define pb push_back

int main(){
int np;cin>>np;
rep(tp,np){
	long long n,pd, pg; cin>>n>>pd>>pg;
	bool fail=false;
	if(pg == 0 && pd > 0) fail=true;
	if(pg == 100 && pd < 100) fail=true;
	bool got = false;
	for(long long i=1; i<= min(n,100LL); i++){
		long long top = pd*i/100;
		long long real = top*100/i;
		if(real == pd) got=true;
	}
	if(!got) fail=true;
	printf("Case #%d: %s\n", tp+1, fail ? "Broken" : "Possible");
}
}
