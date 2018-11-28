#include<cstdio>
#include<ctime>
#include<algorithm>
using namespace std;

const int maxn=1000+10;
pair<int,int> r[maxn];
pair<int,int> P[maxn],res[maxn];
int p[maxn];
int n,t,w,l;
int id;
pair<int,int> A[maxn];

bool check(pair<int,int> p,int n)
{
    int rr=r[n].first;
    if (p.first+rr<0 || p.first+rr>w || p.second+rr<0 || p.second+rr>l) return 0;
    for (int i=1;i<n;i++)
    {
        if (P[i].first>=p.first+rr*2 || P[i].first+r[i].first*2<=p.first ||
            P[i].second>=p.second+rr*2 || P[i].second+r[i].first*2<=p.second)
            continue;
        return 0;
    }
    return 1;
}

int main()
{
    freopen("b2.in","r",stdin);

    for (scanf("%d",&t);t--;)
    {
        scanf("%d%d%d",&n,&w,&l);
        for (int i=1;i<=n;i++) scanf("%d",&r[i].first),r[i].second=i;
        for (int i=1;i<=n;i++) r[i].first*=-1;
        sort(r+1,r+n+1);
        for (int i=1;i<=n;i++) r[i].first*=-1;

        for (int i=1;i<=n;i++)
        {
            pair<int,int> res=make_pair(w+1,l+1);
            for (int j=0;j<=i;j++)
            {
                pair<int,int> now=P[j];
                now.first+=r[j].first*2;
                if (now.first<0) now.first=0;
                if (now.second<0) now.second=0;
                if (now.first==0) now.first-=r[i].first;
                if (now.second==0) now.second-=r[i].first;
                if (check(now,i)) res=min(res,now);

                now=P[j];
                now.second+=2*r[j].first;
                if (now.first<0) now.first=0;
                if (now.second<0) now.second=0;
                if (now.first==0) now.first-=r[i].first;
                if (now.second==0) now.second-=r[i].first;
                if (check(now,i)) res=min(res,now);
            }
            if (res.first==w+1) printf("- - %d %d\n",i,r[i].first);
            P[i]=res;
        }

        for (int i=1;i<=n;i++) res[r[i].second]=make_pair(P[i].first+r[i].first,P[i].second+r[i].first);
        printf("Case #%d:",++id);
        for (int i=1;i<=n;i++) printf(" %d %d",res[i].first,res[i].second);
        printf("\n");
    }
}


