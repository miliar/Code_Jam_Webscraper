#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdlib.h>
#define max(a,b) ((a)>(b)?(a):(b)) 
#define min(a,b) ((a)<(b)?(a):(b))
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef int unit;
typedef vector<unit> multi;


const int RAD = 8;
const int DIG_MAX = 100000000;

multi mul(const multi &v1, const multi &v2) {
  multi ret;
  ull carry = 0;
  for (int i=0; i<v1.size()+v2.size()-1; i++) {
    ull t = carry;
    int mx = i - v2.size()+1;
    mx = max(0,mx);
    int mn = v1.size();
    mn = min(i+1,mn);
    for (int p=mx; p<mn; p++) {
       t += v1[p] * v2[i-p];
    }
    ull k = t / DIG_MAX;
    if (k > 0) {
      t = t - k * DIG_MAX;
      carry =k;      
    } else {
      carry = 0;
    }
    ret.push_back(t);
  }
  if (carry > 0) {
    ret.push_back(carry);
  }
  return ret;
}


multi pseudo_div(const multi &v1, const multi &v2) {
 // v1 > v2
  multi ret;
  if (v1.size() > v2.size()) {
    int aa = v2[v2.size()-1];
    if (v2.size() > 1) ++aa;
    int a = DIG_MAX / aa;
    multi upper;
    for (int i=v2.size(); i<v1.size(); i++) {
      upper.push_back(v1[i]);  
    }
    if (a <=1) return upper;
    else {
      multi b;
      b.push_back(a);
      return mul(upper, b);
    }
    
  } else {
  int cc = v2[v2.size()-1];
  if (v2.size() > 1) --cc;
    int c = v1[v1.size()-1] / cc;
    if (c == 0) c = 1;
    multi d;
    d.push_back(c);
    return d;
  }
}

multi sub(const multi &v1, const multi &v2) {
  // if ret < 0 return empty
  multi ret;
  if (v1.size() < v2.size()) return ret;
  int carry = 0;
  for (int i=0; i<v1.size(); i++) {
   int ttt;
   if (i < v2.size()) ttt = v2[i];
   else ttt = 0;
    long long t = v1[i] - ttt + carry;
    if (t < 0) {
      if (i+1 == v1.size()) {
        ret.empty(); return ret;
      }
      carry =  -1;
      t += DIG_MAX;
    } else {
      carry = 0;
    }
    ret.push_back(t);
  }

  multi ret_new;
  int mx = ret.size()-1;
  for(; mx >=0; mx--) {
    if ( ret[mx] != 0) break;
  }
  ret_new.push_back(ret[0]);
  for(int i=1; i<=mx; i++) {
    ret_new.push_back(ret[i]);
  }
  
  return ret_new;
}

bool compare (const multi &v1, const multi &v2) {
  if (v1.size() != v2.size()) {
    return v1.size() > v2.size();
  } else {
    for (int i=v1.size()-1; i>=0; i--) {
      if (v1[i] > v2[i]) return 1;
      else if (v1[i] < v2[i]) return 0;
    }
  }
  return 1;
}

bool equal (const multi &v1, const multi &v2) {
  if (v1.size() != v2.size()) {
    return 0;
  } else {
    for (int i=v1.size()-1; i>=0; i--) {
      if (v1[i] != v2[i]) return 0;
    }
  }
  return 1;
}

bool is_empty(multi &v) {
  return (v.size() ==1 && v[0] == 0);
}


multi gcd(multi &v1, multi &v2) {
  // v1 > v2
  multi ret = sub(v1, mul(pseudo_div(v1, v2), v2));
  if (is_empty(ret)) return v2;
  else if (compare(ret, v2)) return gcd(ret, v2);
  
  return gcd(v2, ret);
}

void print(const multi &v) {
  int first = v[v.size()-1];
  if (first == 0 && v.size() > 1) {
    cout << "## IL" << endl;
  }
  cout << first;
  for (int i=v.size()-2; i>=0; i--) {
    ull u = v[i];
    for (ull t = DIG_MAX/10; t != 0; t = t / 10) {
      ull s = u / t;
      cout << s;
      u -= s * t;
    }
  }
  cout << endl;
}

int main(void) {
  int c, n;
  cin >> c;
  for (int i=0; i<c; i++) {
    cin >> n;
    vector<multi> dat, sb;
    for (int j=0; j<n; j++) {
      string s;
      cin >> s;
      multi m;
      int sz = s.size();
      while (sz > 0) {
        int rr = sz-RAD;
        int r = RAD;
        if (rr < 0) {
          r += rr;
          rr = 0;
        }
        m.push_back((unit)(atoi(s.substr(rr, r).c_str())));
        sz -= RAD;
      }
      dat.push_back(m);
    }
    
    sort(dat.begin(), dat.end(), compare);
    
    for (int k=0; k<n-1; k++) {
      if (equal(dat[k],dat[k+1])) continue;
      multi sbb = sub(dat[k], dat[k+1]);
      sb.push_back(sbb);
    }
    sort(sb.begin(), sb.end(), compare);
    
    multi cand = sb[0];
    for (int k=1; k<sb.size(); k++) {
      if (equal(cand,sb[k])) continue;
      cand = gcd(cand, sb[k]);
    }
    
    multi recent = dat[dat.size()-1];
    while(! compare(cand, recent)) {
      multi pd = pseudo_div(recent, cand);
      multi mt = mul(pd, cand);
      recent = sub(recent, mt);
    }
    multi result;
    if (is_empty(recent)) result = recent;
    else result = sub(cand, recent);
    cout << "Case #" << (i+1) << ": " ;
    print(result);
  }
  return 0;
}