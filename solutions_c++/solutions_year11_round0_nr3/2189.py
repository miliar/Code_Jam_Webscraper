#include<iostream>
#include<list>
using namespace std;
int main()
{
    int t1,n,sum=0,a[1002],sum1=0,flag=0,s,q,z=1;
    list<int> t;
    cin>>t1;
    while(t1)
    {
            sum=0;
            sum1=0;
            cin>>n;
            t.clear();
            for(int i=0;i<n;i++)
            {
                    cin>>a[i];
                    t.push_back(a[i]);
                    sum1=sum1+a[i];
            }
            t.sort();
            s=t.front();
         //   cout<<s;
            for(int i=0;i<n;i++)
            {
                    q=t.front();
                    t.pop_front();
                   // cout<<" "<<t.front();
                    sum=sum^q;
            }
            if(sum==0)
            {
                      flag=1;
                      sum=sum1-s;
            }
            else
            flag=0;
                    
            if(flag==1)
            cout<<"Case #"<<z<<": "<<sum<<endl;
            else
            cout<<"Case #"<<z<<": "<<"NO"<<endl;
            t1--;
            z++;
            }
            return 0;
    }
    
