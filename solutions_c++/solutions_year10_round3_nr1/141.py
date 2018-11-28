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
#define maxn 10100
int nsc, sc;
int n;
int a[maxn];
int b[maxn];
void init(){
	scanf("%d", &n);
	for(int i=0; i<n; i++)
		scanf("%d %d", &a[i], &b[i]);
}
void solve(){
	int cnt=0;
	for(int i=0; i<n; i++){
		for(int j=i+1; j<n; j++){
			if ((a[i]>a[j] && b[i]<b[j])
				|| (a[i]<a[j] && b[i]>b[j]))
				cnt++;
		}
	}
	printf("Case #%d: %d\n", sc, cnt);
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