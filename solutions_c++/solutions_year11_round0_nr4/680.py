#include"iostream"
#include"stdio.h"
#include"algorithm"
#include"queue"
#include"string.h"
#include"vector"
#include"stack"
#include"set"
#define N 1005
using namespace std;
int a[N];
int n;
void init() {

}
void solve(int cases) {
	double result=0;
	for (int i = 1; i <= n; ++i) {
		if(i!=a[i])result++;
	}
	printf("Case #%d: %.6lf\n",cases,result);

}
int main() {
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	init();
	for (int i = 0; i < T; ++i) {

		scanf("%d", &n);
		for (int j = 1; j <= n; ++j) {
			scanf("%d", &a[j]);
		}
		solve(i + 1);
	}
	return 0;
}
