#include <iostream>
#include <fstream>
using namespace std;

int N,K,T;

int main()
{
    ifstream fin("Alarge.in");
    ofstream fou("Alarge.out");
    fin>>T;
 //   cin>>T;
    for (int t=1;t<=T;t++)
    {
      fin>>N>>K;
      //cin>>N>>K;
      long tmp,fi; tmp=1;
      bool ans;
      ans = false;
      if ((K%2)==0) ans =false;
      else
      {
          tmp=1;
          for (int i=1;i<N;i++) tmp=tmp*2;
          for (int i=N;i<=30;i++)
          {
              if (ans) break;
              tmp = tmp*2;
              fi = tmp-1;
              if (fi>K) break;
                 else
                 {
                     int tk;
                     tk = K - fi;
                     if ((tk%(tmp*2))==0) ans=true;
                 }
          }
      }
       if (ans)
       {
           fou<<"Case #"<<t<<": ON"<<endl;
       }
       else
       {
           fou<<"Case #"<<t<<": OFF"<<endl;
        }
    }
    fin.close();
    fou.close();
    return 0;
}
