#include <iostream>
#include <vector>
#include <string>

#define sz(a) ((int)((a).size()))
using namespace std;

int testcase;
int n;
vector< pair<string, int> > lines;
int o[ 101 ], b[ 101 ];

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> n;
    lines.clear();
    for (int i = 0; i < n; ++i) {
      string type;
      int p;
      cin >> type >> p;
      lines.push_back(make_pair(type, p));
    }
    int count = 0;
    int tm = 0;
    int op = 1, bp = 1;
    while (1) {
      tm++;
      if (lines[count].first == "O") {
        int ebp = -1;
        for (int i = count+1; i < sz(lines); ++i) {
          if (lines[i].first == "B") {
            ebp = lines[i].second;
            break;
          }
        }
        if (ebp != -1) {
          if (ebp < bp) {
            bp --;
          } else if (ebp > bp) {
            bp ++;
          }
        }
        if (lines[count].second == op) {
          count++;
        } else if(lines[count].second < op) {
          op--;
        } else {
          op++;
        }
      } else {
        int eop = -1;
        for (int i = count+1; i < sz(lines); ++i) {
          if (lines[i].first == "O") {
            eop = lines[i].second;
            break;
          }
        }
        if (eop != -1) {
          if (eop < op) {
            op --;
          } else if (eop > op) {
            op ++;
          }
        }
        if (lines[count].second == bp) {
          count++;
        } else if(lines[count].second < bp) {
          bp--;
        } else {
          bp++;
        }

      }
      // cout << tm << " " << op << " " << bp << endl;
      if (count == n) {
        break;
      }
    }
    cout << "Case #" << tn << ": " << tm << endl;
  }
  return 0;
}
