#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int main()
{
    int t,T,N,i,j,A[10000],B[10000],ans;
    fin>>T;
    for (t=1;t<=T;t++)
    {
        ans=0;
        fin>>N;
        for (i=1;i<=N;i++) fin>>A[i]>>B[i];
        for (i=1;i<=N;i++)
           for (j=i+1;j<=N;j++)
              if (A[i]<A[j]&&B[i]>B[j]||A[i]>A[j]&&B[i]<B[j]) ans++;
        fout<<"Case #"<<t<<": "<<ans<<endl;
    }
    system("pause");
    return 0;
}
