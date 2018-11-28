#include<iostream>
#include<string>
#include<vector>
#include<set>
using namespace std;

int cas,n,m;
string s;
set<string> dat;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    
    for(int cnt=1;cnt<=cas;cnt++)
    {
         dat.clear();
         scanf("%d%d",&n,&m);
         
         for(int i=0;i<n;i++)
         {
             cin>>s;
             int l=s.length();
             string a="";
             for(int i=1;i<=l;i++)
             {
                 if(s[i]=='/'||i==l)
                 {
                     set<string>::iterator it;
                     it=dat.find(a);
                     if(it==dat.end())
                         dat.insert(a);
                     continue;
                 }
                 a.push_back(s[i]);
             }
         }
         int res=0;
         for(int i=0;i<m;i++)
         {
             cin>>s;
             int l=s.length();
             string a="";
             for(int i=1;i<=l;i++)
             {
                 if(s[i]=='/'||i==l)
                 {
                     set<string>::iterator it;
                     it=dat.find(a);
                     if(it==dat.end()) 
                     {
                         res++;
                         dat.insert(a);
                     }
                     continue;
                 }
                 a.push_back(s[i]);
             }
         }
      //   set<string>::iterator it;
      //   for(it=dat.begin();it!=dat.end();it++) 
      //       cout<<*it<<endl;
         printf("Case #%d: %d\n",cnt,res);
    }
    return 0;
} 
