#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <fstream>
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <iomanip>
#include <list>  
using namespace std;  
class D{
      public:
      int n;
      int d;
};
int gcd( int m, int n)
{
while( m!= n) // execute loop until m == n
{
if( m > n)
m= m - n; // large - small , store the results in large variable
else
n= n - m;
}
return ( m); // m or n is GCD
}

int lcm( int m, int n)
{
return( m * n / gcd (m,n)); // product of 2 numbers / gcd is lcm
}
int main(){
    ifstream in("A-small-attempt2.in");
    ofstream out("A-small-attempt2.out");
    int T;
    in>>T;
    int oo=1;
    while(T--){
               int N;
               in>>N;
               char a[200][200];
               D f[200],f2[200],f3[200];
               D temp;
               int z=0;
               while(N--) in>>a[z++];
               N=z;
               temp.n=0; temp.d=0;
               for(int i=0;i<N;i++){
                       f[i].n=f[i].d=f2[i].n=f2[i].d=f3[i].n=f3[i].d=0;
               }
               for(int i=0;i<N;i++){
                       for(int j=0;j<N;j++){
                               if(a[i][j]=='.')continue;
                               ++f[i].d;
                               if(a[i][j]=='1') ++f[i].n;
                       }
                       int k;
                      if(f[i].n&&f[i].d) if((k=gcd(f[i].n,f[i].d))!=1) f2[i].n/=k,f2[i].d/=k;
               }
               for(int i=0;i<N;i++){
                       int k=0;
                       for(int j=0;j<N;j++){
                        if(a[i][j]=='.')continue;      
                        k++;
                        D tt;
                        tt.n= f[j].n;
                        tt.d= f[j].d;
                           --tt.d;
                        if(a[j][i]=='1') --tt.n;
                        if(!f2[i].d){
                                     f2[i].n=tt.n;
                                     f2[i].d=tt.d;
                        }
                        else{                      
                          int l=0;
                          if(tt.d&&f2[i].d)l=lcm(tt.d,f2[i].d);
                          f2[i].n= (f2[i].n*(l/f2[i].d))+ (tt.n*(l/tt.d));
                          f2[i].d= l;
                        }
                       }
                       f2[i].d *= k;
                       if(f2[i].n&&f2[i].d)if((k=gcd(f2[i].n,f2[i].d))!=1) f2[i].n/=k,f2[i].d/=k;                     
               }
               for(int i=0;i<N;i++){
                       int k=0;
                     for(int j=0;j<N;j++){
                             if(a[i][j]=='.') continue;  
                             k++;
                             if(!f3[i].n&&!f3[i].d) f3[i].n=f2[j].n,f3[i].d=f2[j].d;
                             else{
                                  int l=0;
                                  if(f3[i].d&&f2[j].d)l=lcm(f3[i].d,f2[j].d);
                                  f3[i].n= (f2[j].n*(l/f2[j].d))+ (f3[i].n*(l/f3[i].d));
                                  f3[i].d= l;
                             }
                     }
                     f3[i].d *= k;
                     if(f3[i].n&&f3[i].d)if((k=gcd(f3[i].n,f3[i].d))!=1) f3[i].n/=k,f3[i].d/=k;
               }
               cout<<"Case #"<<oo<<":\n";
               out<<"Case #"<<oo++<<":\n";
               for(int i=0;i<N;i++){
                  //   D a,b,c;
//                     a.n = f[i].n;
//                     a.d = 4*f[i].d;
//                     b.n = f2[i].n;
//                     b.d = 2*f2[i].d;
//                     c.n = f3[i].n;
//                     c.d = 4*f3[i].d;
//                     
//                     double l = lcm(lcm(a.d,b.d),c.d);
//                     int nu = (a.n*(l/a.d))+(b.n*(l/b.d))+(c.n*(l/c.d));
                     //cout<<setprecision(12)<<nu/l<<'\n';
//                     out<<setprecision(12)<<nu/l<<'\n';

                     double a,b,c;
                     a = 0.25*f[i].n/f[i].d;
                     b = 0.5*f2[i].n/f2[i].d;
                     c = 0.25*f3[i].n/f3[i].d;
                     cout<<setprecision(12)<<a+b+c<<'\n';
                     out<<setprecision(12)<<a+b+c<<'\n';

               }
    }                     


    
    in.close();
    out.close();
    system("pause");
    return 0;
}
    
