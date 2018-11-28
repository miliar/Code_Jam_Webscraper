#include<fstream>
using namespace std;

ifstream fin("C-large.in");
ofstream fout("data.out");

const int maxn=1003;

long long T,R,K,N;
long long g[maxn];

long long lst[maxn];
long long tot[maxn];

bool vis[maxn];
long long a[maxn],cnt;

long long sum[maxn];

void Make_lst()
{
    int sum=0;
    int len,j;

    for (int i=1;i<=N;i++)
        if (sum+g[i]<=K)
        {
            sum+=g[i];
            len=i;
        }
        else
            break;
    lst[1]=len;
    tot[1]=sum;

    for (int i=2;i<=N;i++)
    {
        sum-=g[i-1];
        len--;

        if (len==0)
        {
            sum=g[i];
            j=i;
            len=1;
        }
        else
            j=i+len-1;

        while (1==1)
        {
            j++;
            if (j>N) j-=N;
            if (j==i) break;
            if (sum+g[j]<=K)
            {
                sum+=g[j];
                len++;
            }
            else break;
        }
        lst[i]=len;
        tot[i]=sum;
    }
}

void work()
{
    memset(vis,0,sizeof(vis));
    cnt=0;

    int k=1;
    while (1==1)
    {
        if (1==vis[k]) break;

        vis[k]=1;
        cnt++;
        a[cnt]=k;

        k=k+lst[k];
        if (k>N) k-=N;
    }

    int st;
    int zhouqi;
    for (int i=1;i<=cnt;i++)
        if (a[i]==k)
        {
            st=i;
            break;
        }
    zhouqi=cnt-st+1;

    for (int i=1;i<=cnt;i++)
        sum[i]=sum[i-1]+tot[a[i]];

    long long ans;
    if (R<=st) ans=sum[R];
    else
    {
        ans=sum[st-1];
        R-=(st-1);
        long long tmp=R/zhouqi;
        ans=ans+(sum[cnt]-sum[st-1])*tmp;
        tmp=R%zhouqi;
        ans=ans+sum[st+tmp-1]-sum[st-1];
    }

    fout<<ans<<endl;
}

int main()
{
    fin>>T;
    for (int u=1;u<=T;u++)
    {
        fin>>R>>K>>N;
        for (int i=1;i<=N;i++)
            fin>>g[i];
        Make_lst();
        fout<<"Case #"<<u<<": ";
        work();
    }

    fin.close();
    fout.close();
    return 0;
}
