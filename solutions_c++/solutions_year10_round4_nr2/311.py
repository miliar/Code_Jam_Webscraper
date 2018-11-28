#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

int miss[2000];
int price[2000];


static const int MAX_DEPTH = 13;
static const int SIZE = 1 << (MAX_DEPTH + 1);  // 2^18 = 262144

typedef int Node;

inline Node merge(Node left, Node right) {
  return left < right ? left : right;
}

struct SegmentTree {
  Node data[SIZE];
  void change(int index, Node value) {
    int target = (1 << MAX_DEPTH) + index;
    data[target] = value;
    for (int i = 1; i <= MAX_DEPTH; i++) {
      target >>= 1;
      data[target] = merge(data[target * 2], data[target * 2 + 1]);
    }
  }
  Node get(int left, int right) {
    assert(left <= right);
    return in_get(0, 1, left, right);
  }
private:
  Node in_get(int depth, int node, int left, int right) {
    int width = 1 << (MAX_DEPTH - depth);
    int index = node - (1 << depth);
    int node_left = index * width;
    int node_mid = node_left + (width >> 1);
    if (right - left + 1 == width && left == node_left) {
      return data[node];
    } else if (right < node_mid) {
      return in_get(depth + 1, node * 2, left, right);
    } else if (left >= node_mid) {
      return in_get(depth + 1, node * 2 + 1, left, right);
    }
    return merge(in_get(depth + 1, node * 2, left, node_mid - 1), in_get(depth + 1, node * 2 + 1, node_mid, right));
  }
};
struct FenwickTree {
  int tree[10000];
  FenwickTree() { memset(tree, 0, sizeof(tree)); }
  void add(int index, int value) {
    for (index++; index < SIZE + 1; index += (index & -index)) {
      tree[index] += value;
    }
  }
  int sum(int index) {
    int ret = 0;
    for (index++; index > 0; index -= (index & -index)) {
      ret += tree[index];
    }
    return ret;
  }
};

int p;
int n;
int rangel[2000];
int ranger[2000];
int depth[2000];
//FenwickTree ftree;
//SegmentTree stree;

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    MEMSET(rangel, 0);
    MEMSET(ranger, 0);
    MEMSET(depth, 0);
    //MEMSET(&stree, 0);
    //ftree = FenwickTree();
    test_case++;
    scanf("%d", &p);
    n = 1 << p;
    REP(i, n) {
      scanf("%d", &miss[i]);
      //stree.change(i, miss[i]);
    }
    REP(i, (1 << p) - 1) {
      scanf("%d", &price[i]);
      //assert(price[i] == 1);
    }
    int width = 2;
    int left = 0;
    int d = 1;
    REP(i, (1 << p) - 1) {
      int right = left + width - 1;
      rangel[i] = left;
      ranger[i] = right;
      depth[i] = d;
      left += width;
      if (left == n) { d++; left = 0; width *= 2; }
    }
    //assert(width == n * 2);
    //assert(d == p + 1);
    int ans = 0;
    for (int i = (1 << p) - 1; i >= 0; i--) {
      int lmin = 100;
      FOREQ(j, rangel[i], ranger[i]) {
        lmin = min(lmin, miss[j]);
      }
      //int lmin = stree.get(rangel[i], ranger[i]);
      if (lmin < depth[i]) { ans++; }
    }
    printf("Case #%d: %d\n", test_case, ans);
  }
}
