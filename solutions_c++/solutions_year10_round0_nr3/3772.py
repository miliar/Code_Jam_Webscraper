//C++
#include<iostream>
#include<math.h>
using namespace std;

  int main()
{
    int Dan[100000];  
    int R,k,n,i,j;
    int zz,z1,z3;
    int t;      
    int g[100008];
    int z;
    cin>>t;
    for(i=0;i<t;++i)
        {z3=0;
        z1=0;
         j=0;   
           cin>>R>>k>>n;    
                 for(zz=0;zz<n;++zz)
                 {cin>>g[zz];                           }
                 zz=0;
                 for(z3=0;z3<R;++z3)     
                 {z1=0;                                    
                 z1=0; 
                    z=j;
                  while((z1<k+1 && j!=z) || (z1<k+1 && z1==0)){                                        
                  z1=z1+g[j];
                  if(z1<k+1)
                  {
                  zz=zz+g[j];                  
                  if(j<n-1)
                  ++j;
                  else if(j==n-1)
                  j=0;}                     }                           }
                  Dan[i]=zz;}
                  for(z1=0;z1<t;++z1)
                  cout<<"Case #"<<z1+1<<": "<<Dan[z1]<<"\n";
                  
    system("pause");
    return 0;
}
