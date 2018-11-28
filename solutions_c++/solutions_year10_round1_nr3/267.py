#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <deque>
#include <cmath>
#include <utility>

using namespace std;


typedef long long ll;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define DBG(x) cerr<<#x<<" = "<<x<<endl
#define DBGV(x) {cerr<<#x<<": "; for(int i=0;i<sz(c);i++) cerr<<x[i]<<" "; cerr<<endl;}
#define DBGA(x) {cerr<<#x<<": "; for(int i=0;i<int(sizeof(x)/sizeof(x[0]));i++) cerr<<x[i]<<" "; cerr<<endl;}

map<int,map<int,int> > hash;
int solve(int a,int b){
	if(a<=0||b<=0) return 1;
	int k;	
	int r=0;
	if(hash.count(a)&&hash[a].count(b)) return hash[a][b];
	hash[a][b]=r;
	for(k=max((a+b)/b,(b+a)/a);k>0;k--){
		r|=!solve(a-k*b,b);
		r|=!solve(a,b-k*a);
		if(r) return hash[a][b]=r;
	}
	return hash[a][b]=r;
}
int main(){
	assert(freopen("C.in","rt",stdin)==stdin);
	assert(freopen("C.out","wt",stdout)==stdout);
	int T,a,b,c,d;
	scanf("%d",&T);
	for(int C=1;C<=T;C++){
		scanf("%d %d %d %d",&a,&b,&c,&d);
		int i,j,r=0;
		for(i=a;i<=b;i++){
			for(j=c;j<=d;j++){
				r+=solve(i,j);
			}
		}
		printf("Case #%d: %d\n",C,r);
	}
	return 0;
}
