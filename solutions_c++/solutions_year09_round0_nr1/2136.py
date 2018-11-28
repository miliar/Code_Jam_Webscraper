#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<queue>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
   int l,n,d;
   scanf("%d %d %d",&l,&d,&n);
   char words[5050][20];
   for(int i=0;i<d;i++)scanf("%s",words[i]);
   
   //for(int i=0;i<d;i++)printf("%s\n",words[i].c_str());
   int test=1;
   for(;n--;test++)
   {
      bool f[20][29];
      memset(f,false,sizeof(f));
      char input[1000];
      scanf("%s",input);
      for(int i=0,j=0;input[i];)
      {
         if(input[i]!='(')
         {
            f[j][input[i]-'a']=true;
            j++;i++;
         }
         else
         {
            i++;
            for(;input[i]!=')' && input[i];i++)
            {
               f[j][input[i]-'a']=true;
            }
            j++;i++;
         }
      }
      int ans=0;
      for(int i=0;i<d;i++)
      {
         int flag=0;
         for(int j=0;j<l;j++)
            if(f[j][words[i][j]-'a']==false){flag=1;break;}
         
         if(!flag)ans++; 
      }
      printf("Case #%d: %d\n",test,ans);
   }
   return 0;
}         
                  
         
      
