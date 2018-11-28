#include<fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("data.out");

long long T,N,K;
long long fn[32];

int main()
{
    fin>>T;

    for (int i=1;i<=30;i++)
        fn[i]=(1<<i);

    for (int u=1;u<=T;u++)
    {
        fin>>N>>K;
        long long ys=K%fn[N];
        fout<<"Case #"<<u<<": ";
        if (ys==fn[N]-1)
            fout<<"ON";
        else
            fout<<"OFF";
        fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
