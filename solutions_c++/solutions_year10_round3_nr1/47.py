#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;
typedef long long LLD;

#define x first
#define y second

int vectorMul(PII a, PII b, PII c) {
	return (c.x - a.x) * (c.y - b.y) - (c.y - a.y) * (c.x - b.x);
}

bool lineIntersect(int a, int b, int c, int d) {
	return max (a, b) >= min (c, d) && max (c, d) >= min (a, b);
}

bool intersect(PII a, PII b, PII c, PII d) {
	int s11 = vectorMul(a, b, c);
	int s12 = vectorMul(a, b, d);
	int s21 = vectorMul(c, d, a);
	int s22 = vectorMul(c, d, b);
	if (s11 == 0 && s12 == 0 && s21 == 0 && s22 == 0)//on line
		return lineIntersect(a.x, b.x, c.x, d.x) && lineIntersect(a.y, b.y, c.y, d.y);
	else
		return ((LLD)s11 * s12 <= 0) && ((LLD)s21 * s22 <= 0);
}


void solution(int tstNum){
	int n;
	scanf("%d", &n);
	int res = 0;
	int a[1000], b[1000];
	for (int i = 0; i < n; i++){
		scanf("%d%d", &a[i], &b[i]);
	}
	for (int i = 0; i < n; i++){
		for (int j = i + 1; j < n; j++){
			res += intersect(PII(0, a[i]), PII(10, b[i]), PII (0, a[j]), PII(10, b[j]));
		}
	}
	printf("Case #%d: %d\n", tstNum + 1, res);
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}