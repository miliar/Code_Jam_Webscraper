#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
using namespace std ;
typedef long long LL ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
struct kraw
{
      int x, y, d ;
      string s ;
      kraw(int xx=0, int yy=0 , int dd=0, const string ss=string()) : x(xx), y(yy), d(dd), s(ss) {}
} ;
vector<kraw> graf[20][50] ;
char board[20][50] ;
int wart[20][50] ;
const int MAX = 1000, MIN = 0, PRZESUNIECIE = 500 ;
string odp[MAX+1][20][50] ;
main()
{
      ios_base::sync_with_stdio(0) ;
      int C, i, j, k, q , Q, W ;
      cin >> C ;
      int t_x[] = {-1, 0, 0, 1} ;
      int t_y[] = {0, -1, 1, 0} ;
      for(int test=1 ; test<=C ; test++)
      {
            cout << "Case #" << test << ":" << endl ;
            cin >> W >> Q ; // odwr
            REP(i,W) REP(j,W)
            {
                  cin >> board[i][j] ;
                  graf[i][j].clear() ;
                  if(board[i][j]>='0' && board[i][j]<='9') {
                        int a = board[i][j] - '0' ;
                        wart[i][j] = a ;
                      //  cout << "wart[" << i << "," << j << " = " << wart[i][j] << endl ;
                  }
            }
            REP(i,W) REP(j,W)
            {
                  if(!(board[i][j]>='0' && board[i][j]<='9')) continue ;
                  REP(k, 4)
                  {
                        int nx = i + t_x[k] ;
                        int ny = j + t_y[k] ;
                        if(nx<0 || nx>=W || ny<0 || ny>=W) continue ;
                        REP(q, 4)
                        {
                              int mx = nx + t_x[q] ;
                              int my = ny + t_y[q] ;
                              if(mx<0 || mx>=W || my<0 || my>=W ) continue ;
                              string s ;
                              s += board[nx][ny] ;
                              s += string(1, wart[mx][my]+'0') ;
                              graf[i][j].push_back(kraw(mx,my, (board[nx][ny]=='+' ? wart[mx][my] : -wart[mx][my]), s)) ;
                        //      cout << "dla " << i << " " << j << " dokladam " << graf[i][j].back().x << " " << graf[i][j].back().y << " " << graf[i][j].back().d << " " << s << endl ;
                        }
                  }
            }
            
            for(i=MIN ; i<=MAX ; i++) {
                  REP(j,20) REP(k,50)
                  odp[i][j][k].clear() ;
            }
            queue< kraw > kolejka ;
            REP(i,W) REP(j,W)
            {
                  if(!(board[i][j]>='0' && board[i][j]<='9')) continue ;
                  odp[wart[i][j]+PRZESUNIECIE][i][j] = string(1, board[i][j]) ;
                  kolejka.push(kraw(i,j, wart[i][j]+PRZESUNIECIE)) ;
            }
                  
                  
            while(!kolejka.empty())
            {
                  kraw a = kolejka.front() ; kolejka.pop() ;
                  FOREACH(q, graf[a.x][a.y]) {
                        int nd = a.d + q->d ;
                        if(nd < MIN || nd >MAX) continue ;
                        string s = odp[a.d][a.x][a.y] + q->s ;
                        if(odp[nd][q->x][q->y]=="" || (odp[nd][q->x][q->y].size() == s.size() && s < odp[nd][q->x][q->y])) {
                              odp[nd][q->x][q->y] = s ;
                        //      cout << "odp[" << nd << " " << q->x << " " << q->y << "] = " << odp[nd][q->x][q->y] << endl ;
                              kolejka.push(kraw(q->x, q->y, nd)) ;
                        }
                  }
            }
            int a ;
            while(Q--)
            {
                  cin >> a ;
                  string s ;
                  REP(i,20) REP(j, 50) {
                        if(odp[a+PRZESUNIECIE][i][j]=="") continue ;
                        else
                        {
                         //     cout << "  " << odp[a+PRZESUNIECIE][i][j] << endl ;
                              if(s=="") s = odp[a+PRZESUNIECIE][i][j] ;
                              else if(odp[a+PRZESUNIECIE][i][j].size() < s.size() || (odp[a+PRZESUNIECIE][i][j].size() == s.size() && odp[a+PRZESUNIECIE][i][j] < s) )
                                    s = odp[a+PRZESUNIECIE][i][j] ;
                        }
                  }
                  cout << s << endl ;           
            }
      }           
}
