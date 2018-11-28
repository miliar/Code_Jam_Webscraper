#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int u=0;u<tc;u++)
{
int r,c;
int flag=0;
cin>>r>>c;
char a[r][c];
for(int y=0;y<r;y++)
{
for(int z=0;z<c;z++)
{
cin>>a[y][z];
//cout<<a[r]<<endl;
if(a[r][c]=='#')
flag++;
}
}
if(flag%4!=0)
{
cout<<"Case #"<<u+1<<":"<<endl;
cout<<"Impossible"<<endl;
}
else
{
for(int y=0;y<r;y++)
{
for(int z=0;z<c;z++)
{
if(a[y][z]=='#')
{
if(y+1<r && z+1<c)
{
if(a[y][z+1]=='#' && a[y+1][z+1]=='#' && a[y+1][z]=='#')
{
char d='\\';
a[y][z]='/';
a[y][z+1]=d;
a[y+1][z]=d;
a[y+1][z+1]='/';
}
}
}
}
}
int bit=0;
for(int y=0;y<r;y++)
{
for(int z=0;z<c;z++)
{
if(a[y][z]=='#')
{
cout<<"Case #"<<u+1<<":"<<endl;
cout<<"Impossible"<<endl;
bit=1;
break;
}
}
if(bit==1)
break;
}
if(bit==0)
{
cout<<"Case #"<<u+1<<":"<<endl;
for(int y=0;y<r;y++)
{
for(int z=0;z<c;z++)
{
cout<<a[y][z];
}
cout<<endl;
}
}
}
}
return 0;
}
