#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <queue>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define REP(i,b) for(int i=0; i<b; i++)


typedef long long ll;
typedef vector<int> vint;
typedef pair<int,int> pii;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int c,n,k,b,t,x[100],v[100],a[100];
	scanf("%d",&c);
	FOR(r,1,c)
	{
        scanf("%d%d%d%d",&n,&k,&b,&t);
        FOR(i,1,n) scanf("%d",&x[i]);
        FOR(i,1,n) scanf("%d",&v[i]);
        FOR(i,1,n) if ((b-x[i])<=t*v[i]) a[i]=0; else a[i]=1;
        int s=0,t=0,p=0;
        for (int i=n;(i>=1 && p<k);i--)
        {
            t+=a[i];
            if (a[i]==0) { p++; s+=t; }
        }
        printf("Case #%d: ",r);
        if (p<k) printf("IMPOSSIBLE\n"); else printf("%d\n",s);
    }
		
	return 0;
}
