#include <iostream>
#include <vector>
#include <string>
#include <list>

#include "cout.h"
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

vector<string> split(string str, int delim=' ')
{
  vector<string> result;

  const char *s = str.c_str();
  if (delim == ' ') {
    for (const char *p=s; *p; p++) {
      if (*p == delim) s++;
      else break;
    }
    if (!*s) return result;

    for (const char *p=s; *p; p++) {
      if (*p == delim) {
        if (s < p) {
          string a(s,p-s);
          result.push_back(a);
        }
        s = p + 1;
      }
    }
    if (*s) result.push_back(s);
  } else {
    for (const char *p=s; *p; p++) {
      if (*p == delim) {
        string a(s,p-s);
        result.push_back(a);
        s = p + 1;
        if (*s == '\0') result.push_back("");
      }
    }
    if (*s) result.push_back(s);
  }

  return result;
}

vector<int> map_atoi(vector<string> nums)
{
  vector<int> vals(nums.size());
  for (int i=nums.size()-1; i>=0; i--) vals[i] = atoi(nums[i].c_str());
  return vals;
}

vector<set<int> > ng, ok, vi;

//
// 二進数
//
vector<int> rebase(int x, int base)
{
  // printf("rebase(%d,%d) = ", x, base);
  vector<int> ar;
  while (x > 0) {
	ar.push_back(x % base); x /= base;
  }
  // cout << ar << endl;
  return ar;
}

bool check(int x, int base) {
  // printf("check(x=%d, base=%d)\n", x,base);
  //cout << ok[base] << " , " << ng[base] << " , " << vi[base] << endl;
  if (found(ok[base],x)) {
    // printf("ok[%d][%d] exists.\n", base,x);
    return true;
  }
  if (found(ng[base],x)) {
    // printf("ng[%d][%d] exists.\n", base,x);
    return false;
  }
  if (found(vi[base],x)) {
    // printf("vi[%d][%d] exists. loop.\n", base,x);
    return false;
  }

  vi[base].insert(x);
  
  vector<int> ar = rebase(x,base);
  int sum=0;
  tr(ar,it){
    int y = *it;
    sum += y*y;
  }
  // cout << "sum of " << ar << " = " << sum << endl;
  if (sum==1 || found(ok[base],sum)) {
    ok[base].insert(x);
    return true;
  }
  if (found(ng[base],sum)) {
    ng[base].insert(x);
    return false;
  }

  int rv = check(sum,base);
  if (rv) {
    ok[base].insert(x);
    return true;
  } else {
    ng[base].insert(x);
    return false;
  }
}

main()
{
  int T;
  string nums;
  
  ng.resize(11);
  ok.resize(11);
  vi.resize(11);
  
  rep(i,11){
    ng[i].clear();
    ok[i].clear();
    vi[i].clear();
  }

  cin >> T;
  getline(cin,nums);

  rep(t,T){
    rep(i,11){
      // ng[i].clear();
      // ok[i].clear();
      // vi[i].clear();
    }

    getline(cin,nums);
    vector<int> bases = map_atoi(split(nums));
    int bn = sz(bases);
    // cout << bases << endl << endl;

    for(int x=2;;x++){
      int ok=0;
      rep(i,bn){
        int base=bases[i];
        if (check(x,base)) {
          // printf("check(%d,%d) = true\n", x,base);
          ok++;
        }
        else {
          // printf("check(%d,%d) = false\n", x,base);
        }
      }
      if (ok==bn) {
        printf("Case #%d: %d\n", 1+t, x);
        break;
      }
    }
  }
}
