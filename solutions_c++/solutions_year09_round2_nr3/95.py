#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> P;

typedef pair<pair<int, int>, int> Vertex;
typedef int Weight;
struct Edge {
  Vertex src;
  Vertex dest;
  Weight weight;
  string op;
  Edge() {}
  Edge(const Vertex& src, const Vertex& dest, Weight weight, string op) :
    src(src), dest(dest), weight(weight), op(op) {}
};

typedef vector<Edge> Edges;
typedef map<Vertex, Edges> Graph;
typedef map<Vertex, pair<Vertex, Weight> > Potential;

// for MST / Dijkstra
bool operator>(const Edge& lhs, const Edge& rhs) {
  if (lhs.weight != rhs.weight) { return lhs.weight > rhs.weight; }
  if (lhs.src != rhs.src) { lhs.src > rhs.src; }
  if (lhs.dest != rhs.dest) { lhs.dest > rhs.dest; }
  return lhs.op > rhs.op;
}

string dijkstra(Graph& g, const Vertex& startV, int x, int cutLen) {
  Potential pot;
  priority_queue<Edge, Edges, greater<Edge> > Q;

  string s(1, (char)(startV.second + '0'));
  Q.push(Edge(startV, startV, 0, s));

  if (startV.second == x) {
    return s;
  }

  while (!Q.empty()) {
    Edge edge = Q.top(); Q.pop();
    Vertex p = edge.dest;
    Weight curr = edge.weight;

    if (pot.count(p)) { continue; } // already visited.
    pot[p] = make_pair(edge.src, curr);

    Edges& es = g[p];
    for (int i = 0; i < es.size(); ++i) {
      Edge& e = es[i];
      if (pot.count(e.dest)) { continue; } // already visited.
      string st = edge.op + e.op;
      if (cutLen >= 0 && st.length() > cutLen) { continue; }
      Q.push(Edge(e.src, e.dest, curr + e.weight, st));
      //cout << e.op + edge.op << " : "<< e.dest.second << endl;
      if (e.dest.second == x) { // found!!!
        return st;
      }
    }
  }

  return "";
}

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, 1, -1, 0};

void createGraph(Graph& g, int W, const vector<string>& f)
{
  const int RANGE = 200;

  for (int h = 0; h < W; ++h) {
    for (int w = 0; w < W; ++w) {
      if (f[h][w] == '+' || f[h][w] == '-') { continue; }
      //cout << "(" << h << ',' << w << ")  ";
      for (int r = -RANGE; r <= RANGE; ++r) {
        Vertex s = make_pair(make_pair(h, w), r);

        int sign = 1, x = 0; string op = "  ";
        for (int d1 = 0; d1 < 4; ++d1) {
          int h1 = h + dy[d1], w1 = w + dx[d1];
          if (h1 < 0 || W <= h1 || w1 < 0 || W <= w1) { continue; }
          assert(f[h1][w1] == '+' || f[h1][w1] == '-');
          if (f[h1][w1] == '+') { sign = 1; } else { sign = -1; }
          op[0] = f[h1][w1];
          for (int d2 = 0; d2 < 4; ++d2) {
            int h2 = h1 + dy[d2], w2 = w1 + dx[d2];
            if (h2 < 0 || W <= h2 || w2 < 0 || W <= w2) { continue; }
            assert('0' <= f[h2][w2] && f[h2][w2] <= '9');
            x = f[h2][w2] - '0';
            op[1] = f[h2][w2];
            Vertex d = make_pair(make_pair(h2, w2), r + sign * x);
            g[s].push_back(Edge(s, d, 1, op));
          }
        }
      }
    }
  }
}

string solve(int W, const vector<string>& f, Graph& g, int x)
{
  string answer = "";
  int cutLen = -1;
  // graph created.
  for (int h = 0; h < W; ++h) {
    for (int w = 0; w < W; ++w) {
      if (f[h][w] == '+' || f[h][w] == '-') { continue; }
      Vertex startV = make_pair(make_pair(h, w), f[h][w] - '0');
      string goal = dijkstra(g, startV, x, cutLen);
      //      cout << goal << endl;
      if (goal == "") { continue; }
      if (answer == "" || (goal.length() < answer.length()) || (goal.length() == answer.length() && goal < answer)) {
        answer = goal;
        cutLen = answer.length();
      }
    }
  }

  if (answer == "") {
    throw "NOT FOUND";
  }
  return answer;
}

int main(void)
{
  int T; cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << (i+1) << ":" << endl;

    int W, Q; cin >> W >> Q;
    vector<string> f(W);
    string str; getline(cin, str);
    for (int w = 0; w < W; ++w) {
      getline(cin, f[w]);
    }

    Graph g;
    createGraph(g, W, f);

    for (int q = 0; q < Q; ++q) {
      int x; cin >> x;
      //cout << x << endl;
      cout << solve(W, f, g, x) << endl;
    }
  }

    return 0;
}

