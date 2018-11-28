#include <cstdio>
#include <algorithm>
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
#define SZ(x) ((int) (x).size())
#define EPS 1E-9
#define INF 0x3F3F3F3f
#define D(x) cout<<__LINE__<<"  "#x" is "<<x<<endl
#define DM(mat,rows,cols) FOR(i,rows){FOR(j,cols)cout<<mat[i][j]<<" ";cout<<endl;}

int cmp(double x, double y = 0, double tol = EPS) {
   return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool cmp_eq(double x, double y) { return cmp(x, y) == 0; }
bool cmp_lt(double x, double y) { return cmp(x, y) < 0; }

int main()
{
   freopen("in/B-large.in","r",stdin);
   freopen("out/B-large.out","w",stdout);   
   
   int T, c10;
   bool yes = false;
   string str, strx, str2;
   
   cin >> T;
   FOR(i,T)
   {
      strx = "";
      cin >> str;
      //strx = str;
      c10 = 0;
      FOR(j,SZ(str))
      {
         if(str[j]=='0') c10++;
         else strx += str[j];
      }
      //strx = str2;
      sort(ALL(strx));
      str2 = str;
      //sort(ALL(str2));
      yes = false;
      //next_permutation(ALL(str2));
      //cout << str << endl;
      while(!yes)
      {
         //cout << ">" << str2 << endl;
         while(next_permutation(ALL(str2)) && (!yes))
         {
            //cout << ">>" << str2 << endl;
            if(str2[0]!='0')
            {
               yes = true;
               //cout << str2 << endl;
               break;
            }
         }
         if(!yes)
         {  
            str2 = strx;
            c10++;
            FOR(j,c10) str2.insert(1,"0");
            //cout << ">>>" << str2 << endl;
            if(str2[0]!='0')
            {
               yes = true;
               break;
            }
         }
      }
      cout << "Case #" << (i+1) << ": " << str2 << endl;
   }
   
   return 0;
}
