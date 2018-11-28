#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;

struct node {
	int a,b;
};
bool operator < (const node &n1,const node &n2) {
	return n1.a<n2.a || n1.a==n2.a && n1.b<n2.b;
}
int i,j,ans,testcase,test,n;
node a[1005];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&testcase);
	for (test=1; test<=testcase; ++test) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i)
			scanf("%d%d",&a[i].a,&a[i].b);
		sort(a+1,a+1+n);
		
		ans=0;
		for (i=1; i<=n; ++i) {
			for (j=1; j<i; ++j)
				if (a[i].b<a[j].b) ++ans;
		}
		printf("Case #%d: %d\n",test,ans);
			
	}
	return 0;
}