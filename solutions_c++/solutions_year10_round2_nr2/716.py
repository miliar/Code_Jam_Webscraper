#include <fstream>
#include <iostream>
using namespace std;
ifstream fin("B.in");
ofstream fout("B.out");
int main()
{
    int c,C,N,K,B,T,i,j,k,ans,x[100],v[100];
    double reachT[100];
    fin>>C;
    for (c=1;c<=C;c++)
    {
        fin>>N>>K>>B>>T;
        for (i=1;i<=N;i++) fin>>x[i];
        for (i=1;i<=N;i++) fin>>v[i];
        for (i=1;i<=N;i++)
           if (x[i]+v[i]*T>=B) reachT[i]=(B-x[i])/(v[i]*1.0);
           else reachT[i]=0;
        for (i=1;i<=N;i++) if (reachT[i]>0)
           for (j=i+1;j<=N;j++) if (reachT[i]<reachT[j])
               reachT[i]=reachT[j];
        k=0;
        ans=0;
        for (i=N;i>=1;i--)
           if (reachT[i]>0)
           {
              k++;
              for (j=i+1;j<=N;j++) if (reachT[i]<reachT[j]||reachT[j]==0) ans++;
              if (k==K) break;
           }
        fout<<"Case #"<<c<<": ";
        if (k==K) fout<<ans<<endl; 
        else fout<<"IMPOSSIBLE"<<endl;
    }
    system("pause");
    return 0;
}
