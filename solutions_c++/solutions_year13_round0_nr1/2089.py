#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
using namespace std;
 
/* 
int input()
{
int t=0;
char c;
c=getchar_unlocked();
while(c<'0' || c>'9')
c=getchar_unlocked();
while(c>='0' && c<='9')
{
t=t*10+c-'0';
c=getchar_unlocked();
}
return(t);
}
*/
 
int main(){
int t,i,j,draw,flag,k;
string s[4];
scanf("%d",&t);
for(i=1;i<=t;++i){
draw=1;
flag=0;
int crx[4]={0},cro[4]={0},crt[4]={0},ccx[4]={0},cco[4]={0},cct[4]={0};
for(j=0;j<4;++j){
cin>>s[j];
for(k=0;k<4;++k){
if(s[j][k]=='X')
crx[j]++;
else if(s[j][k]=='O')
cro[j]++;
else if(s[j][k]=='T')
crt[j]++;
else
draw=0;
}
}
scanf("\n");
for(j=0;j<4;++j){
for(k=0;k<4;++k){
if(s[k][j]=='X')
ccx[j]++;
else if(s[k][j]=='O')
cco[j]++;
else if(s[k][j]=='T')
cct[j]++;
}
}
for(j=0;j<4;++j){
if(crx[j]+crt[j]==4){
flag=1;
break;
}
else if(cro[j]+crt[j]==4){
flag=2;
break;
}
}
if(flag==0){
for(j=0;j<4;++j){
if(ccx[j]+cct[j]==4){
flag=1;
break;
}
else if(cco[j]+cct[j]==4){
flag=2;
break;
}
}
}
if(flag==0){
if((s[0][0]=='X' || s[0][0]=='T') && (s[1][1]=='X' || s[1][1]=='T') && (s[2][2]=='X' || s[2][2]=='T') && (s[3][3]=='X' || s[3][3]=='T'))
flag=1;
else if((s[0][0]=='O' || s[0][0]=='T') && (s[1][1]=='O' || s[1][1]=='T') && (s[2][2]=='O' || s[2][2]=='T') && (s[3][3]=='O' || s[3][3]=='T'))
flag=2;
}
if(flag==0){
if((s[0][3]=='X' || s[0][3]=='T') && (s[1][2]=='X' || s[1][2]=='T') && (s[2][1]=='X' || s[2][1]=='T') && (s[3][0]=='X' || s[3][0]=='T'))
flag=1;
else if((s[0][3]=='O' || s[0][3]=='T') && (s[1][2]=='O' || s[1][2]=='T') && (s[2][1]=='O' || s[2][1]=='T') && (s[3][0]=='O' || s[3][0]=='T'))
flag=2;
}
if(flag==1) 
printf("Case #%d: X won\n",i);
else if(flag==2)
printf("Case #%d: O won\n",i);
else if(draw)
printf("Case #%d: Draw\n",i);
else 
printf("Case #%d: Game has not completed\n",i);
}
return 0;
}