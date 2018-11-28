using namespace std;
#include<cstdio>
#include<algorithm>
#define Nm 256
#define s(i) (S[i]-'0')
int n,t,na,nb;
struct trip
{
    int a,b,c;
} T[Nm];

void read()
{
    char S[12];
    int i,na,nb;

    scanf("%d%d%d ",&t,&na,&nb);
    for(n=na+nb,i=0;i<n;++i)
    {
        gets(S);
        T[i].a=(s(0)*10+s(1))*60+s(3)*10+s(4);
        T[i].b=(s(6)*10+s(7))*60+s(9)*10+s(10);
        T[i].c=i>=na;
    }
}

bool cmp(trip a, trip b)
{
    return a.a<b.a;
}

void solve()
{
    int i,j,time,p;

    sort(T,T+n,cmp);

    for(na=nb=i=0;i<n;++i)
    {
        if(T[i].c==2) continue;
        if(T[i].c) ++nb;
        else ++na;
        time=T[i].b+t; p=T[i].c^1; T[i].c=2; j=i+1;
        while(1)
        {
            for(;j<n;++j)
                if(T[j].c==p && T[j].a>=time) break;
            if(j==n) break;
            time=T[j].b+t; p^=1; T[j].c=2; ++j;
        }
    }
}

int main()
{
    int i,t;

    freopen("train.in","r",stdin);
    freopen("train.out","w",stdout);

    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        read();
        solve();
        printf("Case #%d: %d %d\n",i,na,nb);
    }
    return 0;
}

