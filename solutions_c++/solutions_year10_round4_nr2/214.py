#include <algorithm>
#include <climits>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmin( T &res, const U &x ) { if ( x < res ) res = x; }
typedef long long int64;
#define ZERO(v) memset(v, 0, sizeof v)

const int MAXP = 10;
const int64 INF = LONG_LONG_MAX / 4;

int P;

struct Node {
   int64 cost;
   int64 memo[MAXP+1];
   Node *left, *right;

   Node(bool leaf, int mixed, Node *left, Node *right) : left(left), right(right) {
      if (leaf) {
         fill(memo, memo+P+1, INF);
         for (int i=P-mixed; i<=P; ++i) {
            memo[i] = 0;
         }
      } else {
         fill(memo, memo+P+1, -1);
         cost = mixed;
      }
   }

   int64 calc(int bought) {
      int64 &ret = memo[bought];
      if (ret != -1) return ret;

      ret = INF;
      for (int b=0; b<=1; ++b) {
         relaxmin(ret, b*cost + left->calc(bought+b) + right->calc(bought+b));
      }
      return ret;
   }

   ~Node() {
      if (left) delete left;
      if (right) delete right;
   }
};

Node *nodep[MAXP+2][1<<(MAXP+2)];
           
int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      cin >> P;

      ZERO(nodep);
      for (int i=P; i>=0; --i) {
         for (int j=0; j<(1<<i); ++j) {
            int x; cin >> x;
            nodep[i][j] = new Node(i == P, x, nodep[i+1][2*j], nodep[i+1][2*j+1]);
         }
      }

      cout << "Case #" << tt << ": " << nodep[0][0]->calc(0) << endl;
      delete nodep[0][0];
   }

   return 0;
} 
