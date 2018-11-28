#include<iostream>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<deque>
#include<stack>
#include<algorithm>
#include<queue>
#include<map>
#include<cstdio>
using namespace std;
int main()
{int t,a[110];
int n,cs=0;
cin>>t;
char c[110];
while(t--)
{cs++;
          int ps1=1,ps2=1,cnt=0,cal;
          cin>>n;
    for(int i=0;i<n;i++)
    {
    cin>>c[i]>>a[i];
    }
            
    for(int i=0;i<n;i++)
    {
            if(c[i]=='O')
            {
               cal=a[i]-ps1;
               ps1=a[i];
               cal=(abs(cal)+1);
               cnt+=cal;
               for(int j=i;j<n;j++)
               {
                       if(c[j]=='B')
                       {
                           if(cal>abs(ps2-a[j]))
                           ps2=a[j];
                           
                           else
                           {
                               if(ps2<a[j])
                               ps2=ps2+cal;
                               else
                               ps2=ps2-cal;
                               }  
                               break;    
                       }
                       
               } 
               }
               else
               {cal=a[i]-ps2;
               ps2=a[i];
               cal=(abs(cal)+1);
               cnt+=cal;
               for(int j=i;j<n;j++)
               {
                       if(c[j]=='O')
                       {
                           if(cal>abs(ps1-a[j]))
                             ps1=a[j];
                           else
                           {
                               if(ps1<a[j])
                               ps1=ps1+cal;
                               else
                               ps1=ps1-cal;
                               }  
                               break;    
                       }
                   
                   }                
            }
    }
    cout<<"Case #"<<cs<<": "<<cnt<<endl;
    
          
          }



return 0;
}
