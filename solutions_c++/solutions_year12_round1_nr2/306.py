#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

struct node{
	int id, l1, l2;
	friend bool operator < (const node &a, const node &b){
		return a.l2 < b.l2;
	}
};

bool cmp1(const node &a, const node &b){
	return a.l1 < b.l1;
}
bool cmp2(const node &a, const node &b){
	return a.l2 < b.l2;
}

int _, n, h[1111], x, y;
node a[1111], b[1111];

void solve(){
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		h[i] = 0;
	for (int i = 0; i < n; i++){
		scanf("%d%d", &x, &y);
		a[i].id = i;
		a[i].l1 = x;
		a[i].l2 = y;
		b[i] = a[i];
	}
	sort(a, a + n, cmp1);
	sort(b, b + n, cmp2);
	int ans = 0, p1 = 0, p2 = 0, now = 0;
	priority_queue<node> Q;
	while (1){
		while (p2 < n && b[p2].l2 <= now){
			now += 2 - h[ b[p2].id ];
			h[ b[p2].id ] = 2;
			p2++;
			ans++;
		}
		while (p1 < n && a[p1].l1 <= now){
			Q.push(a[p1]);
			p1++;
		}
		while (!Q.empty() && h[ Q.top().id ] != 0)
			Q.pop();
		if (!Q.empty()){
			h[ Q.top().id ] = 1;
			Q.pop();
			now++;
			ans++;
		}
		else
			break;
	}
	for (int i = 0; i < n; i++)
		if (h[i] < 2){
			puts("Too Bad");
			return;
		}
	printf("%d\n", ans);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &_);
	for (int i = 1; i <= _; i++){
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
