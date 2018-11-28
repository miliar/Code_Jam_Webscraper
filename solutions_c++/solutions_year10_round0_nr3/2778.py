#include<iostream>
using namespace std;

class tp
{
      public:
             int k;
             int r;
             int n;
             int euro;
             int g[1000];
             void getdata();
             void getval();             
};
void tp::getdata()
{
     cin>>r>>k>>n;
     for(int i=0;i<n;i++)
             cin>>g[i];
}
void tp::getval()
{
     euro=0;
     int count=0,j=0,l,sum;
     while(count<r)
     {
                   sum=0;
                   l=j;
                   while(1)
                   {
                           if(sum+g[j]<=k)
                           {
                                          sum+=g[j];
                                          j=(j+1)%n;
                                          if(j==l)
                                                  break;
                                                  
                           }
                           else
                               break;
                   }
                   count++;
                   euro+=sum;
     }
}
int main()
{
    int t;
    tp test[50];
    cin>>t;
    for(int i=0;i<t;i++)
        test[i].getdata();
    for(int i=0;i<t;i++)
    {
            test[i].getval();
            cout<<"Case #"<<i+1<<": "<<test[i].euro<<endl;
            }    
    
}
