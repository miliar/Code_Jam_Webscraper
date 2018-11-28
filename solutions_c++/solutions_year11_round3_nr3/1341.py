#include<iostream>
#include<fstream>
#include<sstream>
#include<cstring>
#include<vector>
#include<utility>
#include<cmath>
//#include<>
using namespace std;

#define for_n(i,n) for( (i)=0;(i)<(n);(i)++)
#define lli long long int
#define ulli unsigned long long int

int main()
{
    ifstream fin("in3.txt");
    ofstream fout("out3.txt");
    int T;
    fin>>T;int t;
    for_n(t,T)
    {
              ulli N,L,H,i;
              fin>>N>>L>>H;
              
              vector<ulli> A; A.resize(0);A.resize(N);lli ans=-1;
              vector<ulli> B;B.resize(0);B.resize(H+1);for_n(i,H+1)B[i]=0;  
              for_n(i,N)
              {
                        fin>>A[i];
              }
              for_n(i,N)
              {
                        for(ulli j=L;j<=H;j++)
                        {
                                if(j%A[i]==0 || A[i]%j == 0){B[j]+=(i+1);}
                        }
              }
              for(ulli j=L;j<=H;j++){
                      if(B[j]==(N*(N+1))/2 ){ans = j;break;}
                      }
                      cout<<"Case #"<<t+1<<": ";fout<<"Case #"<<t+1<<": ";
                      if(ans == -1){cout<<"NO\n";fout<<"NO\n";}
                      else {cout<<ans<<"\n";fout<<ans<<"\n";}
    }
              
     fin.close();         
                                
               
    int y;cin>>y;
    return 0;
}
