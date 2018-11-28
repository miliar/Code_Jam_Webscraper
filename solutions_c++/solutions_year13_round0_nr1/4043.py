#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>
#include <climits>
#include <functional>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back


typedef unsigned int uint;
typedef long long LL;
typedef long double LD;

typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl

typedef enum dir {
   North, West, South, East, none
};



int main(int argc, char **argv)
{

   int testcases, result, w, h;

   cin >> testcases;


   char map[4][4];
   char tmp;

   for (int caso = 1; caso <= testcases; ++caso)
   {
      std::cin.get(tmp);
      for (int i = 0; i < 4; i++)
      {
         for (int j = 0; j < 4; j++)
         {
            std::cin.get(map[i][j]);
            //cout << map[i][j];
         }
         //cout << endl;
         std::cin.get(tmp);
      }


      bool start = true;
      bool finished = false;
      int cont = 0;
      char curr = 'm';
      for (int i = 0; i < 4 && !finished; i++)
      {
         start = true;
         cont = 0;
         for (int j = 0; j < 4; j++)
         {
            if (start) {
               curr = map[i][j];
               if (curr != 'T') start = false;
               cont++;
            } else if (curr == map[i][j] || map[i][j] == 'T') cont++;


            if (curr == '.' || map[i][j] == '.') break;
            //cout << curr << " " <<  cont << " ";
         }
         if (cont == 4) {
            finished = true;
            cout << "Case #" << caso << ": " << curr << " won" << endl;
            break;
         }
      }
      for (int i = 0; i < 4 && !finished; i++)
      {
         start = true;
         cont = 0;
         for (int j = 0; j < 4; j++)
         {
            if (start) {
               curr = map[j][i];
               if (curr != 'T') start = false;
               cont++;
            } else if (curr == map[j][i] || map[j][i] == 'T') cont++;
            if (curr == '.' || map[j][i] == '.') break;
         }
         if (cont == 4) {
            finished = true;
            cout << "Case #" << caso << ": " << curr << " won" << endl;
            break;
         }
      }
      cont = 0;
      start = true;
      for (int j = 0; j < 4 && !finished; j++)
      {
         if (start) {
            curr = map[j][j];
            if (curr != 'T') start = false;
            cont++;
         } else if (curr == map[j][j] || map[j][j] == 'T') cont++;
         if (curr == '.' || map[j][j] == '.') break;
         if (cont == 4) {
            finished = true;
            cout << "Case #" << caso << ": " << curr << " won" << endl;
            break;
         }
      }
      cont = 0;
      start = true;
      for (int j = 0; j < 4 && !finished; j++)
      {
         if (start) {
            curr = map[j][3-j];
            if (curr != 'T') start = false;
            cont++;
         } else if (curr == map[j][3-j] || map[j][3-j] == 'T') cont++;
         if (curr == '.' || map[j][3-j] == '.') break;
         if (cont == 4) {
            finished = true;
            cout << "Case #" << caso << ": " << curr << " won" << endl;
            break;
         }
      }

      if (!finished ) {
         for (int i = 0; i < 4 && !finished; i++)
         {
            for (int j = 0; j < 4 && !finished; j++)
            {
               if (map[i][j] == '.') {
                  finished = true;
                  cout << "Case #" << caso << ": Game has not completed" << endl;
               }
            }

         }
      }
      if (!finished) {
         cout << "Case #" << caso << ": Draw" << endl;
         
      }



   }

}