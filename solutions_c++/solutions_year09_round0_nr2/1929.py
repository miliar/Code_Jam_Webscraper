#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
struct state{int x,y;};
state con[102][102];
char b[102][102];
int a[102][102],h,w,let;
void cnc(int i,int j)
{
 int mini=99999;
 if(i-1>-1)
 {
 if(a[i-1][j]<mini&&a[i-1][j]<a[i][j])          
 {mini=a[i-1][j];con[i][j].x=i-1;con[i][j].y=j;}
 }    
 if(j-1>-1)
 {
 if(a[i][j-1]<mini&&a[i][j-1]<a[i][j])          
 {mini=a[i][j-1];con[i][j].x=i;con[i][j].y=j-1;}
 }
 if(j+1<w)
 {
 if(a[i][j+1]<mini&&a[i][j+1]<a[i][j])          
 {mini=a[i][j+1];con[i][j].x=i;con[i][j].y=j+1;}
 }    
 
 if(i+1<h)
 {
 if(a[i+1][j]<mini&&a[i+1][j]<a[i][j])          
 {mini=a[i+1][j];con[i][j].x=i+1;con[i][j].y=j;}
 }    
     
 if(mini==99999)
 {con[i][j].x=i;con[i][j].y=j;}    
return;
}
char getroot(int i,int j)
{
if(b[i][j]!='-')
{return b[i][j];}
if(con[i][j].x==i&&con[i][j].y==j)
{
let++;
char xx=let;
return b[i][j]=xx;
}
char yy=getroot(con[i][j].x,con[i][j].y);
if(yy!='-')
{return b[i][j]=yy;}
}
void col(char z,int i,int j)
{
if(con[i][j].x==i&&con[i][j].y==j)
{b[i][j]=z;return;}
b[i][j]=z;
col(z,con[i][j].x,con[i][j].y);
return;
}
int main()
{

freopen("ww.in","r",stdin);
freopen("ww.out","w",stdout);
int n;
cin>>n;
for(int k=0;k<n;k++)
{    
let=97;
memset(b,'-',sizeof(b));
cin>>h>>w;
for(int i=0;i<h;i++)
{
        for(int j=0;j<w;j++)
        {
        cin>>a[i][j];
        }    
}    
    
for(int i=0;i<h;i++)
{
for(int j=0;j<w;j++)
{
cnc(i,j);
}        
}
/*for(int i=0;i<h;i++)
{
for(int j=0;j<w;j++)
{
cout<<con[i][j].x<<","<<con[i][j].y<<" ";
}        
cout<<endl;
}*/

b[0][0]='a';
for(int i=0;i<h;i++)
{
for(int j=0;j<w;j++)
{
if(b[i][j]!='-')
{
col(b[i][j],con[i][j].x,con[i][j].y);
continue;
}
else
{b[i][j]=getroot(con[i][j].x,con[i][j].y);}
}        
}
cout<<"Case #"<<k+1<<":"<<endl;
for(int i=0;i<h;i++)
{
       for(int j=0;j<w-1;j++)
       {
       cout<<b[i][j]<<" ";
       }

cout<<b[i][w-1]<<endl;
}
}    
return 0;    
}
