#include<iostream>
#include<cstdio>
using namespace std;
const int maxn=1001;
long long T,r,k,n;
long long Ans,G[maxn];
bool Visit[maxn];
long long Next[maxn],Sum[maxn];


long long GoFind(int &Now)
{
     int NextPos=Now;
     if (!Visit[Now])
     {
         Sum[Now]=0;
         NextPos=Now;
         while (Sum[Now]+G[NextPos]<=k)
         {
               Sum[Now]+=G[NextPos];
               NextPos=(NextPos+1) % n;
               if (NextPos==Now) break;
         }
         Next[Now]=NextPos;
         Visit[Now]=true;
     }
     int Back=Now;
     Now=Next[Now];
     return Sum[Back];
}
void Solve(int rank)
{
     memset(Visit,false,sizeof(Visit));
     for (int i=0;i<n;++i) cin>>G[i];
     int Now=0;
     Ans=0;
     for (int i=0;i<r;++i)
         Ans+=GoFind(Now);
     cout<<"Case #"<<rank<<": "<<Ans<<endl;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.txt","w",stdout);
    cin>>T;
    for (int i=0;i<T;++i)
    {
        cin>>r>>k>>n;
        Solve(i+1);
    }
    return 0;
}
