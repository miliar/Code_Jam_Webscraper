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

int s2[32];

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	s2[0]=1;
	FOR(i,1,31) s2[i]=2*s2[i-1];
	int t,n,k;
	scanf("%d",&t);
	FOR(i,1,t)
	{
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",i);
        if ((k+1)%s2[n]==0) printf("ON\n"); else printf("OFF\n");
    }	
	return 0;
}
