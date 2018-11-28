#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
#include<queue>
#include<cstring>
using namespace std;
int main()
{
   int t,test=1;
   scanf("%d",&t);
   for(;t--;test++)
   {
      int r,c;
      scanf("%d %d",&r,&c);
      int a[105][105];
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
         scanf("%d",&a[i][j]);
      
      int dx[]={-1, 0,0,1};
      int dy[]={ 0,-1,1,0};
      int next[105][105];
      
      memset(next,-1,sizeof(next));
      
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
      {
         int low=10005,ind=-1,flag=0;
         for(int k=0;k<4;k++)
         {
               int x=i+dx[k],y=j+dy[k];
               if(x<0 || y<0 || x>=r || y>=c)continue;
               if(a[x][y]<a[i][j] && a[x][y]<low){ind=k;low=a[x][y];flag=1;}
         }
         if(flag)
         {
            next[i][j]=ind;
         }
      }
      
      char name='a',ans[105][105],map[28];
      bool seen[105][105];
      memset(seen,false,sizeof(seen));
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
      {
         if(next[i][j]>-1 || seen[i][j])continue;
         seen[i][j]=true;
         queue<int> q;
         q.push(i);q.push(j);
         while(!q.empty())
         {
            int i1=q.front();q.pop();
            int j1=q.front();q.pop();
            ans[i1][j1]=name;
            for(int k=0;k<4;k++)
            {
               int x=i1+dx[k],y=j1+dy[k];
               if(x<0 || y<0 || x>=r || y>=c || next[x][y]==-1)continue;
               if(x+dx[next[x][y]]==i1 && y+dy[next[x][y]]==j1 && !seen[x][y])
               {
                  q.push(x);q.push(y);
                  seen[x][y]=true;
                  ans[x][y]=name;
               }  
            }
         }
         name++;
       }
       
      bool seen1[28];
      char ch='a';
      memset(seen1,false,sizeof(seen1));
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
      {
         if(!seen1[ans[i][j]-'a']){seen1[ans[i][j]-'a']=true;map[ans[i][j]-'a']=ch++;}
      }
      for(int i=0;i<r;i++)
      for(int j=0;j<c;j++)
      {
         ans[i][j]=map[ans[i][j]-'a'];
      }
      
      printf("Case #%d:\n",test);
      for(int i=0;i<r;i++){
      for(int j=0;j<c-1;j++)
         printf("%c ",ans[i][j]);
      printf("%c\n",ans[i][c-1]);
      }
      }
      return 0;
}            
                  
            
         
                  
               
         
      
      
   
