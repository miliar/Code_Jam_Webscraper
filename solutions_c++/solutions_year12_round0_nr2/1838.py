#include<iostream>
using namespace std;


int main()
{
    int i,t,n,arr[101],s,p,k=1,tot,cnt1,cnt2,tmp,num;
    
    cin>>t;
    while(t--)
    {
              cin>>n>>s>>p;
              cnt1=cnt2=0;
              for(i=0;i<n;i++)
              cin>>arr[i];
              
              for(i=0;i<n;i++)
              {
                              if(arr[i]>=2 && arr[i]<=28)
                              {
                                           num = arr[i];
                                           tmp = (num+2)/3;
                                           
                                           if(tmp>=p)
                                           cnt1++;
                                           else if(num%3!=1)
                                           {
                                                if(tmp+1==p)
                                                cnt2++;
                                           }
                              }
                              else
                              {
                                  num = arr[i];
                                  tmp = (num+2)/3;
                                  
                                  if(tmp>=p)
                                  cnt1++;
                              }
              }
              
              if(cnt2>s)
              tot = cnt1+s;
              else
              tot = cnt1+cnt2;
              
              cout<<"Case #"<<k++<<": "<<tot<<'\n';
    }
    
    return(0);
}
