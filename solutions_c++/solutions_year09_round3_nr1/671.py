#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;
int flag[36],num[62];
int main( )
{
  int T,tmp;
  string str;
  freopen("out.txt","w",stdout);
  cin>>T;
  for(int t=1;t<=T;t++)
  {
    cin>>str;
    memset(flag,0,sizeof(flag));
    int cnt=0;
    for(int i=0;str[i];i++)
    {
      if(str[i]>='a'&&str[i]<='z')
       {
           if(!flag[str[i]-'a'+10])
             {
                 cnt++;

                flag[str[i]-'a'+10] =cnt;

             }
       }
      else
      {
          if(!flag[str[i]-'0'])
          {
              cnt++;

              flag[str[i]-'0']=cnt;
          }
      }
    }
    if(cnt==1)
     {
         for(int i=0;str[i];i++)
     num[i]=1;
     cnt=2;
     }
     else
     {
    for(int i=0;str[i];i++)
    {
      if(str[i]>='a'&&str[i]<='z')
        {

         num[i]=flag[str[i]-'a'+10]-1;
         if(!num[i])
        num[i]=1;
         else if(num[i]==1)
         {
             num[i]=0;
         }
        }
      else
       {

           num[i]=flag[str[i]-'0']-1;
            if(!num[i])
        num[i]=1;
         else if(num[i]==1)
         {
             num[i]=0;
         }
       }
    }
     }
    //cout<<cnt<<endl;
   // for(int i=0;i<str.size( );i++)
   // printf("%d ",num[i]);
    int sum=0;
      for(int i=0;i<str.size( );i++)
      {
          sum=sum*cnt+num[i];

      }

    cout<<"Case #"<<t<<": "<<sum<<endl;
  }
   return 0;
}
