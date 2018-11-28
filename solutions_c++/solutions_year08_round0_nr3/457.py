#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LINF 90000000000000000000LL
#define LLMAX ((unsigned long long)(-1))

int N;
long double f, R, t, r, g;
long double rad;


bool inside(long double x, long double y) { return SQ(x) + SQ(y) < SQ(rad) + eps;}

long double findK(long double x1, long double y1, long double x2, long double y2){
//   cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
   long double th1, th2, A1, A2, T1, T2, B, C;

   th1 = acos(y2/rad);
   th2 = asin(x1/rad);

   A1 = SQ(rad) * th1 / 2;
   A2 = SQ(rad) * th2 / 2;

   T1 = x2 * y2 / 2;
   T2 = x1 * y1 / 2;
   B = x1 * (y1 - y2);
   C = A2 - T2;
   return A1 - T1 - B - C;
}

int counter[4];

int main(){
   cin >> N;

   FOR(i,0,N){
      cin >> f >> R >> t >> r >> g;
      long double racket = PI * SQ(R), safe = 0;
      rad = R - t - f;
      long double x, y, rect = SQ(g-f-f);
      x = y = r;
      MEMSET(counter,0);

      int rc = 0;
      while(y < rad+eps){
	    while(x < rad+eps){
		    if(!inside(x+f,y+f)) break;
//		    cout << "Inside for SOME points" << endl;
		    if(inside(x+g-f,y+g-f)) safe += rect, rc++;
		    else{
//  	   	            cout << "corner at: (" << x+f << "," << y+f << ")" << endl;
//			    cout << "Before: " << safe << endl;

			    int desc = 0;
			    long double x1, y1, x2, y2, add;
			    if(inside(x+f,y+g-f)) { desc += 2; y1 = y+g-f; x1 = sqrt(SQ(rad)-SQ(y1)); add = (x1-x-f) * (g-f-f);
				safe += add;
//				cout << "Adding left: " << add << endl;
			    }
			    else { x1 = x+f; y1 = sqrt(SQ(rad)-SQ(x1));}

			    if(inside(x+g-f,y+f)) { desc += 1; x2 = x+g-f; y2 = sqrt(SQ(rad)-SQ(x2)); add= (x2-x1) * (y2-y-f); 
				safe += add;
//				cout << "Adding below: " << add << endl;
			    }
			    else { y2 = y+f; x2 = sqrt(SQ(rad)-SQ(y2));}
//			    cout << "Type: " << desc << endl;
			    safe += findK(x1,y1,x2,y2);
//			    cout << "After: " << safe << endl;
			    counter[desc]++;
			}
		    x += g + r + r;
		}
	    x = r; y += g + r + r;
	}
/*
     cout << "RC: " << rc << " -> " << rc * rect << endl;
     cout << "RSrad: " << racket << " " << 4*safe << " " << PI * SQ(rad) << endl;
     cout << "Hit: " << racket - 4 * safe << endl;
     cout << "Counters: "; FOR(j,0,4) cout << counter[j] << " "; cout << endl;
*/
     cout << "Case #" << (i+1) << ": " << (racket - 4 * safe) / racket << endl;
//     cout << endl;
   }
   return 0;
}
