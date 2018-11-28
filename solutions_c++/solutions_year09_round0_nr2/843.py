#include<iostream>
#include<string>
#include<set>
#include<memory.h>
using namespace std;
int mat[100][100];
int used[100][100];
int ddd[100][100];
char res[100][100];
int h,w,ind;int dir[4][2]={-1,0,0,-1,0,1,1,0};
bool check(int i,int j)
{
    return i>=0&&i<h&&j>=0&&j<w;     
}
void dfs(int i,int j)
{
    used[i][j]=1;res[i][j]=char(ind+'a');
    for(int k=0;k<4;k++)
    {
        int ni=i+dir[k][0],nj=j+dir[k][1];
        if(check(ni,nj)&&!used[ni][nj]){
        int dd;
        if(k==0)dd=3;
        else if(k==3)dd=0;
        else if(k==1)dd=2;
        else if(k==2)dd=1;
        if(ddd[i][j]==k||ddd[ni][nj]==dd)
        dfs(ni,nj);      
        }          
    }     
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int t;scanf("%d",&t);for(int hh=1;hh<=t;hh++){
        int i,j;
        scanf("%d%d",&h,&w);
        for(i=0;i<h;i++)
        for(j=0;j<w;j++)
        scanf("%d",&mat[i][j]);
        memset(used,0,sizeof(used));
        ind=0;
        for(i=0;i<h;i++)
        for(j=0;j<w;j++)
        {
            int mark=-1,minn=0x7fffffff;
            for(int k=0;k<4;k++)
            {
                 int ni=i+dir[k][0],nj=j+dir[k][1];
                 if(check(ni,nj)&&mat[ni][nj]<mat[i][j]&&mat[ni][nj]<minn)
                 {
                     minn=mat[ni][nj];
                     mark=k;                                 
                 }       
            } 
            ddd[i][j]=mark;               
        }
        for(i=0;i<h;i++)
        for(j=0;j<w;j++)
        if(!used[i][j])
        {
           dfs(i,j);
           //printf("%d %d\n",i,j);
           ind++;
        } printf("Case #%d:\n",hh);
        for(i=0;i<h;i++){
        for(j=0;j<w;j++)
        {
            if(j)printf(" ");
            printf("%c",res[i][j]);  
        }
        printf("\n");                                    
        }    
    }
}
