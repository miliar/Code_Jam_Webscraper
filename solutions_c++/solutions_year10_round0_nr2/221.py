#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)

int gcd(int a,int b){
	if(b==0) return a;
	return gcd(b,a%b);
}
int main(){
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t,cs,n,i,j,g,gx,mx,ans,a[1005];
	scanf("%d",&t);
	for(cs=1;cs<=t;cs++){
		scanf("%d",&n);
		mx = 0;
		for(i = 0;i<n;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+n);
		g = a[1] - a[0];
		for(i=2;i<n;i++){
			g = gcd(g,a[i] - a[i-1]);
		}
		ans = g - a[0] % g;
		for(i = 0;i<n;i++){
			if(a[i] % g ) break;
		}
		if(g==1 || i==n)
			printf("Case #%d: %d\n",cs,0);
		else {
			printf("Case #%d: %d\n",cs,g - a[0]%g);
		}
	}
	return 0;
}