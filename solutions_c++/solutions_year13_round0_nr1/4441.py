#include<algorithm>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<vector>
#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<map>
#define fill(a,v) memset(a,v,sizeof(a))
#define sn(n) scanf("%d",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define MOD 1000000007
#define MAX 10001
using namespace std;
int main(){
 
int t,i,j,k,n,m,sum;
bool flag;
char c;
unsigned long long ans=0;
sn(t);
int grid[4][4];
int test=0;
while(t--)
{
test++;
ans=0;
flag=false;
REP(i,0,4)
{
REP(j,0,4)
{
scanf("%c",&c);
switch(c){
case 'X':  {grid[i][j]=1;break;}
case 'T':  {grid[i][j]=4;break;}
case '.':  {grid[i][j]=16;flag=true;break;}
case 'O':  {grid[i][j]=64;break;}
default: {j--;break;}
}
}
scanf("%c",&c);
}

ans=0;
REP(i,0,4)
{
sum=0;
REP(j,0,4)
{
sum+=grid[i][j];
}
switch(sum){
case 7:
case 4: {ans =1;break;}
case 196:
case 256: {ans =2;break;}
default : {break;}

}
if(ans!=0)
	break;

}
if(ans==0)
{

REP(j,0,4)
{
sum=0;
REP(i,0,4)
{
sum+=grid[i][j];
}
switch(sum){
case 7:
case 4: {ans =1;break;}
case 196:
case 256: {ans =2;break;}
default : {break;}

}
if(ans!=0)
	break;
}
}
sum=0;
if(ans==0)
{
sum=grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3];
}
switch(sum){
case 7:
case 4: {ans =1;break;}
case 196:
case 256: {ans =2;break;}
default : {break;}

}
sum=0;
if(ans==0)
{
sum=grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3];
}
switch(sum){
case 7:
case 4: {ans =1;break;}
case 196:
case 256: {ans =2;break;}
default : {break;}
}

switch(ans)
{
case 1: {printf("Case #%d: X won\n",test);break	;}
case 2: {printf("Case #%d: O won\n",test);break;}
default : {if(flag){printf("Case #%d: Game has not completed\n",test);}else printf("Case #%d: Draw\n",test);}
}

scanf("%c",&c);
}
 
 
}
