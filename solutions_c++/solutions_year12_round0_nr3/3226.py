#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int T,A,B,d=1;
    cin>>T;
    while(T--)
    {
              cin>>A>>B;
              int count=0;
              for(int i=A;i<B;i++)
              {
                      int j=i;
                      int I=i;
                      int c=0;
                      while(j>0)
                      {
                                j/=10;
                                c++;
                      }
                      int p=10,a=1,q=10;
                      for(j=0;j<c-1;j++)
                      {
                              int m=I%p;
                              m=m*(int)pow((float)10,(float)c-a);
                              int n=(I/q)+m;
                              if(n>I && n<=B && n>A)
                              {
                                     count++;
                              }
                              p*=10;
                              q*=10;
                              a++;
                      }
              }
              cout<<"Case #"<<d<<": ";
              cout<<count<<endl;
              d++;
    }
    return 0;
}
