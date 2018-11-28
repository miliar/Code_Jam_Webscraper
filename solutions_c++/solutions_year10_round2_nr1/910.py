#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<functional>
using namespace std;
const int INF=(1<<31)-1;
const double EPS=1e-8;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,steven=1,j,i,k,N,M;
    char str[110];
    char str1[110];
    for(scanf("%d",&T);steven<=T;steven++)
    {
                                           
       set<string> v;
       set<string>::iterator it;
       scanf("%d%d",&N,&M);
       for(i=0;i<N;i++)
       {
         scanf("%s",str);
         int len=strlen(str);
         for(j=0;j<len;j++)
         {
            if(str[j]=='/')
            {
               j++;
               k=0;
               while(str[j]!='/'&&j<len){k++;j++;} 
               memset(str1,0,sizeof(str1));
               memcpy(str1,str,j);
               string temp(str1);
               if(v.find(temp)==v.end())
                  v.insert(temp);
               j--;         
            }                  
         }                
       } 
       /*for(it=v.begin();it!=v.end();it++)
       {
          cout<<(*it)<<" ";                       
       }
       cout<<endl;*/
       int sum=0;
       for(i=0;i<M;i++)
       {
         scanf("%s",str);
         int len=strlen(str);
         for(j=0;j<len;j++)
         {
            if(str[j]=='/')
            {
               j++;
               k=0;
               while(str[j]!='/'&&j<len){k++;j++;} 
               memset(str1,0,sizeof(str1));
               memcpy(str1,str,j);
               string temp(str1);
               if(v.find(temp)==v.end())
               {
                  sum++;
                  v.insert(temp);
               }
               j--;         
            }                  
         }                
       } 
       
       
       printf("Case #%d: %d\n",steven,sum);                                   
    }
    //system("pause");
    return 0;
}
