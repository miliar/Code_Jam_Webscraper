#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <cstdlib>
#include<conio.h>
#include<fstream>
 


#define FOR(i,st,en) for(int i=st;i<=en;i++)
#define sqr(a) a*a
using namespace std;

int main()
{
    FILE *_i,*_o;
    _i=fopen("tst.in","r");
    _o=fopen("tst.out","w+");
   // ofstream out("A-large.out");
    int N;
    fscanf(_i,"%d",&N);
    
    FOR(k,1,N)
    {fprintf(_o,"Case #%d: ",k);
     int n,a,b,c,d,X,Y,m;
     vector<int> x,y;
    //body
    fscanf(_i,"%d %d %d %d %d %d %d %d",&n,&a,&b,&c,&d,&X,&Y,&m);
    cout<<n<<" "<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<X<<" "<<Y<<" "<<m<<" "<<endl;
    x.push_back(X);
     y.push_back(Y);  
    for(int i=1;i<=n-1;i++)
    {x.push_back((a*x[i-1]+b)%m);
     y.push_back((c*y[i-1]+d)%m);       
     
    }
    int cnt=0;
    for(int i=0;i<n;i++)
     for(int j=0;j<n;j++)
        for(int l=0;l<n;l++)
          {int gx,gy;
           gx=(x[i]+x[j]+x[l])%3;
           gy=(y[i]+y[j]+y[l])%3; 
           if(gx==0 && gy==0)
           cnt++;    
          }
          
     fprintf(_o,"%d",cnt);
    
    
    
    fprintf(_o,"\n");
    //out<<endl;
    
      
    }
    cout<<"done";
    fclose(_i);
    fclose(_o);
    //out.close();
getche();
return 0;
}
