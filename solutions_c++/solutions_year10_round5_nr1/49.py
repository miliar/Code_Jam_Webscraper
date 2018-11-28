#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int limit,tot,d;
bool isprime[1000000];
long long a[10];
int prime[1000000];
long long ans;

void ex_gcd(long long aa,long long b,long long c,long long &x,long long &y)
{
    if (b==0)
    {
        x=c/aa;
        y=0;
    }
    else
    {
        ex_gcd(b,aa % b,c,x,y);
        swap(x,y);
        y=y-aa/b*x;
    }
}

void check(long long aa,long long b,long long p)
{
    long long s=a[0];
    for (int i=1;i<tot;i++)
    {
        s=(s*aa+b) % p;
        if (s!=a[i]) return;
    }
    s=(s*aa+b) % p;
    if (ans==-1) ans=s;
    else
    if (ans==s) ans=s;
    else
        ans=-2;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    memset(isprime,true,sizeof(isprime));
    tot=0;
    for (int i=2;i<1000000;i++)
    {
        if (isprime[i]) prime[tot++]=i;
        for (int j=2;j*i<1000000;j++) isprime[j*i]=false;
    }
    prime[tot++]=1000001;
    int T;
    scanf("%d",&T);
    for (int i=1;i<=T;i++)
    {
        scanf("%d%d",&d,&tot);
        limit=1;
        for (int j=0;j<d;j++) limit=limit*10;
        for (int j=0;j<tot;j++) cin >> a[j];
        
        
        printf("Case #%d: ",i);
        
        if (tot >1 && a[0]==a[1]) {cout << a[0] << endl; continue;}
        if (tot<3) {cout << "I don't know." << endl; continue;}
        
        ans=-1;
        
        for (int j=0;prime[j]<limit;j++)
        {
            long long p=prime[j];
            bool pd=false;
            for (int i=0;i<tot;i++)
                if (p<=a[i]) pd=true;
            if (pd) continue;
            long long aa=a[1]-a[0],b=p,c=a[2]-a[1],x,y;
            if (aa==0) x=7;
                else ex_gcd(aa,b,c,x,y);
            x=(x % p + p) % p;
            y=((a[1]-a[0]*x) % p+p) % p;
            check(x,y,p);
        }
        if (ans==-2) cout << "I don't know." << endl;
            else cout << ans << endl;
    }
}
