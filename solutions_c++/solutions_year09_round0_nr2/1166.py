//WaterShed
#include<iostream>
#include<cstring>
using namespace std;
int arr[101][101],memo[101][101],m,n,count;
int ret(int i,int j)
{

 if(memo[i][j]==-1)
 { 
  int x=i,y=j,min=1000000,ix=i,iy=j;
 //North
  x=i-1;y=j;
  if(x>0 && arr[x][y]<arr[i][j] && arr[x][y]<min)
  { min=arr[x][y];ix=x;iy=y;}
//West
  x=i;y=j-1;
  if(y>0 && arr[x][y]<arr[i][j] && arr[x][y]<min)
  { min=arr[x][y];ix=x;iy=y;}
//East
  x=i;y=j+1;
  if(y<=n && arr[x][y]<arr[i][j] && arr[x][y]<min)
  { min=arr[x][y];ix=x;iy=y;}
//South
  x=i+1;y=j;
  if(x<=m &&  arr[x][y]<arr[i][j] && arr[x][y]<min)
  { min=arr[x][y];ix=x;iy=y;}
  if(min==1000000)
   memo[i][j]=count++;
  else 
   memo[i][j]=ret(ix,iy); 
 }

 return memo[i][j];
}
int main()
{
int t;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  cin>>m>>n;
   memset(arr,-1,sizeof(arr));
   memset(memo,-1,sizeof(memo));
  count=0;
   for(int p=1;p<=m;p++)
   for(int q=1;q<=n;q++)
   {
    cin>>arr[p][q]; 
   }
   cout<<"Case #"<<i<<":\n";
   for(int p=1;p<=m;p++)
   for(int q=1;q<=n;q++)
   {
    ret(p,q);
   cout<<char(memo[p][q]+'a')<<(q==n?"\n":" ");}
  
 }
 return 0;
}
