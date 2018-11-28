#include<iostream.h>
//#include<conio.h>
using namespace std;
int main()
{
    long long T,i;
    cin>>T;
    for(i=0;i<T;i++)
    {
          long long N,K,j;
          cin>>N>>K;
          long long var=1,incr;  
          for(j=1;j<N;j++)
          {
                var=(var*2)+1;              
          } 
          //cout<<var;               
          incr=var+1;
          if((K-var)%incr==0)
               cout<<"Case #"<<i+1<<": ON"<<endl;
          else 
               cout<<"Case #"<<i+1<<": OFF"<<endl;
    }
    return 0;    
}
