#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

int fib[128];

LL calc(int a, int b) {
	int i;
	LL s = 0;
	for (i = 1 ; fib[i] <= MAX(a,b) ; i += 2) {
		s += MIN(a / fib[i-1], b / fib[i]);
		if (fib[i-1] != fib[i])
			s += MIN(b / fib[i-1], a / fib[i]);
	}
	return s;
}

int check(int a, int b) {
	if (a < b) swap(a,b);
	int flg = 1;
	while (b != 0) {
		if (a / b > 1) return flg;
		int tmp = b;
		b = a % b;
		a = tmp;
		flg = 1 - flg;
	}
	return 0;
}

int main() {
	freopen("c-small.in","r",stdin);
	freopen("c-small.out","w",stdout);
	fib[0] = 1; fib[1] = 1;
	int i, ca, T;
	for (i = 2 ; i < 100 ; i++)
		fib[i] = fib[i-1] + fib[i-2];
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++) {
		int A1,A2,B1,B2;
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		/*
		LL tot = (LL)(A2-A1+1)*(B2-B1+1);
		printf("%I64d %I64d %I64d %I64d\n",calc(A2,B2),
			calc(A1-1,B2),calc(A2,B1-1),calc(A1-1,B1-1));
		printf("Case #%d: %I64d\n",ca,
			tot-(calc(A2,B2)-calc(A1-1,B2)-calc(A2,B1-1)+calc(A1-1,B1-1)));
		*/
		int ans = 0, a, b;
		for (a = A1 ; a <= A2 ; a++)
			for (b = B1 ; b <= B2 ; b++)
				if (check(a,b)) {
					//printf("(%d,%d)\n",a,b);
					++ans;
				}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
