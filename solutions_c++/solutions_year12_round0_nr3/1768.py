/******************************************************************************

 @File Name : {PROJECT_DIR}/recycle.cc

 @Creation Date : 14-04-2012

 @Last Modified : Sat 14 Apr 2012 10:07:56 PM CST

 @Created By: Zhai Yan

 @Purpose :

*******************************************************************************/
#include <set>
#include <map>
#include <vector>
#include <stdio.h>

using namespace std;

namespace {

  void dump_set(const set<int>& s)
  {
    for (auto it = s.begin(); it != s.end(); ++it)
      printf("%d ", *it);
    printf("\n");
  }


  void insert_eq_val(int val, int upper, map <int, set<int> >& eq_set, vector<bool> & used_vals)
  {
    set <int> eq_vals;
    int max_val = val;
    for (int i = 10, new_val; val % i != val; i *= 10) {
      char buf[20];
      sprintf(buf, "%d%d", val % i, val / i);
      if (val % i < i / 10) continue;
      sscanf(buf, "%d", &new_val);
      if (new_val > upper) continue;
      eq_vals.insert(new_val);
      max_val = max(max_val, new_val);
      used_vals[new_val] = true;
    }
    eq_vals.insert(val);
    //dump_set(eq_vals);
    eq_set.insert(make_pair(max_val, eq_vals));
  }

  void create_eq_set(int n, map <int, set <int> >& eq_set)
  {
    vector<bool> used_vals(n + 1, false);
    for (int i = 1; i <= n; i++) if (!used_vals[i]) {
      insert_eq_val(i, n + 1, eq_set, used_vals);
    }
  }
 
  int query_range(const map <int, set <int> >& eq_set, int a, int b)
  {
    int total = 0;
    for (auto it = eq_set.lower_bound(a);
      it != eq_set.end(); ++it) {
      int count = 0;
  //    dump_set(it->second);
      for (auto val_it = it->second.begin(); 
          val_it != it->second.end(); ++val_it) {
        if (*val_it >= a && *val_it <= b)
          count++;
      }
      total += count * (count - 1) / 2;
    }
    return total;
  }

  int solve(FILE* f, map <int, set <int> >& eq_set)
  {
    int a, b;
    scanf("%d%d", &a, &b);
    return query_range(eq_set, a, b);
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  map <int, set <int> > eq_set;
  create_eq_set(2000000, eq_set);
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: %d\n", i, solve(stdin, eq_set));
  }
  return 0;
}
