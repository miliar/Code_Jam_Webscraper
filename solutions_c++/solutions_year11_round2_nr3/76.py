#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

int n;
vector<vector<int> > adj;
vector<vector<int> > rooms;
int best;
vector<int> output;

void add_edge(int a, int b) {
  adj[a].push_back(b);
  adj[b].push_back(a);
}

int mod(int a, int b) {
  return (a%b + b) % b;
}

const int MAXC = 5;
void rek(int v, vector<int> &colour, vector<int> &cnt) {
  if (v == n) {
    int sum = 0;
    for (int c=0; c<MAXC; ++c) {
      sum += cnt[c] > 0;
    }
    if (sum > best) {
      bool ok = true;
      vector<int> room(MAXC, 0);
      for (int i=0; ok && i<(int)rooms.size(); ++i) {
        fill(room.begin(), room.end(), 0);
        for (int j=0; j<(int)rooms[i].size(); ++j) {
          room[colour[rooms[i][j]]] = 1;
        }
        for (int c=0; c<MAXC; ++c) {
          ok &= (room[c] > 0) == (cnt[c] > 0);
        }
      }
      if (ok) {
        best = sum;
        output = colour;
      }
    }
    return;
  }

  for (int c=0; c<MAXC; ++c) {
    colour[v] = c;
    cnt[c]++;
    rek(v+1, colour, cnt);
    cnt[c]--;
  }
}

vector<int> findroom(int n, int a, int b, set<pair<int, int> > &used_edges) {
  int start = a;
  vector<int> ret;
  do {
    ret.push_back(b);
    used_edges.insert(make_pair(min(a, b), max(a, b)));
    int next = adj[b][0];
    for (int i=1; i<(int)adj[b].size(); ++i) {
      if (mod(adj[b][i]-a, n) > mod(next-a, n)) {
        next = adj[b][i];
      }
    }
    a = b; b = next;
  } while (start != a);
  return ret;
}

int main() {
  cin.sync_with_stdio(0);
  int CASES; cin >> CASES;

  for (int tt=1; tt<=CASES; ++tt) {
    int m; cin >> n >> m;
    vector<int> a(m), b(m);
    for (int i=0; i<m; ++i) cin >> a[i];
    for (int i=0; i<m; ++i) cin >> b[i];

    adj.clear();
    adj.resize(n);
    for (int i=0; i<n; ++i) add_edge(i, (i+1)%n);
    for (int i=0; i<m; ++i) add_edge(a[i]-1, b[i]-1);

    set<pair<int, int> > used_edges;
    rooms.clear();
    for (int i=0; i<n; ++i) {
      int a = i, b = (i+1)%n;
      if (used_edges.find(make_pair(min(a, b), max(a, b))) != used_edges.end()) {
        continue;
      }
      rooms.push_back(findroom(n, a, b, used_edges));
    }

    best = 0;
    output.resize(n);
    if (m == 0) {
      best = n;
      for (int i=0; i<n; ++i) {
        output[i] = i;
      }
    } else {
      vector<int> colour(n, 0), cnt(MAXC, 0);
      cnt[0] = 1;
      rek(1, colour, cnt);
    }

    printf("Case #%d: %d\n", tt, best);
    for (int i=0; i<n; ++i) {
      if (i > 0) printf(" ");
      printf("%d", output[i]+1);
    }
    printf("\n");
  }

  return 0;
}
