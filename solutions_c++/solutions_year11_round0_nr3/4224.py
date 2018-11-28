#include<iostream>

using namespace std;

int main()
{
long T,n;
cin>>T;
for(int t=1;t<=T;t++)
{
          cin>>n;
          long sum=0,xsum=0,min=10000001,x;
          for(int i=0;i<n;i++)
          {
                  cin>>x;
                  if(i==0) min=x;
                  if(x<min) min=x;
                  
                  sum+=x;
                  xsum=xsum^x;
          }
          if(xsum!=0)
          {
                              cout<<"Case #"<<t<<": NO"<<endl;
          }
          else
          {
                              cout<<"Case #"<<t<<": "<<(sum-min)<<endl;
          }
          

}


return 0;
}
