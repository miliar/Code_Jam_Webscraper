#include<iostream>
#include<cstring>
using namespace std;
int burnt[101][101],a[101][101],chr[101][101],min1[101][101];int m,n,l=0;int mina;
void min(int i,int j)
{

  mina=100000000; min1[i][j]=-1;
  if(a[i-1][j]<mina && i>0)
   {mina=a[i-1][j];min1[i][j]=1;}
  if(a[i][j-1]<mina && j>0)
   {mina=a[i][j-1];min1[i][j]=2;}
  if(a[i][j+1]<mina && j<n-1)
   {mina=a[i][j+1];min1[i][j]=3;}
  if(a[i+1][j]<mina && i<m-1)
   {mina=a[i+1][j];min1[i][j]=4;}
  if(mina>=a[i][j])min1[i][j]=0;
  
}
void dfs(int i,int j)
{

if(burnt[i][j]!=1)

{
  burnt[i][j]=1; 
if (min1[i][j]==0)
  {chr[i][j]=l;l++;}
else if(min1[i][j]==1)
   {dfs(i-1,j);chr[i][j]=chr[i-1][j];}
  else if(min1[i][j]==2)
   {dfs(i,j-1);chr[i][j]=chr[i][j-1];}
  else if(min1[i][j]==3)
   {dfs(i,j+1);chr[i][j]=chr[i][j+1];}
   else if(min1[i][j]==4)
   {dfs(i+1,j);chr[i][j]=chr[i+1][j];}
}
}
int main()
{
int t,count=0;
cin>>t;
while(t>-1)
{ 
  if(t==0)
   {return 0;}
  t--;
  count++;
  cout<<"Case #"<<count<<":\n";
  
  int i,j,k;
  cin>>m>>n;
  for(i=0;i<m;i++)
    for(j=0;j<n;j++)
      {cin>>a[i][j];burnt[i][j]=0;chr[i][j]=-1;}
     l=0;
   for(i=0;i<m;i++)
     for(j=0;j<n;j++)
        {min(i,j);}
    for(i=0;i<m;i++)
        for(j=0;j<n;j++)
          if(burnt[i][j]==0)
             {dfs(i,j);}
   char chr1[26];
    strcpy(chr1,"abcdefghijklmnopqrstuvwxyz\0");
   for(i=0;i<m;i++)
     {for(j=0;j<n;j++)cout<<chr1[chr[i][j]]<<" ";cout<<endl;}  
}

}
