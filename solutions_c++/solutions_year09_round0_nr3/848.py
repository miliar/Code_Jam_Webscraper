#include<iostream>
#include<string>
#define M 10000
using namespace std;
string a="welcome to code jam",inp;
int ans[20][501];
void dp()
{
 int i,j;
 memset(&ans,0,sizeof(ans));
for(i=1;i<=inp.size();i++)
{
 if(inp[i-1]==a[0])
 ans[1][i]=ans[1][i-1]+1;
 else
 ans[1][i]=ans[1][i-1];
 ans[1][i]=ans[1][i]%M;
}
//cout<<ans[1][7]<<endl;
 for(i=2;i<=a.size();i++)
 {
  for(j=1;j<=inp.size();j++)
  {
   if(inp[j-1]==a[i-1])
   {
    ans[i][j]=ans[i][j-1]+ans[i-1][j-1];
   }
   else
   ans[i][j]=ans[i][j-1];
   ans[i][j]=ans[i][j]%M;
  }
 }
}
main()
{
      
      int test,cas=1;
      cin>>test;
//      fflush(stdin);
char ch;
scanf("%c",&ch);
      while(test--)
      {
       getline(cin,inp);
       int x=a.size(),y=inp.size();
       dp();
       int fin=ans[x][y];
       cout<<"Case #"<<cas<<": ";
       if((fin/1000)==0)
       cout<<"0";
       if((fin/100)==0)
       cout<<"0";
       if((fin/10)==0)
       cout<<"0";
       cout<<fin<<endl;;
       
       cas++;
      }
//       cin>>ans[0][0];
}
