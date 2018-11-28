#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

// types
typedef unsigned long long UINT; 
typedef long long INT;


// limits
#define MAX_M 10000

static bool is_debug = getenv("MYDEBUG") != NULL;

template <class DST, class SRC>
static DST lexical_cast(const SRC &src)
{
  stringstream ss;
  ss << src;
  DST r;
  ss >> r;
  return r;
}

enum GATE{
  GATE_OR,
  GATE_AND,
};

struct Node {
  bool isLeaf;
  bool isChangable;
  GATE gate;
  bool val;
};

static inline unsigned parentIndex(unsigned n)
{
  return n/2;
}

static inline unsigned leftChildIndex(unsigned n)
{
  return n*2;
}

static inline unsigned rightChildIndex(unsigned n)
{
  return n*2+1;
}

// [node][gate][val]
unsigned dp[MAX_M+1][2][2];

// static go(unsigned index, Node *nodes, unsigned M, bool val)
// {

//   int r;

//   if (dp[index][GATE_AND][val] || dp

//   if (!nodes[index].isChangable)
//     dp[index][nodes[index].gate == GATE_AND ? GATE_OR : GATE_AND][val] = -1;

//   if (nodes[index].gate == GATE_AND) {
//     if (val) {
//       int rl, rr;
//       rl = go(leftChildIndex(index), nodes, M, 1);
//       rr = go(rightChildIndex(index), nodes, M, 1);
//       dp[index][GATE_AND][val] = rl+rr;
//     } else {
//       int rl0, rl1, rr0, rr1;
//       rl0 = go(leftChildIndex(index), nodes, M, 0);
//       rl1 = go(leftChildIndex(index), nodes, M, 1);
//       rr0 = go(rightChildIndex(index), nodes, M, 0);
//       rr1 = go(rightChildIndex(index), nodes, M, 1);

//       dp[index][GATE_AND][val] = min(rl0+rr0, min(rl0+rr1, min(rl1,rr0)));
//     }
//   } else {
//     if (val) {
//       int rl0, rl1, rr0, rr1;
//       rl0 = go(leftChildIndex(index), nodes, M, 0);
//       rl1 = go(leftChildIndex(index), nodes, M, 1);
//       rr0 = go(rightChildIndex(index), nodes, M, 0);
//       rr1 = go(rightChildIndex(index), nodes, M, 1);

//       dp[index][GATE_OR][val] = min(rl0+rr1,min(rl1+rr0, min(rl1+rr1)));
//     } else {
//       int rl, rr;
//       rl = go(leftChildIndex(index), nodes, M, 0);
//       rr = go(rightChildIndex(index), nodes, M, 0);
//       dp[index][GATE_OR][val] = rl+rr;
//     }
//   }
// }


int lg(unsigned n)
{
  unsigned r = 0;
  while (n >>= 1)
    r++;
  return r;
}

string compute(Node *nodes, unsigned M, bool rootVal)
{
  if (is_debug)
    for (unsigned i = 1; i <= M; i++) {
      cout <<"nodes["<<i<<"]=("<<nodes[i].isLeaf<<","<<nodes[i].isChangable<<","<<nodes[i].gate<<","<<nodes[i].val<<")"<<endl;
    }

  unsigned last_inter = parentIndex(M);
  unsigned last_2nd_level = lg(last_inter);
  int inf = MAX_M+1;

  for (unsigned i = (M-1)/2 +1; i <= M; i++)  {
    dp[i][GATE_AND][nodes[i].val] = 0;
    dp[i][GATE_OR][nodes[i].val] = 0;
    dp[i][GATE_AND][!nodes[i].val] = inf;
    dp[i][GATE_OR][!nodes[i].val] = inf;
  }

  for (int level = last_2nd_level; level >= 0; level--)
    for (unsigned i = 1<<level; i<= last_inter && i <= (1<<(level+1))-1; i++) {
      if (is_debug) {
	cout << "level="<< level << " i="<<i << endl;
      }
      unsigned lc = leftChildIndex(i), rc = rightChildIndex(i);
      GATE gate = nodes[i].gate;

      int l0 = min(dp[lc][GATE_AND][0], dp[lc][GATE_OR][0]);
      int l1 = min(dp[lc][GATE_AND][1], dp[lc][GATE_OR][1]);
      int r0 = min(dp[rc][GATE_AND][0], dp[rc][GATE_OR][0]);
      int r1 = min(dp[rc][GATE_AND][1], dp[rc][GATE_OR][1]);
      if (is_debug) {
	cout << "l0="<<l0 << " l1="  << l1 << " r0="<<r0<<" r1="<<r1<<endl;
      }

      int val0_min[2];
      int val1_min[2];

      val0_min[GATE_AND] = min(l0+r0, min(l0+r1, l1+r0));
      val0_min[GATE_OR] = l0+r0;
      val1_min[GATE_AND] = l1+r1;
      val1_min[GATE_OR] = min(l0+r1, min(l1+r0, l1+r1));

      if (!nodes[i].isChangable) {
	dp[i][gate][0] = val0_min[gate];
	dp[i][gate][1] = val1_min[gate];
	dp[i][!gate][0] = dp[i][!gate][1] = inf;
      } else {
	dp[i][gate][0] = val0_min[gate];
	dp[i][gate][1] = val1_min[gate];
	dp[i][!gate][0] = val0_min[!gate]+1;
	dp[i][!gate][1] = val1_min[!gate]+1;

      }

      if (is_debug) {
	cout <<dp[i][GATE_AND][0] << endl;
	cout <<dp[i][GATE_OR][0] << endl;
	cout <<dp[i][GATE_AND][1] << endl;
	cout <<dp[i][GATE_OR][1] << endl;

      }
    }
  
  int r = min(dp[1][GATE_AND][rootVal], dp[1][GATE_OR][rootVal]);
  return r < inf ? lexical_cast<string>(r) : "IMPOSSIBLE";
}

int main(int argc, char **argv)
{
  string line;
  unsigned nof_cases;

  getline(cin, line);
  nof_cases = lexical_cast<unsigned>(line);
  unsigned case_ = 1;
  while (case_ <= nof_cases) {
    Node nodes[MAX_M+1];
    getline(cin, line);
    istringstream is(line);
    unsigned M;
    bool V;
    is >> M >> V;
    for (unsigned i = 1; i <= (M-1)/2; i++) {
      getline(cin, line);
      istringstream is(line);
      unsigned G, C;
      is >> G >> C;
      nodes[i].isLeaf = false;
      nodes[i].gate =  G == 1 ? GATE_AND : GATE_OR;
      nodes[i].isChangable = C == 1 ? true : false;
    }

    for (unsigned i = 1; i <= (M+1)/2; i++) {
      getline(cin, line);
      nodes[i+(M-1)/2].isLeaf = true;
      nodes[i+(M-1)/2].val = lexical_cast<unsigned>(line);
    }
      
    cout << "Case #"<< case_++ << ": " << compute(nodes, M, V) << endl;
  }

  return 0;
}

