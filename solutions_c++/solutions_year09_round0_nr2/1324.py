#include<cstdio>
#include<iostream>
using namespace std;
char current;
char find(char ans[100][100],int grid[100][100],int i,int j,int h,int w);
int main()
{
int grid[100][100];
char ans[100][100];
int h,w;
int i,j;

int testcount,testcases;
cin>>testcases;
for(testcount=1;testcount<=testcases;testcount++)
{
cin>>h>>w;
for(i=0;i<h;i++)
for(j=0;j<w;j++)
{
cin>>grid[i][j];
ans[i][j]='Z';
}
current='a';

for(i=0;i<h;i++)
for(j=0;j<w;j++)
if(ans[i][j]=='Z')
{
ans[i][j]=find(ans,grid,i,j,h,w);
}

cout<<"Case #"<<testcount<<":"<<endl;

for(i=0;i<h;i++){
for(j=0;j<w;j++)
cout<<ans[i][j]<<" ";
cout<<endl;
}
}
return 0;
}








char find(char ans[100][100],int grid[100][100],int i,int j,int h,int w)
{
int side=0;//1=n,2=w,3=e,4=s
int value=grid[i][j];
if(i!=0 && grid[i-1][j]<value)
{side=1;value=grid[i-1][j];}
if(j!=0 && grid[i][j-1]<value)
{side=2;value=grid[i][j-1];}
if(j!=w-1 && grid[i][j+1]<value)
{side=3;value=grid[i][j+1];}
if(i!=h-1 && grid[i+1][j]<value)
{side=4;value=grid[i+1][j];}

if(side==0)
{
if(ans[i][j]=='Z')
{
ans[i][j]=current;
current++;
}
return ans[i][j];
}

if(side==1)
{
return find(ans,grid,i-1,j,h,w);
}

if(side==2)
{
return find(ans,grid,i,j-1,h,w);
}

if(side==3)
{
return find(ans,grid,i,j+1,h,w);
}

if(side==4)
{
return find(ans,grid,i+1,j,h,w);
}


}
