#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt,n,last1,last2,t1,t2;

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		last1=last2=0; t1=t2=1;
		for (int i=1;i<=n;++i) {
			char ch; int x;
			cin >> ch >> x;
			if (ch=='O') {
				last1=max(last2+1,last1+abs(x-t1)+1);
				t1=x;
			} else {
				last2=max(last1+1,last2+abs(x-t2)+1);
				t2=x;
			}
		}
		printf("Case #%d: %d\n",ii,max(last1,last2));
	}
}
