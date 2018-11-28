#include <iostream>
#include <utility>
#include <algorithm>

inline int min(int a, int b) { if(a < b) return a; return b; }

using namespace std;

bool tree[10001], can[10001];

int leaf;

inline int next_left(int n) { return 2*n; }
inline int next_right(int n) { return 2*n + 1; } 
inline int up(int n) { return n<<1; }
inline bool is_leaf(int n) { return n > leaf; }

//This is O(n), n = 10000
int memo1[10001];
int eval(int start)
{
    int& retVal = memo1[start];
    if(retVal != -1) return retVal;

    if(is_leaf(start)) retVal = tree[start];
    else if(tree[start] == 0)
	retVal = eval(next_left(start)) | eval(next_right(start));
    else 
	retVal = eval(next_left(start)) & eval(next_right(start));

    return retVal;
}

int memo2[10001];
int doit(int start)
{
    int& retVal = memo2[start];
    if(retVal != -1) return retVal;
    retVal = 999999999;

    if(eval(start) == 1) return retVal = 0;
    if(is_leaf(start)) return retVal = 999999999;
    
    if(tree[start] == 0) 
	retVal = min(doit(next_left(start)), doit(next_right(start)));
    else
    {
	if(can[start])
	    retVal = min(retVal, 1 + min(doit(next_left(start)), doit(next_right(start))));
	retVal = min(retVal, doit(next_left(start)) + doit(next_right(start)));
    }

    return retVal;     
}

int main()
{
  int n;
  cin >> n;
  for(int z = 0; z < n; z++)
  {
      memset(memo1, -1, sizeof(memo1));
      memset(memo2, -1, sizeof(memo2));
      for(int i = 0; i < 10001; i++) tree[i] = can[i] = 0;

      int m, v;
      cin >> m >> v; v ^= 1;
      leaf = (m-1)/2;
      tree[0] = 0; can[0] = 0; int start = 1, i;
      for(i = 0; i < leaf; i++) { int temp, chg; cin >> temp >> chg; tree[start] = temp ^ v; can[start++] = chg; }
      for(; i < m; i++) { int temp; cin >> temp; tree[start] = temp ^ v; can[start++] = 0; }
      
      int ret = doit(1);
      if(ret > 10000) cout << "Case #" << z + 1 << ": IMPOSSIBLE" << endl;
      else cout << "Case #" << z + 1 << ": " << doit(1) << endl;
  }
}
