#include<iostream>
using namespace std;

int T,N,M,X,Y;
int arr[105][105];
int vis[105][105];
int ans[105][105];

int sol(int x,int y)
{
 X=x;Y=y;
 
 int m=(1<<30);
 if(x)m=min(m,arr[x-1][y]);
 if(y)m=min(m,arr[x][y-1]);
 if(x<N-1)m=min(m,arr[x+1][y]);
 if(y<M-1)m=min(m,arr[x][y+1]);
 
 if(m>=arr[x][y])return 0;
 
 if(x)
 {if(m==arr[x-1][y])return sol(x-1,y);}
 if(y)
 {if(m==arr[x][y-1])return sol(x,y-1);}
 if(y<M-1)
 {if(m==arr[x][y+1])return sol(x,y+1);}
 if(x<N-1)
 {if(m==arr[x+1][y])return sol(x+1,y);}
}

char SS(int num)
{
 char AA[]="abcdefghijklmnopqrstuvwxyz";
 return AA[num];
    
}


int K;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    for(K=0;K<T;K++)
    {
      cin>>N>>M;
      int i,j;
      memset(vis,-1,sizeof vis);
      
      for(i=0;i<N;i++)
        for(j=0;j<M;j++)
        cin>>arr[i][j];
      int c=0;
      for(i=0;i<N;i++)
        for(j=0;j<M;j++) 
        {
                          X=i,Y=j;
                          sol(i,j);
                          if(vis[X][Y]==-1)vis[X][Y]=c,c=c+1;
                          ans[i][j]=vis[X][Y];
        }
     cout<<"Case #"<<K+1<<":"<<endl;
     
     for(i=0;i<N;i++)
     {
       for(j=0;j<M;j++)
       {
         if(j)cout<<" ";
         cout<<SS(ans[i][j]);                
                       
       }
       cout<<endl;
     }        
    }
    cin>>K;
    
 return 0;   
}
