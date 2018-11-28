#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
#include <map>
#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int maxpoint;
int ansid;

vector<string> words;
vector<int> lmasks;
string letters;

struct Task {
  Task() : lid(0), points(0) {}
  void process() const;

  int lid;
  int points;
  vector<int> ids;
};

queue<Task> q;

void Task::process() const {
  if (ids.size() == 1) {
    if (points > maxpoint || (points == maxpoint && ids[0] < ansid)) {
      maxpoint = points;
      ansid = ids[0];
    }
    return;
  }

  int mask = 0;
  for (int i = 0; i < ids.size(); ++i) {
    mask |= lmasks[ids[i]];
  }
  int k = lid;
  while (k < 26 && !(mask & (1 << (letters[k]-'a')))) {
    k++;
  }
  if (k >= 26) {
    cerr << "impossible" << endl;
    return;
  }
  char ch = letters[k];
  map<int, Task> m;
  for (int i = 0; i < ids.size(); ++i) {
    int h = 0;
    const string& w = words[ids[i]];
    for (int j = 0; j < w.size(); ++j) {
      if (w[j] == ch) {
        h |= 1 << j;
      }
    }
    Task& t = m[h];
    t.ids.push_back(ids[i]);
  }
  for (map<int, Task>::iterator it = m.begin(); it != m.end(); ++it) {
    Task& t = it->second;
    if (it->first == 0) {
      t.points = points + 1;
    } else {
      t.points = points;
    }
    t.lid = k+1;
    q.push(t);
  }
}

void processQ() {
  while (!q.empty()) {
    Task t = q.front();
    q.pop();
    t.process();
  }
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          int n, m;
          fin >> n >> m;
          words.clear();
          lmasks.clear();
          for (int i = 0; i < n; ++i) {
            string s;
            fin >> s;
            words.push_back(s);
            int mask = 0;
            for (int j = 0; j < s.length(); ++j) {
              mask |= 1 << (s[j]-'a');
            }
            lmasks.push_back(mask);
          }

          fout << "Case #" << tind << ":";
          for (int i = 0; i < m; ++i) {
            fin >> letters;

            maxpoint = 0;
            ansid = 0;

            Task tasks[11];
            for (int j = 0; j < words.size(); ++j) {
              int l = words[j].length();
              tasks[l].ids.push_back(j);
            }

            q = queue<Task>();
            for (int j = 1; j <= 10; ++j) {
              if (!tasks[j].ids.empty()) {
                q.push(tasks[j]);
              }
            }

            processQ();

            fout << ' ' << words[ansid];
          }
          fout << endl;
	}
	return 0;
}
