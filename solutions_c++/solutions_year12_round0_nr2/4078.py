//#pragma warning(disable:4996)
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

struct trip{
	int a, b, c;

	trip(int _a, int _b, int _c):a(_a), b(_b), c(_c){}
};

inline bool cmp(const trip &p, const trip &q){
	if (p.c != q.c) return(p.c > q.c);
	if (p.b != q.b) return(p.b > q.b);
	return(p.a > q.a);
}

int sup, cnt;
int T, N, S, P;
vector<trip> v1; // < P with sup
vector<trip> v2; // >= P without sup
vector<trip> v;

void calc(){
	sup = 0;
	cnt = 0;
	v.clear();

	for (int i = 0; i < N; i++){
		int tot, x, y;
		scanf("%d", &tot);
		x = tot / 3; y = tot % 3;
		if (y == 0){
			// x, x, x
			// x-1, x, x+1 (*)
			if (x >= P) cnt++;
			else if (x + 1 < P) {}
			else if (0 <= x - 1 && x + 1 <= 10) v.push_back(trip(x - 1, x, x + 1));
		}
		else if (y == 1){
			// x, x, x+1
			// x-1, x+1, x+1 (*)
			if (x + 1 >= P) cnt++;
		}
		else {
			// x, x+1, x+1
			// x, x, x+2 (*)
			if (x + 1 >= P) cnt++;
			else if (x + 2 < P) {}
			else if (x + 2 <= 10) v.push_back(trip(x, x, x + 2));
		}
	}
	sort(v.begin(), v.end(), cmp);
	if (S > (int)v.size()) S = (int)v.size();
	for (int i = 0; i < S; i++){
		if (v[i].c >= P) cnt++;
	}
	printf("%d\n", cnt);
}

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d%d%d", &N, &S, &P);
		printf("Case #%d: ", i);
		calc();
	}
	return 0;
}