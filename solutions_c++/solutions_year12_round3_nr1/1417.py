#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;
int n;
bool m;
vector<int> v[1001];
int c[1001][1001];
bool vis[1001];
int dfs(int i)
{
    
    if(vis[i]==false)
    {  vis[i]=true;
      for(int j=0;j<v[i].size();j++)
      {     
             // cout<<"r"<<i<<endl;
              int p=v[i][j];
              c[i][p]++;
              if(c[i][p]>=2)
              m=true;
              if(!vis[p])
              dfs(p);
              for(int k=1;k<=n;k++)
              { c[i][k]=c[i][k]+c[p][k];
                if(c[i][k]>=2)
                m=true;
              }
              
              
      }
    }
return 0;  
    
}
int main(){
int test,l=1;
cin>>test;
while(test--)
{
int k,m1;
cin>>n;
for(int i=0;i<=n;i++)
{        v[i].clear();
         vis[i]=false;
        for(int j=0;j<=n;j++)
        c[i][j]=0;
}
for(int i=1;i<=n;i++)
{       
        cin>>m1;
        for(int j=0;j<m1;j++)
        {
                cin>>k;
                v[k].push_back(i);
        }
} 
m=false;  
for(int i=1;i<=n;i++)
if(!vis[i])
dfs(i);

if(m)
printf("Case #%d: Yes\n",l++);
else
printf("Case #%d: No\n",l++);   

/*for(int i=1;i<=n;i++)
{
        for(int j=1;j<=n;j++)
        cout<<c[i][j]<<" ";
        cout<<endl;
} */


}
return 0;
}
