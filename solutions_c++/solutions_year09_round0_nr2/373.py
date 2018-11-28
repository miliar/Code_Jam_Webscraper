#include<iostream>
#include<vector>

using namespace std;
int label[10000];
int M,N,A[100][100];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int dp[100][100];

int findbasin(int X,int Y)
{
    if(dp[X][Y]!=-1) return dp[X][Y];
    int minval=A[X][Y];
    int Xpos=-1;
    int Ypos=-1;
    for(int i=0;i<4;i++)
    {
            if(X+dx[i]<M && X+dx[i]>=0 && Y+dy[i]<N && Y+dy[i]>=0 && A[X+dx[i]][Y+dy[i]]<minval)
            {
                         minval=A[X+dx[i]][Y+dy[i]];
                         Xpos=X+dx[i];
                         Ypos=Y+dy[i];
            }
    }
    if(Xpos==-1)
              return dp[X][Y]=X*N+Y;
    else return dp[X][Y]=findbasin(Xpos,Ypos);
}        
    
    
    
int main()
{
    freopen("Q2.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    cin>>T;
    int K=T;

    while(T--)
    {

              int val=0;
              memset(dp,-1,sizeof(dp));
              memset(label,-1,sizeof(label));
              cin>>M>>N;
              
              
              for(int i=0;i<M;i++)
                 for(int j=0;j<N;j++) cin>>A[i][j];
              for(int i=0;i<M;i++)
              {
                      for(int j=0;j<N;j++)
                      {
                              int F=findbasin(i,j);
                              if(label[F]==-1)
                                     label[F]=val++;
                      }
              }             
              cout<<"Case #"<<K-T<<":\n";        
              for(int i=0;i<M;i++)
              {
                       for(int j=0;j<N;j++)
                          cout<<(char)(label[dp[i][j]]+'a')<<" ";
                       cout<<"\n";
              }
}
}
              
