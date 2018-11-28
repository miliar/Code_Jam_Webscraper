#include<iostream>
#include<string.h>
using namespace std;

int main()
{
    int t,n=0;
    cin>>t;
    cin.ignore();
    while(t--)
    {
      int len;
      char arr[110];
      int ans[26];
      n++;
      gets(arr);
      len=strlen(arr);
      /*for(int i=97;i<=122;i++)
      cout<<char(i)<<i<<" ";
      cout<<"\n";*/
      ans[0]=24;ans[1]=6;ans[2]=2;ans[3]=15;ans[4]=10;ans[5]=-3;
      ans[6]=15;ans[7]=16;ans[8]=-5;ans[9]=11;ans[10]=-2;
      ans[11]=-5;ans[12]=-1;ans[13]=-12;ans[14]=-4;ans[15]=2;
      ans[16]=9;ans[17]=2;ans[18]=-5;ans[19]=3;ans[20]=-11;
      ans[21]=-6;ans[22]=-17;ans[23]=-11;ans[24]=-24;ans[25]=-9;
      for(int i=0;i<len;i++)
      {
          if(arr[i]!=' ')
          {
             arr[i]+=ans[arr[i]-97];
          }
             
      }
      printf("Case #%d: %s\n",n,arr);
    }
}
