#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
using namespace std;

int tst, _, n, w, l, c[1111][2], t, v[1111][2];

struct node{
	int r, id;
	friend bool operator < (const node &a, const node &b){
		return a.r > b.r;
	}
} a[11];

bool inc(int l, int r, int p, int q){
	if (r <= p || q <= l)
		return 0;
	return 1;
}

bool construct(){
	int lst = -INF;
	for (int i = 0; i < n; i++){
		lst = max(lst + (i ? a[i - 1].r : 0) + a[i].r, 0);
		if (lst > w) lst = 0;
		t = 0;
		for (int j = 0; j < i; j++)
			if (inc(c[j][0] - a[j].r, c[j][0] + a[j].r, lst - a[i].r, lst + a[i].r))
				t = max(t, c[j][1] + a[j].r + a[i].r);
		if (t > l)
			return 0;
		c[i][0] = lst;
		c[i][1] = t;
	}
	return 1;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &tst);
	while (tst--){
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; i++){
			scanf("%d", &a[i].r);
			a[i].id = i;
		}
		sort(a, a + n);
		while (!construct()){
			random_shuffle(a, a + n);
			swap(w, l);
		}
		for (int i = 0; i < n; i++){
			v[a[i].id][0] = c[i][0];
			v[a[i].id][1] = c[i][1];
		}
		printf("Case #%d:", ++_);
		for (int i = 0; i < n; i++)
			printf(" %d %d", v[i][0], v[i][1]);
		printf("\n");
	}
}
