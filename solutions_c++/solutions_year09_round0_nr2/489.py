#include<iostream>
#include<vector>
using namespace std;

const int dr[]={-1,0,0,1};
const int dc[]={0,-1,1,0};
struct pt { int r,c; pt(int a,int b):r(a),c(b) {} };

int board[100][100],rows,cols;
char mark[100][100];

void mkmark()
{ 
  int r,c,sc=0;
  for(r=0;r<rows;++r) for(c=0;c<cols;++c) mark[r][c]=0;
  for(r=0;r<rows;++r) for(c=0;c<cols;++c) if(mark[r][c]==0)
  { vector<pt> v;
    int tr=r,tc=c;
    while(mark[tr][tc]==0)
    { v.push_back(pt(tr,tc));
      int bi=-1,i;
      for(i=0;i<4;++i)
      { int nr=tr+dr[i], nc=tc+dc[i];
        if(nr<0||nr>=rows||nc<0||nc>=cols) continue;
        if(board[nr][nc]>=board[tr][tc]) continue;
        if(bi==-1 || board[nr][nc]<board[tr+dr[bi]][tc+dc[bi]]) bi=i;
      }
      if(bi==-1) break;
      tr+=dr[bi]; tc+=dc[bi];
    }
    char m = (mark[tr][tc]?mark[tr][tc]:('a'+sc++));
    for(int i=0;i<v.size();++i) mark[v[i].r][v[i].c]=m;
  }
}

int main()
{
  int ci,cn,r,c;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>rows>>cols;
    for(r=0;r<rows;++r) for(c=0;c<cols;++c) cin>>board[r][c];
    mkmark();
    cout<<"Case #"<<ci<<":\n";
    for(r=0;r<rows;++r)
    { cout<<mark[r][0];
      for(c=1;c<cols;++c) cout<<' '<<mark[r][c];
      cout<<endl;
    }
  }
}
