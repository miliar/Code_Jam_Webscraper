#include<iostream>
#include<vector>
#include<map>
using namespace std ;
typedef long long LL ;
int t[110][110] ;
int odp[110][110] ;
struct punkt
{
      int x, y, w ;
      punkt(int xx=0, int yy=0, int ww=0) : x(xx), y(yy), w(ww) {}
} ;
bool operator<(const punkt &a, const punkt &b)
{
      if(a.w != b.w) return a.w < b.w ;
      else if(a.x != b.x) return a.x < b.x ;
      else return a.y < b.y ;
}  
main()
{
      ios_base::sync_with_stdio(0) ;
      int C, H, W, i, j, k ;
      int t_x[] = { -1, 0, 0, 1} ;
      int t_y[] = { 0, -1, 1, 0 } ;
      cin >> C ;
      for(int test=1 ; test<=C ; test++)
      {
            cin >> H >> W ;
            vector<punkt> tab ;
            for(i=0 ; i<H ; i++)
                  for(j=0 ; j<W ; j++)
                  {
                        cin >> t[i][j] ;
                        tab.push_back(punkt(i,j, t[i][j])) ;
                        odp[i][j] = 0 ;
                  }
            sort(tab.begin() , tab.end()) ;
            int nast = 1 ;
            for(vector<punkt>::iterator q = tab.begin() ; q!=tab.end() ; q++)
            {
                  int a=-100, b=-100, ile=1000000000 ;
                  for(k=0 ; k<4 ; k++)
                  {
                        int nx = q->x + t_x[k] ;
                        int ny = q->y + t_y[k] ;
                        if(nx>=0 && nx<H && ny>=0 && ny<W && t[nx][ny] < q->w && ile > t[nx][ny])
                        {
                              a = nx ;
                              b = ny ;
                              ile = t[nx][ny] ;
                        }
                  }
                  if(ile==1000000000) odp[q->x][q->y] = nast++ ;
                  else odp[q->x][q->y] = odp[a][b] ;
            }
            cout << "Case #" << test << ": " << endl ;
            map<int, char> mapa ;
            char dawaj = 'a' ;
            for(i=0 ; i<H ; i++)
            {
                  for(j=0 ; j<W ; j++)
                  {
                        if(mapa.find(odp[i][j])==mapa.end()) mapa[odp[i][j]] = dawaj ++ ;
                        cout << mapa[odp[i][j]] << " " ;
                  }
                  cout << endl ;
            }
      }
}
