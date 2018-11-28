#include <iostream>
#include <queue>
using namespace std;

int t,h,w;
int elev[110][110];
char map[110][110];
int flow[110][110];
int dir[][2] = { {0,0}, {-1,0}, {0,-1}, {0,1}, {1,0} };

typedef pair<int,int> pos;

inline bool ok(int r, int c) { return (r>=0 && r<h && c>=0 && c<w); }
inline int lev(int r, int c) { return (r>=0 && r<h && c>=0 && c<w) ? elev[r][c] : 20000; }

int nxt(int r, int c)
{
  int m=15000,d=0;
  for(int i=0;i<5;i++)
    { int l=lev(r+dir[i][0],c+dir[i][1]); if (l<m) {m=l; d=i;} }
  return d;
}

main()
{
  cin >> t; for(int line=1;line<=t;line++)
  {
    char cur=1; queue<pos> Q;
    cin >> h >> w;

    for(int i=0;i<h;i++) for(int j=0;j<w;j++) scanf("%d",&elev[i][j]);

    for(int i=0;i<h;i++) for(int j=0;j<w;j++)
    {
      map[i][j] = 0;
      flow[i][j] = nxt(i,j);
      if (!flow[i][j])
      {
        map[i][j]=cur++; Q.push(make_pair(i,j));
      }
    }

    while(!Q.empty())
    {
      pos P=Q.front(); Q.pop();
      int r=P.first, c=P.second;
      for(int i=1;i<5;i++)
      {
        int ri=r+dir[i][0], ci=c+dir[i][1];
        if (ok(ri,ci) && !map[ri][ci])
        {
          if (flow[ri][ci]+i == 5)
          {
            map[ri][ci]=map[r][c];
            Q.push(make_pair(ri,ci));
          }
        }
      }
    }

    char tran[30]; cur='a';
    memset(tran,0,sizeof(tran));

    printf("Case #%d:\n", line);
    for(int i=0;i<h;i++) 
    {
      for(int j=0;j<w;j++) { char c=map[i][j]; if (!tran[c]) tran[c]=cur++;
      putchar(tran[c]); putchar(' '); } putchar(10);
    }
  }
}
