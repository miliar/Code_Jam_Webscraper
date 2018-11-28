#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("milkshakes.in");
ofstream fout("milkshakes.out");

struct data
{
    long num;
    long a[2001];
    int b[2001];
};

long n,m=0,a[2001],ans[2001],mint=2001;
data c[2001];

void init()
{
    fin>>n;
    m=0;
    mint=2001;
    long l,x,y;
    bool flag=true;
    fin>>l;
    for (long i=1;i<=l;i++)
    {
        flag=true;
        fin>>c[++m].num;
        for (long j=1;j<=c[m].num;j++)
        {
            fin>>x>>y;
            for (long t=1;t<j;t++)
                if (x==c[m].a[t])
                {
                    flag=false;
                    m--;
                    break;
                }
            if (!flag)
                break;
            c[m].a[j]=x;
            c[m].b[j]=y;
        }
    }
}

bool test()
{
    for (long i=1;i<=m;i++)
    {
        bool flag=false;
        for (long j=1;j<=c[i].num;j++)
            if (a[c[i].a[j]]==c[i].b[j])
            {
                flag=true;
                break;
            }
        if (!flag)
            return false;
    }
    return true;
}

void dfs(const long k,const long sum)
{
    if (sum>mint)
        return;
    if (k>n)
    {
        if (test())
        {
            for (long i=1;i<=n;i++)
                ans[i]=a[i];
            mint=sum;
        }
        return;
    }
    a[k]=0;
    dfs(k+1,sum);
    a[k]=1;
    dfs(k+1,sum+1);
}


void print()
{
    if(mint==2001)
    {
        fout<<"IMPOSSIBLE"<<endl;
        return;
    }
    for (long i=1;i!=n;i++)
        fout<<ans[i]<<' ';
    fout<<ans[n]<<endl;
}

int main()
{
    long T;
    fin>>T;
    for (long i=1;i<=T;i++)
    {
        init();
        dfs(1,0);
        fout<<"Case #"<<i<<": ";
        print();
    }
    return 0;
}
