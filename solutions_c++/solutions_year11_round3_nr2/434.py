#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
const int M = 1000000+10;
const int inf = 1000000000;
const double eps = 1e-8;
int n;
int l, t, c;
int dis[M];
int id[M];
bool cmp(const int &a, const int &b){
	return dis[a] > dis[b];
}
int solve(){
	int i, j;
	int ans = 0;
	scanf ("%d%d%d%d", &l, &t, &n, &c);
	for(i = 0; i < n; i ++)
		id[i] = i;
	for(i = 0;i < c; i ++)
		scanf ("%d", &dis[i]);
	for(j = c, i = 0; j <n; j ++, i ++)
		dis[j] = dis[i];
	for(i = 0; i < n; i ++){
		ans += dis[i]*2;
		if(ans > t)
			break;
	}
	if(i == n) return ans;
	int cha = ans - t;
	ans -= cha;
	cha /= 2;
	dis[i] = cha;
	sort(id+i, id+n, cmp);
	for(j = 0; i < n && j < l; i ++, j ++){
		ans += dis[id[i]];
	}
	for(; i < n; i ++){
		ans += dis[id[i]] * 2;
	}
	return ans;

}
int main(){
	int cas;
	int i;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf ("%d", &cas);
	for(i = 1; i <= cas; i ++){
		printf ("Case #%d: ", i);
		int s = solve();
		printf ("%d\n", s);
	}
	return 0;
}