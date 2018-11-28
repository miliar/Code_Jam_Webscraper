#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define pi 3.141592653589
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

int a[1000],p[1000];
ll s[1000],b[2000];

int main()
{
	int T;
	scanf("%d",&T);
	for (int I=0;I<T;I++){
		int R,k,n;
		ll ans=0;
		scanf("%d%d%d",&R,&k,&n);
		for (int i=0;i<n;i++)scanf("%d",a+i);
		b[0]=a[0];
		for (int i=1;i<n;i++)b[i]=(ll)a[i]+b[i-1];
		for (int i=n;i<2*n;i++)b[i]=(ll)a[i-n]+b[i-1];
		if (b[n-1]<=k){
			ans=(ll)R*(ll)b[n-1];
		} else {
			for (int i=0;i<n;i++){
				int l=i;
				int r=2*n;
				while (r-l>1){
					int x=(l+r)/2;
					if (b[x]-(i?b[i-1]:0)>k)r=x;else l=x;
				}
				s[i]=b[l]-(i?b[i-1]:0);
				p[i]=(l+1)%n;
			}
			int cur=0;
			for (int i=0;i<R;i++){
				ans+=(ll)s[cur];
				cur=p[cur];
			}
		}
		printf("Case #%d: ",I+1);cout << ans << endl;
	}
	return 0;
}
