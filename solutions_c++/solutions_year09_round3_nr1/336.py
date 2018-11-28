#include<iostream>
#include<vector>
#include<cmath>
#include<fstream>

#define atob(i,n) for(int i=0;i<n;i++)

using namespace std;

int main()
{
    int t;
    cin>>t;
    string s;
    bool a[36];
    int eq[36];
    int coun;
    bool excc[36];
    long long result,mul;
    int base;
    for(int u=1;u<=t;u++)
    {
             cin>>s;
             cout<<"Case #"<<u<<": ";
             atob(i,36)
             {
                       a[i]=false;
                       eq[i]=-1;
                       excc[i]=false;
             }
             atob(i,s.length())
             {
                               if(s[i]>='a'&&s[i]<='z')
                               {
                                                       a[s[i]-97]=true;
                               }
                               else
                               {
                                   a[s[i]-'0'+26]=true;
                               }
             }
             base=0;
             atob(i,36)
             {
                       if(a[i]==true)
                         base++;
             }
             
             if(base==1)
               base++;
             coun=1;
             if(s.length()==1)
             {
                              cout<<"1"<<endl;
                              continue;
             }
             atob(i,s.length())
             {
                               if(s[i]>='a'&&s[i]<='z')
                               {
                                                       if(excc[s[i]-97])
                                                         continue;
                                                       eq[s[i]-97]=coun;
                                                       excc[s[i]-97]=true;
                               }
                               else
                               {
                                   if(excc[s[i]-'0'+26])
                                     continue;
                                   eq[s[i]-'0'+26]=coun;
                                   excc[s[i]-'0'+26]=true;
                               }
                               if(coun==1)
                               {
                                          coun=0;
                                          continue;
                               }
                               if(coun==0)
                               {
                                          coun=2;
                                          continue;
                               }
                               coun++;
             }
             result=0;
             mul=1;
             for(int i=s.length()-1;i>=0;i--)
             {
                     if(s[i]>='a'&&s[i]<='z')
                     {
                                             result+=(eq[s[i]-97]*mul);
                                             
                                       
                     }
                     else
                     {
                         result+=eq[s[i]-'0'+26]*mul;
                     }
                     mul*=base;
             }
             cout<<result<<endl;
    }
                                
    return 0;
}
