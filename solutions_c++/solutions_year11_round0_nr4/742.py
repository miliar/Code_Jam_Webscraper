#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
using namespace std;
typedef pair<int, int> pi;
typedef long long int li;
typedef vector<int> vi;
typedef long double ld;
void solve();
#define mp make_pair
#define pb push_back

int main(){
#ifdef DEBUG
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}
void solve(){
	int n;
	
	scanf("%d",&n);
	vi v(n,0);
	for(int i=0;i<n;++i){
		scanf("%d",&v[i]);
	}
	int c=0;
	for(int i=0;i<n;++i){
		if(v[i]!=i+1)
			++c;
	}
	printf("%.10lf\n",(double)c);
	
}