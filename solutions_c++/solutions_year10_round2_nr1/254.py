// In Brother Chun we trust...
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <string>
#include <queue>

#define _DEBUG_MODE_

#ifdef _DEBUG_MODE_
#define db(X) cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl;
#define db_arr(X) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrM(X, M) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; __i__++) cerr << X[__i__] << " "; cerr << endl;
#define db_arrMN(X, M, N) cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; __i__++) cerr << X[__i__] << " "; cerr << endl;
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);i++)
#define ForL(i, m, n) for(i=(m);i<(n);i++)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();

int main() {
  // COUNTER CODE STARTS HERE

  int cases, i;

  cin >> cases;

  For (i, cases) {
    printf("Case #%d: ", i+1);
    _main();
    cout << endl;
  }

  // COUNTER CODE ENDS HERE

  return 0;
}

// ACTUAL CODE STARTS BELOW
vector<string> dirs;
int N, M;

vector<string> readDir() {
  vector<string> result;
  result.clear();
  string p;
  int l, i, j;

  cin >> p;
  l = 1;

  while (true) {
    l = p.find("/", l);
    result.push_back(p.substr(0, l));
    db(p.substr(0, l));
    if (l == -1) {
      break;
    }
    l++;
  }

  return result;
}

bool insert_dir(string dir) {
  if (find(dirs.begin(), dirs.end(), dir) == dirs.end()) {
    dirs.push_back(dir);
    return true;
  }
  return false;
}

void _main() {
  dirs.clear();
  cin >> N >> M;
  int i, j, k;
  vector<string> v;
  dirs.push_back("/");

  For (i, N) {
    v = readDir();
    For (j, v.size()) {
      insert_dir(v[j]);
    }
  }

  k = 0;

  For (i, M) {
    v = readDir();

    For (j, v.size()) {
      if (insert_dir(v[j])) k++;
    }
  }
  
  cout << k;
}
