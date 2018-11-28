#include"iostream"
#include"stdio.h"
#include"algorithm"
#include"queue"
#include"string.h"
#include"vector"
#include"stack"
#include"set"
#define N 1005
#define M 1100000
using namespace std;
int a[N];
int n;

void init() {
}
void solve(int cases) {
	printf("Case #%d: ",cases);
	int t=0;
	int small=INT_MAX;
	int sum=0;
	for (int i = 0; i < n; ++i) {
		t^=a[i];
		if(a[i]<small)small=a[i];
		sum+=a[i];
	}
	if(t!=0)printf("NO\n");
	else printf("%d\n",sum-small);

}
int main() {
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i) {
		init();
		scanf("%d", &n);
		for (int j = 0; j < n; ++j) {
			scanf("%d", &a[j]);
		}
		solve(i + 1);
	}
	return 0;
}
