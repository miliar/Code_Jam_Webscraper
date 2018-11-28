#include<iostream>
#include<stack>
#include<conio.h>
#include<fstream>
using namespace std;
typedef long long int ll;
int main()
{
    int nt,g=1;
    ifstream din("C-small-attempt0.in");
    ofstream dout("out.txt");
    din>>nt;
    while(nt--)
    {
               ll n,m,x,y,z;
               din>>n>>m>>x>>y>>z;
               ll a[m],i,j;
               for(i=0;i<m;i++)
                din>>a[i];
               ll b[n];
               for(i=0;i<n;i++)
               {
                               b[i]=a[i%m];
                               a[i%m]=(x*a[i%m]+y*(i+1))%z;
               }
               ll count[n],ans=0;
               for(i=0;i<n;i++)
                 count[i]=1;
               for(i=1;i<n;i++){
                                
                 for(j=0;j<i;j++)
                 {
                                 
                                 if(b[i]>b[j])
                                 {
                                              count[i]+=(count[j])%1000000007;
                                 }
                 }
                 ans=(ans%1000000007)+(count[i]%1000000007);
                 ans%=1000000007;
          }
          dout<<"Case #"<<g<<": "<<ans+1<<endl;
          cout<<ans+1<<endl;
          g++;
       }
 getch();
return 0;
}
