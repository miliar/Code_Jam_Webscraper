#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<utility>
#include<queue>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<climits>

using namespace std;

#define FOR(i,s,n) for (int i=(int)(s); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

#define A2B 0
#define B2A 1

#define ARRIVE 0
#define LEAVE  1

struct node_t {
  int from, start, hour, min;
  node_t(string t, int f, int s) : from(f), start(s) {
    sscanf(t.c_str(), "%d:%d", &hour, &min);
  }
  bool operator<(const node_t& rhs) const {
    if (hour != rhs.hour)
      return hour < rhs.hour;
    else if (min != rhs.min)
      return min < rhs.min;
    else if (start != rhs.start)
      return start < rhs.start;
    else
      return from < rhs.from;
  }
};

int main()
{
  int N;
  cin >> N;
  REP(i, N) {
    int T, NA, NB;
    cin >> T >> NA >> NB;
    vector<node_t> nodes;
    REP(j, NA) {
      string from, to;
      cin >> from >> to;
      nodes.PB(node_t(from, A2B, LEAVE));
      nodes.PB(node_t(to, A2B, ARRIVE));
    }
    REP(j, NB) {
      string from, to;
      cin >> from >> to;
      nodes.PB(node_t(from, B2A, LEAVE));
      nodes.PB(node_t(to, B2A, ARRIVE));
    }
    sort(ALL(nodes));

    int aneed(0), astay(0), bneed(0), bstay(0);
    int aprevh(-1), aprevm(-1), bprevh(-1), bprevm(-1);
    queue<pair<int, int> > aprev, bprev;
    const char *FROM[] = {"A->B", "B->A"};
    const char *START[] = { "Arrive", "Leave"};
    REP(j, (NA+NB)*2) {
      const node_t& cur(nodes[j]);
      
      // printf("%02d:%02d %s %s\n",
      //        cur.hour, cur.min, FROM[cur.from], START[cur.start]);
      if (cur.from == A2B) { // A to B
        if (cur.start == ARRIVE) { // train arrives to B.
          bprev.push(MP(cur.hour, cur.min));
          bstay++;
        } else if (astay &&
                   (aprev.empty() || 
                    (cur.hour - aprev.front().first)*60 + (cur.min - aprev.front().second) >= T)) {
          // train leaves from A.
          // first
          astay--;
          aprev.pop();
        } else {
          // train leaves from A.
          // first time or it has not passed T min from prev or 
          // no train is ready.
          aneed++;
        }
      } else if (cur.from == B2A) { // B to A
        if (cur.start == ARRIVE) { // train arrives to A.
          aprev.push(MP(cur.hour, cur.min));
          astay++;
        } else if (bstay &&
                   (bprev.empty() || 
                    (cur.hour - bprev.front().first)*60 + (cur.min - bprev.front().second) >= T)) {
          // train leaves from A.
          bprev.pop();
          bstay--;
        } else {
          // train leaves from A.
          // first time or it has not passed T min from prev or 
          // no train is ready.
          bneed++;
        }
      }
      // cout << aneed << " " << astay << " "
      //      << bneed << " " << bstay << endl;
    }
    cout << "Case #" << i+1 << ": " << aneed << " " << bneed << endl;
  }
  return 0;
}

