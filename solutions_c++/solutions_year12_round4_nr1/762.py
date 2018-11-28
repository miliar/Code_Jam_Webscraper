#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define fr(a,b,c) for (int a=b;a<=c;a++)
#define frr(a,b,c) for (int a=b;a>=c;a--)
#define rep(a,b) for (int a=0;a<b;a++)
#define repp(a,b) for (int a=b-1;a>=0;a--)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define pii pair<int,int>
#define oo 1000111222
#define maxN 1
using namespace std;

long long n,d[10010],l[10010],f[10010];

int main()
{
	freopen("asmall.in","r",stdin); freopen("asmall0.out","w",stdout);
	int test;
	cin >> test;
	for (int itest=1;itest<=test;itest++)
	{
		cin >> n;
		fr(i,1,n) cin >> d[i] >> l[i];
		cin >> d[n+1];
		l[n+1]=1LL*oo*oo;
		
		memset(f,0,sizeof(f));
		f[1]=min(d[1],l[1]);
		fr(i,1,n)
			fr(j,i+1,n+1)
				if (f[i]+d[i]>=d[j])
					f[j]=max(f[j],min(l[j],d[j]-d[i]));
				
		printf("Case #%d: ",itest);
		puts(f[n+1]?"YES":"NO");
	}
}
