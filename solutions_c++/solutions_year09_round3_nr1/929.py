#include<iostream>
#include<string>
#include<algorithm>
#include<stddef.h>
#include<math.h>

using namespace std;
long long powe(int base,long long x);
int main()
{
    freopen("prb1.txt","r",stdin);
    freopen("ans1.txt","w",stdout);
    
    int caseid=1,no;
    cin>>no;
    
    for(caseid=1;caseid<=no;caseid++)
    {
               char chk=2;
               int arr[500],i=0,base=0,s[500];
               memset(arr,-1,500);
               long long ans=0;
               string st;
               cin>>st;
                int len=st.length();
               for(i=0;i<len;i++)
               s[i]=st[i]-'0';
               
               for(i=0;i<st.length();i++)
               {
                                        arr[s[i]]=1;
               }
               
               for(i=0;i<=128;i++)
               {
                                  if(arr[i]==1)
                                  base++;
               }
               memset(arr,-1,500);
              
               
               if(len==1)
               {
                                s[0]=1;
               }
               if(len>=2)
               {
                               arr[s[0]]=1;
                               s[0]=1;
                               
                               if(arr[s[1]]==-1)
                               {
                                                arr[s[1]]=0;
                               s[1]=0;
                               
                               }
                               else
                               {
                                   s[1]=(int)arr[s[1]];
                                   chk=0;
                               }
               }
               
               for(i=2;i<len;i++)
               {
                                           if(arr[s[i]]==-1)
                                           {
                                                           arr[s[i]]=chk++;
                                                           s[i]=arr[s[i]];
                                                           if(chk==1)
                                                           chk++;
                                           }
                                           else
                                           {
                                               s[i]=(int)arr[s[i]];
                                           }
               }
               if(base==1)
               base=2;
               
               for(i=len-1;i>=0;i--)
               {
                                     long long temp=powe(base,len-i-1);
                                          ans=ans+(s[i])*temp;
               }
               
               
               
               
               
                
                
            
            cout<<"Case #"<<caseid<<": "<<ans<<endl;                           
    }
}

long long powe(int base,long long x)
{
     long long ans=1;
     for(int i=1;i<=x;i++)
     {
             ans=ans*base;
     }
     return ans;
}
