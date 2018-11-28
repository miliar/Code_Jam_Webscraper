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
#define CL(a,b) memset(a,b,sizeof a)


typedef long long ll;
typedef vector<int> vint;
typedef pair<int,int> pii;

char c[400][400],s[400];
int b[2][400*400],k,t,n;
const int p=150;

bool zyf(char d)
{ return (d<='9' && d>='0'); }
	
int trys(int x,int y)
{
    int r=0,si,sj;
    FOR(i,p,p+2*n-2)    
    FOR(j,p,p+2*n-2)
    if (abs(p+n-1-i)+abs(p+n-1-j)<n && (i+j+n+1)%2==0)
    {
        si=2*x-i; sj=2*y-j;
        if (zyf(c[si][j]))
        { if (c[i][j]!=c[si][j]) return -5; } else
        { c[si][j]=c[i][j]; b[0][k]=si; b[1][k]=j; k++; }
        if (zyf(c[i][sj]))
        { if (c[i][j]!=c[i][sj]) return -5; } else
        { c[i][sj]=c[i][j]; b[0][k]=i; b[1][k]=sj; k++; }
        r=max(r,abs(x-i)+abs(y-j)+1);
    }
    return r;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	CL(c,0);
	//int j;
    FOR(r,1,t)
    {
        int mi=1000000000;
        scanf("%d",&n);
        getchar();
        CL(c,0);
        FOR(i,0,2*n-2)
        {
            gets(s);
            int j=0;
            while (s[j]) { c[p+i][p+j]=s[j]; j++; }
        }
        FOR(i,p-1,p+2*n-1)
        FOR(j,p-1,p+2*n-1)
        {
            k=0;
            int z=trys(i,j);
            if (z>0)
            mi=min(mi,z*z-n*n);
            while(k>0) { k--; c[b[0][k]][b[1][k]]=0; }
        }
        printf("Case #%d: %d\n",r,mi);
    }    		
	return 0;
}
