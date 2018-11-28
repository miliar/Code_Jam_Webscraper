#include<iostream>
#include<fstream>
using namespace std;
int main()
    {
          ifstream fin;
          ofstream fout;
          long n;
          fin.open("a.in");
          fout.open("a.out");
          fin>>n;
          long  i,j,k,l,p,t,temp;
          long zimu[2000];
          long long ans;
          for (t=1;t<=n;t++)
           {fin>>p>>k>>l;
           memset(zimu,0,sizeof(zimu));
           for (i=1;i<=l;i++)
            fin>>zimu[i];
            ans=0;             
            for (i=1;i<=l-1;i++)
             for (j=i+1;j<=l;j++)
              if (zimu[i]<zimu[j])
               {
                temp=zimu[i];
                zimu[i]=zimu[j];
                zimu[j]=temp;
               };
              for (i=1;i<=p;i++)
               {
                 for (j=1;j<=k;j++)
                  {
                    if ((i-1)*k+j>l) break;               
                  ans=ans+zimu[((i-1)*k)+j]*i;
                  } ;             
               } 
             fout<<"Case #"<<t<<": "<<ans<<endl;  
           }
          return 0;
    }
