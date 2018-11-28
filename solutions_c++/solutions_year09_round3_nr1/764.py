#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;
int main()
{
   freopen("d.in","r",stdin);
   freopen("d.out","w",stdout);
   char s[10000];
   int t,i,base=2,cc=1;
   scanf("%d",&t);
   while(t--)
   {
     scanf("%s",s);
     
     if(strlen(s)==1)
     {
      printf("Case #%d: 1\n",cc++);
      continue;                
     }
     map<char,int>M;
     M[s[0]]=1;
     for(i=1;i<strlen(s);i++)
     {
      if(M.find(s[i])==M.end())
      {
         M[s[i]]=0;
         //x[i]=0;
         break;                      
      }                        
     }
     int j=2;
     for(;i<strlen(s);i++)
     {
      if(M.find(s[i])==M.end())
      {
         M[s[i]]=j++;
         //x[i]=j++;
        // break;                      
      }                        
     }
     base=j;
     __int64 sum=0; 
     for(i=0;i<strlen(s);i++)
      sum=sum*base+M[s[i]];
    // printf("Case #%d: %64d\n",cc++,sum);
     cout<<"Case #"<<cc++<<": "<<sum<<endl;       
             
   }
   //system("pause");
   return 0;
}
