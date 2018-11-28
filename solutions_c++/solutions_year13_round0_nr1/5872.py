/*
    shubham_1286
   algo =             */
using namespace std;
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<algorithm>
#include<list>
#include<deque>
#include<bitset>
#include<limits>
#include<sstream>
#define max(x,y) x>y?x:y
#define min(x,y) x<y?x:y
#define inf INT_MAX
#define low INT_MIN
#define mod 1000000007
int main()
{
int t,test=1;
cin>>t;
char ch[4][4];
while(test<=t)
{
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>ch[i][j];
int flag=10,row=0,rowo=0,col=0,colo=0,diagro=0,diagr=0,diagl=0,diaglo=0,point=0;
for(int i=0;i<4;i++)
{
for(int j=0;j<4;j++)
{flag=10;row=0;rowo=0;col=0;colo=0;diagro=0;diagr=0;diagl=0;diaglo=0;
if(ch[i][j]=='X'||ch[i][j]=='O'||ch[i][j]=='T')
{
//for row
for(int k=0;k<4;k++){
if(ch[i][k]=='X'||ch[i][k]=='T'||ch[i][k]=='O')
{
if(ch[i][k]=='X'||ch[i][k]=='T')
row++;
if(ch[i][k]=='T'||ch[i][k]=='O')
rowo++;
}}
if(row==4||rowo==4)
{
if(row==4)                   
flag=1;
else
flag=2;
break;
}
for(int l=0;l<4;l++){
if(ch[l][j]=='X'||ch[l][j]=='T'||ch[l][j]=='O')
{
if(ch[l][j]=='X'||ch[l][j]=='T')
col++;
if(ch[l][j]=='T'||ch[l][j]=='O')
colo++;
}}
if(col==4||colo==4)
{
if(col==4)                   
flag=3;
else
flag=4;
break;
}
//for diagnol
if((i==0&&j==0)||(i==3&&j==3)||(i==2&&j==2)||(i==1&&j==1))
{
int q=0,w=0;
for(int i=0;i<=3;i++)
{
if(ch[q][w]=='X'||ch[q][w]=='T')
diagr++;
if(ch[q][w]=='T'||ch[q][w]=='O')
diagro++;
q++;w++;
}
if(diagr==4||diagro==4)
{
if(diagr==4)                   
flag=5;
else
flag=6;
break;
}
}
else if((i==0&&j==3)||(i==3&&j==0)||(i==1&&j==2)||(i==2&&j==1))
{
int q=0,w=3;
for(int i=0;i<=3;i++)
{
if(ch[q][w]=='X'||ch[q][w]=='T')
diagl++;
if(ch[q][w]=='T'||ch[q][w]=='O')
diaglo++;
q++;w--;
}
if(diagl==4||diaglo==4)
{
if(diagl==4)                   
flag=7;
else
flag=8;
break;
}
}
}//end if
else
point++;
}
if(flag==1||flag==2||flag==3||flag==4||flag==5||flag==6||flag==7||flag==8)
break;
}
if(flag==1||flag==3||flag==5||flag==7)
printf("Case #%d: X won\n",test);
else if(flag==2||flag==4||flag==6||flag==8)
printf("Case #%d: O won\n",test);
else
{
if(point!=0)
printf("Case #%d: Game has not completed\n",test);
else
printf("Case #%d: Draw\n",test);
}
test++;
}
}
