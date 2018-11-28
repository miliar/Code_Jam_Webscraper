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

int t,m,n,a[35][35],k[35];

void fun(int x,int y, int s)
{
    FOR(i,x,x+s-1)
    { if (a[i][y]<0) return; FOR(j,y+1,y+s-1) if (a[i][j]<0 || a[i][j]==a[i][j-1]) return; }
    FOR(i,x+1,x+s-1) if (a[i][y]==a[i-1][y]) return;
    k[s]++;
    FOR(i,x,x+s-1)  FOR(j,y,y+s-1) a[i][j]=-1;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	FOR(r,1,t)
	{
        scanf("%d%d",&m,&n); getchar();
        int b; char c;
        FOR(i,1,m)
        {
            FOR(j,1,n/4) 
            { 
                c=getchar(); if (c<='9') b=c-'0'; else b=10+c-'A';
                a[i][4*j]=b%2; b/=2; a[i][4*j-1]=b%2; b/=2; 
                a[i][4*j-2]=b%2; b/=2; a[i][4*j-3]=b%2;
            }
            getchar();
        }
        for (int s=min(n,m); s>1; --s)
        {
            k[s]=0;
            FOR(i,1,m-s+1)
            FOR(j,1,n-s+1)
            fun (i,j,s);
        }
        k[1]=n*m; FOR(i,2,min(n,m)) k[1]-=k[i]*i*i;
        int s=0; FOR(i,1,min(n,m)) if (k[i]>0) ++s;
        printf("Case #%d: %d\n",r,s);
        for(int i=min(n,m);i>0;--i) if (k[i]>0) printf("%d %d\n",i,k[i]);
    }
	return 0;
}
