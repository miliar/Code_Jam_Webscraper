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
int nsc, sc;
int l, p, c;
void init(){
	scanf("%d %d %d", &l, &p, &c);
	
}
void solve(){
	int ll=l;
	int rr=p;
	int cnt=0;
	while ((__int64)(ll)*c<rr){
		cnt++;
		rr=(rr+c-1)/c;
	}
	printf("Case #%d: ", sc);
	if (cnt==0){
		printf("0\n");
	}
	else{
		int res=0;
		while (cnt>0){
			cnt=cnt/2;
			res++;
		}
		printf("%d\n", res);
	}
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