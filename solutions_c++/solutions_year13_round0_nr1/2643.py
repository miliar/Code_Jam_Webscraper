#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
using namespace std;
typedef long long int int64;
int fn(string s[],char c)
{
int64 i,j,cn;
for(i=0;i<4;i++){
cn=0;for(j=0;j<4;j++)if(s[i][j]==c||s[i][j]=='T')cn++;if(cn==4)return 1;}
for(j=0;j<4;j++){
cn=0;for(i=0;i<4;i++)if(s[i][j]==c||s[i][j]=='T')cn++;if(cn==4)return 1;}
cn=0;for(i=0,j=0;i<4;i++,j++)if(s[i][j]==c||s[i][j]=='T')cn++;if(cn==4)return 1;
cn=0;for(i=0,j=3;i<4;i++,j--)if(s[i][j]==c||s[i][j]=='T')cn++;if(cn==4)return 1;
return 0;
}
int chk(string s[])
{
int64 i,j,cn=0;
for(i=0;i<4;i++)for(j=0;j<4;j++)if(s[i][j]=='.')cn++;
if(cn==0)return 1;
else return 0; 
}
int main()
{
//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
int64 i,j,n,k,m,t,cnt=1;
cin>>t;
string s[4],str;
while(t--)
{
for(i=0;i<4;i++)cin>>s[i];getline(cin,str);
if(fn(s,'X')==1)printf("Case #%lld: X won\n",cnt);
else if(fn(s,'O')==1)printf("Case #%lld: O won\n",cnt);
else if(chk(s)==1)printf("Case #%lld: Draw\n",cnt);
else printf("Case #%lld: Game has not completed\n",cnt);
cnt++;
}
//system("pause");
return 0;
}
