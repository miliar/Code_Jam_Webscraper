#include<iostream>
#include<string>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)

int ans[100][100];
int in[100][100];
bool edge[100][100][4];
bool visited[100][100];
int dy[]={-1,0,0,1};
int dx[]={0,-1,1,0};
int rev[]={3,2,1,0};

void dfs(int r,int c,int x,int y,int color){
  ans[y][x]=color;
  visited[y][x]=true;

  rep(i,4){
    if ( edge[y][x][i]==false)continue;
    int nex=x+dx[i],ney=y+dy[i];
    if ( visited[ney][nex]==true)continue;
    dfs(r,c,nex,ney,color);    
  }
}

void make_graph(int r,int c){
  rep(i,r)rep(j,c)rep(k,4)edge[i][j][k]=0;

  rep(i,r){
    rep(j,c){
      int index=-1,min_val=20000;
      rep(k,4){
	int nex=j+dx[k],ney=i+dy[k];
	if (nex<0||ney<0||nex>=c||ney>=r||in[ney][nex]>=in[i][j])continue;
	if ( min_val>in[ney][nex])index=k,min_val=in[ney][nex];
      }
      if ( index != -1)edge[i+dy[index]][j+dx[index]][rev[index]]=edge[i][j][index]=true;
    }
  }
    

}

void fill_out(int r,int c){
  char group[26];
  rep(i,26)group[i]=-1;
  int p=0;
  rep(i,r)
    rep(j,c)
    if ( group[ans[i][j]]==-1)group[ans[i][j]]=p++;
  
  
  
  rep(i,r){
    rep(j,c){
      if ( j != 0)cout << ' ';
      cout << (char)(group[ans[i][j]]+'a');
    }
    cout << endl;
  }
  
}


main(){
  int te,tc=1;
  cin>>te;
  while(te--){
    cout << "Case #"<<tc++<<":" << endl;
    int r,c;
    cin>>r>>c;
    rep(i,r)rep(j,c)cin>>in[i][j],visited[i][j]=false;

    make_graph(r,c);
    int p=0;
    rep(i,r){
      rep(j,c){
	if ( visited[i][j]==true)continue;
	dfs(r,c,j,i,p++);
      }
    }

    fill_out(r,c);

  }
}
