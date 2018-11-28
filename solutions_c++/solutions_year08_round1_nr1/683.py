#include <fstream>
using namespace std;

ifstream fin("scalar.in");
ofstream fout("scalar.out");

long n,a[2000],b[2000];

void init()
{
    fin>>n;
    for (long i=1;i<=n;i++)
        fin>>a[i];
    for (long i=1;i<=n;i++)
        fin>>b[i];
}

void sortA()
{
    for (long i=1;i<n;i++)
        for (long j=i+1;j<=n;j++)
            if (a[i]>a[j])
            {
                long temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
}

void sortB()
{
    for (long i=1;i<n;i++)
        for (long j=i+1;j<=n;j++)
            if (b[i]>b[j])
            {
                long temp=b[i];
                b[i]=b[j];
                b[j]=temp;
            }
}

void print()
{
    long sum=0;
    for (long i=1;i<=n;i++)
        sum+=a[i]*b[n-i+1];
    fout<<sum<<endl;
}

int main()
{
    long T;
    fin>>T;
    for (long i=1;i<=T;i++)
    {
        init();
        fout<<"Case #"<<i<<": ";
        sortA();
        sortB();
        print();
    }
    return 0;
}
