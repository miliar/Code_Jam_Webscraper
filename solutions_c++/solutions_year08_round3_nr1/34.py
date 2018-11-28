#include <fstream>


using namespace std;

ifstream fin("text.in");
ofstream fout("text.out");

long p,k,l;
long f[2000];

void sort()
{
  for (long i=0;i<l-1;i++)
    for (long j=i+1;j<l;j++)
        if (f[i]<f[j])
        {
            long temp=f[i];
            f[i]=f[j];
            f[j]=temp;
        }
}


void init()
{
    fin>>p>>k>>l;
    for (long i=0;i!=l;i++)
        fin>>f[i];
    sort();
}

void cal()
{
    long long sum=0;
    for (long i=0;i!=l;i++)
        sum+=(int(i/k)+1)*f[i];
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
        cal();
    }
    return 0;
}
