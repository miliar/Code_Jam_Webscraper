#include <cstdio>
#include <map>
#include <list>

using namespace std;

struct Combine {
  char a, b;
};

struct Compare {
  bool operator() (const Combine& a, const Combine& b) const {
    return a.a < b.a || a.a == b.a && a.b < b.b;
  }
};

int ele_no[128];
map<Combine, char, Compare> mp;
list<char> oppo_ls[128];
list<char> ele_ls;
list<char>::iterator it;

int main() {
  Combine comb;
  char ca, cb, cc;
  int case_no, c, d, n, t;

  scanf("%d", &t);
  for (case_no = 1; case_no <= t; case_no++) {
    scanf("%d", &c);
    getchar();
    
    memset(ele_no, 0, sizeof ele_no);
    mp.clear();
    ele_ls.clear();
    for (int i = 0; i < 128; i++)
      oppo_ls[i].clear();

    for (int i = 0; i < c; i++) {
      ca = getchar();
      cb = getchar();
      cc = getchar();

      if (ca < cb) {
        comb.a = ca;
        comb.b = cb;
      }
      else {
        comb.a = cb;
        comb.b = ca;
      }

      mp[comb] = cc;
    }
    
    scanf("%d", &d);
    getchar();
    for (int i = 0; i < d; i++) {
      ca = getchar();
      cb = getchar();
      oppo_ls[ca].push_back(cb);
      oppo_ls[cb].push_back(ca);
    }
    
    scanf("%d", &n);
    getchar();
    for (int i = 0; i < n; i++) {
      cb = getchar();
      if (!ele_ls.empty()) {
        ca = ele_ls.back();
        if (ca < cb) {
          comb.a = ca;
          comb.b = cb;
        }
        else {
          comb.a = cb;
          comb.b = ca;
        }

        if (cc = mp[comb]) {
          // combine successfully
          ele_ls.pop_back();
          ele_ls.push_back(cc);
          ele_no[ca]--;
          ele_no[cc]++;
        }
        else {
          // check oppo
          ele_ls.push_back(cb);
          ele_no[cb]++;
          for (it = oppo_ls[cb].begin(); it != oppo_ls[cb].end(); it++)
            if (ele_no[*it]) {
              ele_ls.clear();
              memset(ele_no, 0, sizeof ele_no);
              break;
            }
        }
      }
      else {
        ele_ls.push_back(cb);
        ele_no[cb]++;
      }
    }

    printf("Case #%d: [", case_no);
    it = ele_ls.begin();
    if (it != ele_ls.end()) {
      putchar(*it);
      for (it++; it != ele_ls.end(); it++) {
        putchar(',');
        putchar(' ');
        putchar(*it);
      }
    }
    puts("]");
  }

  return 0;
}
