#include <cstdio>
//#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int c=50;
int r[c];
int ans;
int ii,t,n;
int main() {
	char h;
	int i,j,k;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d",&n);
		for (i=1; i<=n; ++i) {
			r[i]=0;
			for (j=1; j<=n; ++j) {
				do h=getchar(); while (h!='0' && h!='1');
				if (h=='1') r[i]=j;
			}
		}
		ans=0;
//		for (i=1; i<=n; ++i) cerr << r[i] << ' ';
//		cerr << '\n';
		for (i=1; i<=n; ++i) if (r[i]>i) {
			j=i+1;
			while (r[j]>i) ++j;
			ans+=j-i;
			for (k=j; k>=i+1; --k) swap(r[k],r[k-1]);
//			cerr << "i = " << i << '\n';
//			for (k=1; k<=n; ++k) cerr << r[k] << ' ';
//			cerr << '\n';
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}