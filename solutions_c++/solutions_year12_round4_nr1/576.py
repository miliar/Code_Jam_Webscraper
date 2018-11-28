
//Michał Glapa
#include<cstdio>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<cstdlib>
#include<time.h>
#include<stack>
#include<cmath>
#include<iostream>
#include<cstring>
using namespace std;
#define ret return
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define FORD(i,j,k) for(int i=j;i>=k;i--)
#define ll long long
#define pii  pair<int, int>
#define vi vector<int >
#define pb push_back
#define mp make_pair
#define make(n) int n; scanf("%d",&n)
#define st first
#define nd second
#define INF 2000000001
#define VAR(i,n) __typeof(n) i = (n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)
#define FORDEACH(i,c) for( VAR(i,(c).rbegin(),i!=(c).rend();i++)
#define REP(i,n) FOR(i,0,n)
#define ld long double
const long long INFLL = (ll)INF * (ll)INF;
const ld EPS = 10e-9;

#define MAXN 1000000
int d[MAXN];
int h[MAXN];
int best[MAXN];
int main()
{
    make(t);
    FOR(q,1,t+1)
    {
        make(n);
        FOR(i,0,n)
        {
            make(dd);make(hh);
            d[i]=dd;
            h[i]=hh;
            best[i]=-1;
        }
        make(x);
        d[n]=x;
        h[n]=INF;
        best[n]=-1;
        best[0] = min(d[0],h[0]);
        FOR(i,1,n+1)
        {
            FOR(j,0,i)
            {
                if(best[j]>=0 && d[j]+best[j] >= d[i])
                    best[i] = max(best[i],min(d[i]-d[j],h[i]));
            }
        }
        if(best[n]!=-1)
        {
            printf("Case #%d: YES\n",q);
        }
        else
            printf("Case #%d: NO\n",q);
    }
}

