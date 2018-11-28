#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include<cstdlib>
#include<cstring>
#include<string>


using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((long long)(v).size())
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}


typedef vector<long long> vi;
typedef vector< vector<long long> > vvi;
typedef vector<string> vs;
typedef long long  ll;

int main()
{

   long long t,test=0;
   scanf("%Ld",&t);
   while(t--)
   {
      char st[100];
      scanf("%s",st);
      string s=st;
      long long len=(long long)s.size();
      long long c[100];for(int i=0;i<100;i++)c[i]=0; //c.clear();
      
      bool seen[100];
      for(int i=0;i<100;i++)seen[i]=false;                 //(len,false); //seen.clear();
      
      for(long long i=0;i<len;i++)
      {
         if(s[i]>='a' && s[i]<='z')c[i]=s[i]-'a';
         else c[i]=s[i]-'0'+26;
      }   
      long long ans[100];for(int i=0;i<100;i++)ans[i]=-1;
      long long a=0; //ans.clear();
      
      for(long long i=0;i<len;i++)
      {
         if(!seen[c[i]])
         {
            seen[c[i]]=true;
            ans[i]=a++;
         }
         
      }
      for(long long i=0;i<len;i++)
      {
         if(ans[i]!=-1)continue;
         else
         {
            for(long long j=0;j<i;j++)
            {
               if(c[i]==c[j]){ans[i]=ans[j];break;}
            }
         }
      }
      for(long long i=0;i<len;i++){if(ans[i]==0)ans[i]=1; else if(ans[i]==1)ans[i]=0;}
      
      long long m=0;
      for(long long i=0;i<len;i++)if(ans[i]>m)m=ans[i];
      
      long long base=m+1;
      if(base==1)base++;
      long long f=0;
      for(long long i=0;i<len;i++)
      {
         f=f*base + ans[i];
      }
      cout << "Case #" << ((test)+1) << ": " << (f) <<endl;
      test++;
      //for(int i=0;i<len;i++)if(s[i]==' ')cout<<" "<<"stupid"<<endl;
      //if(test==46)break;
   }      
         
               
              
            
         
   
   
      
      
   return 0;
}   
