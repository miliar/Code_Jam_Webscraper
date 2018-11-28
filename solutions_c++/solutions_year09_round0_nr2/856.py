#include<iostream>
#include<vector>
using namespace std;
vector<vector<int> > a;
int b[502][502],flag[502][502],maps[26],ans[502][502];
bool myfunc(vector<int> x,vector<int> y)
{
 if(x[0]>y[0])
 return true;
 if(x[0]==y[0] && x[1]<y[1])
 return true;
 if(x[0]==y[0] && x[1]==y[1] && x[2]<y[2])
 return true;
 return false;
}
int dfs(int x,int y,int val)
{
 int sm=val,nx,ny;
 if(flag[x][y]>=0)
 return flag[x][y];
 if(b[x-1][y]<sm && b[x-1][y]!=-1)
 {
  sm=b[x-1][y];
  nx=x-1;
  ny=y;
 }
 if(b[x][y-1]<sm && b[x][y-1]!=-1)
 {
  sm=b[x][y-1];
  nx=x;
  ny=y-1;
 }
 if(b[x][y+1]<sm && b[x][y+1]!=-1)
 {
  sm=b[x][y+1];
  nx=x;
  ny=y+1;
 }
 if(b[x+1][y]<sm && b[x+1][y]!=-1)
 {
  sm=b[x+1][y];
  nx=x+1;
  ny=y;
 }
 
// cout<<sm<<" "<<nx<<" "<<ny<<endl;
 if(sm==val)
 return flag[x][y];
 return dfs(nx,ny,sm);
}


void dfs2(int x,int y,int val,int p)
{
 int sm=val,nx,ny;
 
// cout<<x<<" "<<y<<" "<<p<<endl;
 if(flag[x][y]>=0)
 return;
 flag[x][y]=p;
 if(b[x-1][y]<sm && b[x-1][y]!=-1)
 {
  sm=b[x-1][y];
  nx=x-1;
  ny=y;
 }
 if(b[x][y-1]<sm && b[x][y-1]!=-1)
 {
  sm=b[x][y-1];
  nx=x;
  ny=y-1;
 }
 if(b[x][y+1]<sm && b[x][y+1]!=-1)
 {
  sm=b[x][y+1];
  nx=x;
  ny=y+1;
 }
 if(b[x+1][y]<sm && b[x+1][y]!=-1)
 {
  sm=b[x+1][y];
  nx=x+1;
  ny=y;
 }
 
 if(sm==val)
 return;
 dfs2(nx,ny,sm,p);
}
 
main()
{
 int test,i,j,cas=1;
 scanf("%d",&test);
 
 while(test--)
 {
  a.clear();
  memset(&b,-1,sizeof(b));
  
  vector<int> emp(3);
  int h,w;
  scanf("%d %d",&h,&w);
  for(i=1;i<=h;i++)
  {
   for(j=1;j<=w;j++)
   {
    scanf("%d",&b[i][j]);
    emp[0]=b[i][j];
    emp[1]=i;
    emp[2]=j;
    a.push_back(emp);
   }
  }
  sort(a.begin(),a.end(),myfunc);
  memset(&flag,-1,sizeof(flag));
  int nexval=0;
  for(i=0;i<a.size();i++)
  {
   int val=a[i][0],x=a[i][1],y=a[i][2];
   if(flag[x][y]==-1)
   {
   // cout<<"Now: "<<x<<" "<<y<<" "<<b[x][y]<<" "<<val<<endl;
  
    int find=dfs(x,y,val);
   // cout<<find<<endl;
    if(find>=0)
    dfs2(x,y,val,find);
    else
    {
     dfs2(x,y,val,nexval);
     nexval++;
    }
   }
  }
  memset(&maps,-1,sizeof(maps));
  int nex=0;
  for(i=1;i<=h;i++)
  {
   for(j=1;j<=w;j++)
   {
    if(maps[flag[i][j]]==-1)
    {
     maps[flag[i][j]]=nex;
     nex++;
    }
    ans[i][j]=maps[flag[i][j]];
   }
  }
  cout<<"Case #"<<cas<<":"<<endl;
  for(i=1;i<=h;i++)
  {
   for(j=1;j<=w;j++)
   printf("%c ",char(ans[i][j]+'a'));
   printf("\n");
  }
  cas++;           
 }
}
    
   
