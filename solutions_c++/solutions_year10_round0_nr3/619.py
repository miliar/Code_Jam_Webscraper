#include<fstream>

using namespace std;

const char iname[]="C.in";
const char oname[]="C.out";
const long long maxn=2005;

ifstream f(iname);
ofstream g(oname);

long long a[maxn],r,k,b[maxn],been[maxn],step[maxn],pas,steps,stop,aux,n,i,j;

long long w[maxn];

long long m,c[maxn];

void test(long long testcase)
{

    f>>r>>k>>n;
    for(i=0;i<n;++i)
        f>>a[i],a[n+i]=a[i];
    for(i=0;i<n;++i)
    {
        b[i]=a[i];
        for(j=i+1;j<n+i;++j)
        {
            b[i]+=a[j];
            if(b[i]>k)
            {
                b[i]-=a[j];
                break;
            }
        }
        w[i]=j%n;
    }

    i=0;
    m=0;
    for(i=0;i<2*n;++i)
        been[i]=0;
    for(i=0;i<2*n;++i)
        c[i]=0;
    i=0;
    pas=0;
    while(been[i]==0&&r)
    {
        --r;
        m+=b[i];
        been[i]=1;
        step[i]=++pas;
        if(been[w[i]]==0)
            c[w[i]]=c[i]+b[i];
        else
            stop=c[i]+b[i];
        i=w[i];
    }
    if(r)
    {
        steps=++pas-step[i];
        aux=steps;
        steps=r/steps;
        r-=aux*steps;
        m+=1LL*(stop-c[i])*steps;
        j=i;
        for(i=0;i<n*2;++i)
            been[i]=0;
        while(r)
        {
            --r;
            m+=b[j];
            j=w[j];
        }
    }

    g<<"Case #"<<testcase<<": "<<m<<"\n";

}

int main()
{
    long long t,i;
    f>>t;
    for(i=1;i<=t;++i)
        test(i);
}
