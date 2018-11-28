#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn=2000+10;
const int oo=500000000;

int A[maxn];
pair<int,int> res[maxn];
bool done[maxn];
int n,t,id;

bool work(int l,int r,int ll,int rr,int kk)
{
    if (l>r) return 1;
    if (A[l]>rr) return 0;
    
    
    if (!done[l])
    {
        res[l].second=0;
        done[l]=1;
    }

    if (l==r) return 1;
    if (!done[A[l]])
    {
        int kk=(res[rr].second-res[l].second)/(res[rr].first-res[l].first)+1;
        res[A[l]].second=res[l].second+(res[A[l]].first-res[l].first)*kk;
        done[A[l]]=1;
    }
    return work(l+1,A[l]-1,l,A[l],kk)&work(A[l],r,A[l],rr,kk);
}

bool det(pair<int,int> a,pair<int,int> b,pair<int,int> c)
{
    b.first-=a.first;b.second-=a.second;
    c.first-=a.first;c.second-=a.second;
    long long res=(long long)b.first*c.second-(long long)b.second*c.first;
    return res>0;
}

int main()
{
    //freopen("input.txt","r",stdin);
    freopen("c1.in","r",stdin);

    for (scanf("%d",&t);t--;)
    {
        scanf("%d",&n);
        for (int i=1;i<n;i++) scanf("%d",&A[i]);
        
        res[0]=make_pair(0,0);
        res[n]=make_pair(oo,oo);
        for (int i=1;i<n;i++) done[i]=0;
        done[0]=done[n]=1;

        for (int i=1;i<=n;i++) res[i].first=n*i;
        printf("Case #%d: ",++id);
        if (!work(1,n-1,0,n,oo/(n*n))) printf("Impossible\n");
        else 
        {
            for (int i=1;i<=n;i++) printf("%d%c",res[i].second,i==n?'\n':' ');
            
            for (int i=1;i<n;i++)
            {
                int now=i+1;
                for (int j=i+2;j<=n;j++)
                if (det(res[i],res[now],res[j])) now=j;
                if (now!=A[i])
                    printf("- -\n");
            }
        }
    }
}


