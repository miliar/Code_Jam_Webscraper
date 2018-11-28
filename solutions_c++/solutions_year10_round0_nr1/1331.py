#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
int nsc;
int sc;
int n, k;
void init(){
	scanf("%d %d", &n, &k);
}
void out(bool ans){
	if (!ans){
		printf("Case #%d: %s\n", sc, "OFF");
	}
	else
		printf("Case #%d: %s\n", sc, "ON");
}
bool getbit(int num, int bit){
	return (num&(1<<bit))!=0;
}
void solve(){
	for(int j=0; j<n; j++)
		if (!getbit(k, j)){
			out(false);
			return;
		}
	out(true);
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}