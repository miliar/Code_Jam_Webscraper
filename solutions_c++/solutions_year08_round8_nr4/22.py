//MADE BY lordmonsoon A.I.
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define mp make_pair
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())


////////////////////////////////////////////////////////////////////////////////

int t,n,p,k,c;
map<vi, int> M;
map<int, vi> M2;

vector<int> P,Q;

void generuj(int ile, int last)
{
      if(ile == k)
      {
            M2[c] = P;
            M[P] = c++;
      }
      else
      {
            FOR(i,last,p)
            {
                  P[ile] = i;
                  generuj(ile+1,i + 1);
                  P[ile] = 0;
            }
      }
}

struct MATRIX
{
      short int M[253][253];
};


MATRIX create(void)
{
      MATRIX w;
      REP(i,c) REP(j,c) w.M[i][j] = 0;
      REP(i,c)
      {
            vector<int> S = M2[i];
            REP(j,k) S[j]++;
            int ind = -1;REP(j,k) if(S[j] == p+1) ind = j;
            if(ind == -1)
            {
                  REP(j,k)
                  {
                        vi T = S;
                        T[j] = 1;
                        sort(T.begin(),T.end());
                        w.M[i][M[T]]++;
                  }
            }
            else
            {
                  S[ind] = 1;
                  sort(S.begin(),S.end());
                  w.M[i][M[S]]++;
            }
             
      }      
      return w;
}

#define MOD 30031

MATRIX mnoz(MATRIX &a,MATRIX &b)
{
      MATRIX ret;
      REP(i,c) REP(j,c)
      {
            ret.M[i][j] = 0;
            REP(k,c) ret.M[i][j] = (ret.M[i][j] + a.M[i][k] * b.M[k][j])%MOD;
      }
      return ret;
}

MATRIX G[32];

void gogo(MATRIX &e,int n,int gl = 0)
{
      if(n == 0)
      {
            REP(i,c) REP(j,c) G[gl].M[i][j] = 0;
            REP(i,c) G[gl].M[i][i] = 1;
      }
      else
      {
            gogo(e,n/2,gl+1);
            G[gl] = mnoz(G[gl+1],G[gl+1]);
            if(n&1) G[gl] = mnoz(G[gl],e);
      }
}

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            scanf("%d %d %d",&n,&k,&p);
            M.clear();M2.clear();c = 0;
            P.clear();
            REP(i,k) P.push_back(0);
            generuj(0,1);
            REP(i,k) P[i] = i+ 1;
            
            MATRIX start= create();
/*            REP(i,c)
            {
                  REP(j,c) cout << start.M[i][j] << " ";
                  cout << endl;
            }
*/
//            MATRIX w = start;
/*            REP(i,c)
            {
                  REP(j,c) cout << start.M[i][j] << " ";
                  cout << endl;
            }
*/
            gogo(start,n-k);
            MATRIX w = G[0];
//            REP(i,n-k-1) w = mnoz(start,w);
            printf("Case #%d: ",t2);
            int ret = 0;
            REP(i,c)
            {
                  bool gut = true;
                  vi S = M2[i];
                  REP(j,k) gut = gut && (S[j]<=k && S[j] >= 1);
                  if(gut)
                  {
                        int s = M[P];
                        ret = (ret + w.M[M[P]][i])%MOD;
                  }
                  
            }
            
            printf("%d\n",ret);
      }
      return 0;
}
