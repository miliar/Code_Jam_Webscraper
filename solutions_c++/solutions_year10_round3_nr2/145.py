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
	int l,p,c,tt,s,d,t;
	ll l1,p1,c1;
	scanf("%d",&tt);
	FOR(r,1,tt)
	{
        scanf("%d%d%d",&l,&p,&c);
        l1=l; p1=p; c1=c;
        s=0; while (l1<p1) { s++; l1*=c1; }
        d=1; t=0;
        while (s>d) { t++; d*=2; }
        printf("Case #%d: %d\n",r,t);
    }
		
	return 0;
}
