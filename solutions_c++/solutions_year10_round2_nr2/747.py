#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <conio.h>
//#include<>
using namespace std;

long long min(long long a, long long b)
{
  return a<b?a:b;  
    
};

bool collide (long long x1,long long x2,long long v1,long long v2,long long t,long long b)
{
 if (v1<=v2) return false;
 if (t*(v1-v2)<=x2-x1) return false;
 if (x1*(v1-v2)+v1*(x2-x1)+min(v1,v2)*(t*(v1-v2)-x2+x1)>=b*(v1-v2)) return false;
 return true;
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("B-large.in",ios::in);
    out.open("ap.out",ios::out);
    long long t,M,C,c,N,T,K,B,result,i,j,k,ind,left;
    long long X[100],V[100];
    in >> C;
    for (c=1;c<=C;c++)
    {
        in>>N>>K>>B>>T;
        for (i=0;i<N;i++) in>>X[i];
        for (i=0;i<N;i++) in>>V[i];
/*        for (i=0;i<N;i++) for (j=i+1;j<N;j++) if (X[i]>X[j])
        {
         t=X[i];
         X[i]=X[j];
         X[j]=t;
         t=V[i];
         V[i]=V[j];
         V[j]=t;
             
            
        };*/
        result=0;
        for (i=N-1;i>=0;i--)
        {
          if (X[i]+V[i]*T>=B)
          {
             for (j=i+1;j<N;j++) if (collide(X[i],X[j],V[i],V[j],T,B)) result++;
             K--;
          };
          if (K==0) break;
        };
        if (K==0)
        {
                 out<<"Case #"<<c<<": "<<result<<"\n";
        }
        else
        {
                 out<<"Case #"<<c<<": IMPOSSIBLE"<<"\n";            
        };
//        for (i=0;i<dirs.size();i++) out<< dirs[i]<<"\n";
    };

    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
