#include <cstdio>
#include <set>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int)(x).size())
#define EPS 1E-10
#define INF 0x3F3F3F3f
#define MAX 40
#define DV(x) cout<<__LINE__<<"  "#x" is "<<x<<endl
#define DM(mat,rows,cols) FOR(i,rows){FOR(j,cols)cout<<mat[i][j]<<" ";cout<<endl;}

int cmp(double x, double y = 0, double tol = EPS) {
   return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool cmp_eq(double x, double y) { return cmp(x, y) == 0; }
bool cmp_lt(double x, double y) { return cmp(x, y) < 0; }


int main()
{
   freopen("in/A-large.in","r",stdin);
   freopen("out/A-large.out","w",stdout);

   int T, N, k, cnt = 0;
   string str;

   getline(cin,str);
   sscanf(str.c_str(),"%d",&T);
   
   FOR(t,T)
   {
      cnt = 0;
      
      getline(cin,str);
      sscanf(str.c_str(),"%d",&N);
      
      vector<int> M(N+1,0);
      
      FOR(i,N)
      {
         getline(cin,str);
         FORI(j,1,N+1)
         {
            if(str[j-1]=='1') M[i] >?= j;
         }
         //cout << M[i] << " ";
      }
      //cout << endl;
      
      //FOR(i,N)
      for(int i=0;i<N;++i)
      {
         if(M[i]>i+1)
         {
            int j;
            for(j=i+1;j<N;++j) if(M[j]<=i+1) break;
            for(int l=j;l>i;--l) { swap(M[l],M[l-1]); cnt++; }
         }
      }
      printf("Case #%d: %d\n",t+1,cnt);
   }

   return 0;
}
