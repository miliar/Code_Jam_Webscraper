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
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t,n,a[1100],b[1100],s;
	scanf("%d",&t);
	FOR(r,1,t)
	{
        scanf("%d",&n);
        FOR(i,1,n) scanf("%d%d",&a[i],&b[i]);
        s=0;
        FOR(i,1,n-1)
        FOR(j,i+1,n)
        if (a[i]<a[j] && b[i]>b[j] || a[i]>a[j] && b[i]<b[j]) ++s;
        printf("Case #%d: %d\n",r,s);
    }
	return 0;
}
