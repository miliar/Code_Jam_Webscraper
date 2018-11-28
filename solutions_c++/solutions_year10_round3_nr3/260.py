#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;


int grid[513][513] ;
int hist[513] ;

int main()
{
   freopen("C-small-attempt0.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   scanf("%d",&T) ;
   for(int run=1;run<=T;++run)
   {
      int M , N ;
      cin >> M >> N ;
      for(int i=0;i<M;++i)
      {
         char ch ;
         int t = N/4 ;
         for(int j=0,k=0;j<t;++j)
         {
            cin >> ch ;
            //cout << ch ;
            if('0'<=ch && ch<='9') ch -= '0' ;
            else ch = (ch - 'A') + 10 ;
            grid[i][k++] = ((ch & 8)?1:0) ;
            grid[i][k++] = ((ch & 4)?1:0) ;
            grid[i][k++] = ((ch & 2)?1:0) ;
            grid[i][k++] = ((ch & 1)?1:0) ;
         }
         //cout << endl ;
      }
      
      vector<pair<int,int> > out ;
      while(true)
      {
         int lg = 0 ;
         int x = -1 , y = -1 ;
         for(int base=0;base<M;++base)
         {
            for(int i=0;i<N;++i)
            {
               hist[i] = 0 ;
               if(grid[base][i] == -1) continue ;
               int tc = grid[base][i] ;
               for(int k=base;k<M && grid[k][i]==tc;tc=1-tc,++k,++hist[i]) ;
            }
            int cur = 0 ;
            int cy = -1 ;
            for(int i=0;i<N;++i)
            {
               if(grid[base][i] == -1) continue ;
               int lb = i-1 ;
               int ub = i+1 ;
               int tc = 1-grid[base][i] ;
               for(;lb>=0 && tc==grid[base][lb] && hist[lb]>=hist[i];--lb,tc=1-tc) ;
               ++lb ;
               tc = 1-grid[base][i] ;
               for(;ub<N && tc==grid[base][ub] && hist[ub]>=hist[i];++ub,tc=1-tc) ;
               --ub ;
               int temp = lb ;
               lb = ub-lb+1 ;
               lb = min(hist[i],lb) ;
               if(lb > cur)
               {
                  cur = lb ;
                  cy = temp ;
               }
            }
            if(cur > lg)
            {
               lg = cur ;
               x = base ;
               y = cy ;
            }
         }
         if(lg == 0 || x < 0 || y < 0) break ;
         for(int i=x;i<x+lg;++i) for(int j=y;j<y+lg;++j) grid[i][j] = -1 ;
         if(out.size()>0 && out[out.size()-1].first == lg) out[out.size()-1].second = out[out.size()-1].second + 1 ;
         else out.push_back(make_pair(lg,1)) ;
      }
      printf("Case #%d: %d\n",run,out.size()) ;
      for(int i=0;i<out.size();++i) printf("%d %d\n",out[i].first,out[i].second) ;
   }
   return 0 ;
}
