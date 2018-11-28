#include <iostream>
#include <cstdlib>
#include <string>
#include <climits>

using namespace std;
int m[1001][1001];
int a[1001][1001];
int x,y,C=0;
int dx[4]={1,0,0,-1};
int dy[4]={0,1,-1,0};

int req(int i,int j)
{
    if(a[i][j]!=-1)return a[i][j];
    int least = m[i][j];
    int lx,ly;
    for(int k=0;k<4;k++){
       int a = i+dx[k];
       int b = j+dy[k];
       if(a<0||a>x-1||b<0||b>y-1)continue;
       if(m[a][b]<=least){
           if(m[a][b]==m[i][j])continue;
           least = m[a][b];
           lx = a;ly=b;
       }
    }
    if(least == m[i][j])a[i][j]=C++;
    else a[i][j] = req(lx,ly);
    return a[i][j];
}
void dp()
{
    for(int i=0;i<x;i++){
      for(int j=0;j<y;j++){
          if(a[i][j]==-1)req(i,j);
      }
    }
}
int main(int argc, char const* argv[])
{
    int t,l=1;
    cin>>t;
    while (t--) {
        cin>>x>>y;
        for (int i = 0; i < x; i++)
        for (int j = 0; j < y; j++)
          cin>>m[i][j];
        memset(a,-1,sizeof a);
        C=0;
        dp();
        cout<<"Case #"<<l<<":"<<endl;l++;
        for(int i=0;i<x;i++){
          for(int j=0;j<y;j++)
            cout<<(char(a[i][j]+'a'))<<" ";
          cout<<endl;
        }
    }
    return 0;
}
