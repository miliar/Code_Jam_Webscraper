#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
const int dy[]={1,0,0,-1};
const int dx[]={0,1,-1,0};
int W,H,field[100][100],ans[100][100],cnt;

int fill(int x,int y){
  int dmin=101*101,next_x,next_y;
  for(int k=0;k<4;k++){
    int tx=x+dx[k];
    int ty=y+dy[k];
    if(tx<0 || tx>=W || ty<0 || ty>=H)continue;
    if(field[y][x]>field[ty][tx] && dmin>=field[ty][tx]){
      dmin=field[ty][tx]; next_x=tx; next_y=ty;
    }
  }
  if(dmin!=101*101){
    if(ans[next_y][next_x]==0){
      ans[next_y][next_x]=fill(next_x,next_y);
    }
    return ans[next_y][next_x];
  }
  else{
    cnt++;
    return cnt;
  }
}

int main(void){
  int T;
  vector<int> vx,vy;
  
  cin>>T;
  for(int x=1;x<=T;x++){
    cnt=0;
    memset(ans,0,sizeof(ans));
    memset(field,0,sizeof(field));
    printf("Case #%d:\n",x);

    int dmax=-1;
    cin>>H>>W;
    for(int i=0;i<H;i++)for(int j=0;j<W;j++){
      cin>>field[i][j];
      if(dmax<=field[i][j]){
        if(dmax==field[i][j]){ vx.push_back(j); vy.push_back(i); }
        else{
          vx.clear(); vy.clear();
          vx.push_back(j); vy.push_back(i);
        }
        dmax=field[i][j];
      }
    }

    for(;;){
      for(int p=0;p<vx.size();p++){
        ans[vy.at(p)][vx.at(p)] = fill(vx.at(p),vy.at(p));
      }
      
      vx.clear(); vy.clear();
      int d2max=-1;
      
      for(int i=0;i<H;i++)for(int j=0;j<W;j++){
        if(dmax>field[i][j] && d2max<=field[i][j] && ans[i][j]==0){
          if(d2max==field[i][j]){ vx.push_back(j); vy.push_back(i);}
          else{
            vx.clear(); vy.clear();
            vx.push_back(j); vy.push_back(i);
          }
          d2max=field[i][j];
        }
      }
      if(d2max==-1)break;
      dmax=d2max;
    }
    
    char alpha[30],cc='a';
    memset(alpha,0,sizeof(alpha));
    
    for(int i=0;i<H;i++){
      for(int j=0;j<W;j++){
        if(j)printf(" ");
        
        if(alpha[ans[i][j]]==0){
          alpha[ans[i][j]]=cc;
          printf("%c",cc);
          cc++;
        }else{
          printf("%c",alpha[ans[i][j]]);
        }
      }
      puts("");
    }
  }
  return 0;
}