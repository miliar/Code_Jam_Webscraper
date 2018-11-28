#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <set>
using namespace std;

typedef vector<string> solution;

class Node {
public:
  string tail;
  int pos;
  int cost;

  Node (string t, int p, int c)
    :tail(t), pos(p), cost(c) {}

  bool operator<(const Node &lh) const {
    return lh.cost < cost;
  }
};

string tail(solution s) {
  return *(s.end()-1);
}

int main()
{
  int n,k,p;
  cin>>n;
  for(int m=1;m<=n;m++) {
    cin>>k;
    cin.ignore();
    map<string, int> freq;
    set<string> engine;

    int f = 0;
    for(int i=0;i<k;i++) {
      string s;
      getline(cin,s);
      freq.insert(make_pair<string,int>(s,f++));
      engine.insert(s);
    }

    //    cout << "engine" << engine.size() << ", " << flush;

    vector<string> v;
    cin>>p;
    cin.ignore();
    for(int i=0;i<p;i++) {
      string s;
      getline(cin,s);
      v.push_back(s);
    }

    //    cout << "querry" << v.size() << ": " << flush;

    // PFS
    bool table[ v.size() ][ engine.size() ];
    for(int i=0;i<(int)v.size();i++)
      for (int j=0;j<(int)engine.size();j++) {
        table[i][j] = false;
      }

    priority_queue<Node> Q;

    for(set<string>::iterator i = engine.begin();
        i != engine.end();
        i++) {
      Q.push( Node(*i, 0, 0) );
    }

    while(!Q.empty()) {
      Node n = Q.top(); Q.pop();
      int l  = n.pos;
      while(l!=(int)v.size()) {
        if (v[l] == n.tail) {
          for(set<string>::iterator it = engine.begin();
              it != engine.end();
              it++) {
            if (*it != n.tail) {
              if (table[l][ freq[*it] ]) continue;

              table[l][ freq[*it] ] = true;
              Q.push(Node(*it, l, n.cost+1));
            }
          }

          break;
        }
        l++;

      }

      if (l==(int)v.size()) {
        cout << "Case #"<<m<< ": " << n.cost << endl;
        break;
      }
    }

    //    cout << endl;
  }
}
