#include <fstream>
using namespace std;
ifstream fin("C.in");
ofstream fout("C.out");
int main()
{
    long long t,T,R,K,N,i,j,now,ans,a[1001],max[1001],next[1001];
    fin>>T;
    for (t=1;t<=T;t++)
    {
        fout<<"Case #"<<t<<": ";
        fin>>R>>K>>N;
        for (i=1;i<=N;i++) fin>>a[i];
        for (i=1;i<=N;i++)
        {
            j=i%N+1;
            max[i]=a[i];
            while (j!=i&&max[i]+a[j]<=K)
            {
               max[i]+=a[j];
               j=j%N+1;
            }
            next[i]=j;
        }
        now=1;
        ans=0;
        for (i=1;i<=R;i++)
        {
            ans+=max[now];
            now=next[now];
        }
        fout<<ans<<endl;
    }
    return 0;
}
