#include <iostream>

using namespace std;
#define MAX 10000
#define OR 0
#define AND 1
#define LEFT(n) (((n)*2)+1)
#define RIGHT(n) (((n)*2)+2)

int value[MAX];
int op[MAX];
int changeable[MAX];
int N, M, V;

bool isleaf(int node) {
  return !(node < (M - 1) / 2);
}

bool eval(int leaf) {
  if (isleaf(leaf)) {
    return value[leaf];
  } else {
    int left = eval(LEFT(leaf));
    int right = eval(RIGHT(leaf));
    return op[leaf] == AND ? left && right : left || right;
  }
}

int dp[MAX][2];

int rec (int node, int target) {
  //cout << "looking" << node + 1 << endl;
  int ret;
  if (dp[node][target] != -2) {
    ret = dp[node][target];
  }
  else if (eval(node) == target) {
    ret = 0;
  } else {
    if (isleaf(node)) {
      ret = -1;
    } else {
      ret = INT_MAX;
      bool left = eval(LEFT(node));
      bool right = eval(RIGHT(node));
      //int leftflip = rec(LEFT(NODE), left ^ 1);
      //int rightflip = rec(RIGHT(NODE), right ^ 1);
      for (int i = 0; i < 2; i++) {
        if (i == 1 && !changeable[node]) break;
        if (i == 1) {
          op[node] ^= 1;
        }
        //cout << node + 1 << " target = " << target << " op = " << (op[node] == AND ? "AND" : "OR") << endl;
        if (target == 1) {
          int tmpleft = (left ? 0 : rec(LEFT(node), 1));
          int tmpright = (right ? 0 : rec(RIGHT(node), 1));
          if (op[node] == AND) {
            //cout << "hoge" << endl;
            if (tmpleft != -1 && tmpright != -1) {
              ret = min(ret, tmpleft + tmpright + i);
            }
          } else {
            if (tmpleft != -1) {
              ret = min(ret, tmpleft + i);
            }
            else if (tmpright != -1) {
              ret = min(ret, tmpright + i);
            }
          }
        } else { //target == 0
          int tmpleft = (!left ? 0 : rec(LEFT(node), 0));
          int tmpright = (!right ? 0 : rec(RIGHT(node), 0));
          if (op[node] == AND) {
            if (tmpleft != -1) {
              ret = min(ret, tmpleft + i);
            }
            if (tmpright != -1) {
              ret = min(ret, tmpright + i);
            }
          } else {
            if (tmpleft != -1 && tmpright != -1) {
              ret = min(ret, tmpleft + tmpright + i);
            }
          }
        }
        if (i == 1) {
          op[node] ^= 1;
        }
      }
      if (ret == INT_MAX) ret = -1;
      //cout << node + 1 << " -> " << V << " -- " << ret << endl;
    }
  }
  //cout << node + 1 << " to " << target << " is " << ret << endl;
  return dp[node][target] = ret;
}

main () {
  cin >> N;
  for (int n = 0; n < N; ++n) {
    cin >> M >> V;
    //cout << M << endl;
    for (int m = 0; m < M; m++) {
      if (!isleaf(m)) {
        cin >> op[m] >> changeable[m];
      }
      else {
        cin >> value[m];
      }
    }
    for (int i = 0; i < MAX; i++) {
      dp[i][0] = dp[i][1] = -2;
    }
    int res = rec(0, V);
    printf("Case #%d: ", n + 1);
    if (res == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << res << endl;
    }
  }
}

