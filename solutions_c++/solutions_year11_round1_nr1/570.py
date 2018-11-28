#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<time.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

typedef long long LL;
typedef pair<int,int> pii;

LL gcd(LL a, LL b)
{
    if(b==0) return a;
    return gcd(b,a%b);
}

LL N, Pd, Pg;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Alarge_out.txt","w",stdout);

    int T; scanf("%d",&T);

    REP(t,1,T)
    {
        cin>>N>>Pd>>Pg;

        printf("Case #%d: ",t);

        if(Pg==100 && Pd < 100)
        {
            puts("Broken");
        }
        else if(Pd > 0 && Pg == 0)
        {
            puts("Broken");
        }
        else
        {
            LL g = gcd(100,Pd);
            LL mn = 100/g;

            if(mn <= N)
            {
                puts("Possible");
            }
            else
                puts("Broken");
        }
    }

    return 0;
}
