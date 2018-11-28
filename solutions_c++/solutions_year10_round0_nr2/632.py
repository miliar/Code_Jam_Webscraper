int N;
const int debug = 0;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

// strings store numbers
// most significant digit is in string[0], least significant in string[n]


// a>b --> 1
// a=b --> 0
// a<b --> -1
int cmp(const string&a, const string& b) {
  if (a.size() > b.size()) return 1;
  if (a.size() < b.size()) return -1;
  for (int i=0; i<a.size(); i++) {
    if (a[i] > b[i]) return 1;
    if (a[i] < b[i]) return -1;
  }
  return 0;
}

// if a < b*10**shift 
// then ret false
// else a -= b*10**shift, ret true
bool sub_shift(string& a, const string& b, int shift) {
  if (debug)
  fprintf(stderr,"sub_shift(%s,%s,%d)) -- BEGIN\n",
    a.c_str(), b.c_str(), shift);
  assert(a.size() > 0);
  assert(a.size() == 1 || a[0]!='0');
  assert(b.size() > 0);
  assert(b.size() == 1 || b[0]!='0');
  assert(shift>=0);
  if (a.size() < b.size() + shift) return false;
  string res(a);
  int carry = 0;
  { int i, bi, ai;
  for (i=0, bi=b.size()-1, ai=a.size()-1-shift; 
       i<b.size() && ai>=0; 
       i++,bi--,ai--) 
  {
    int v = a[ai] - b[bi] - carry;
    carry = 0;
    if (v<0) v+=10, carry = 1;
    res[ai] = '0' + v;
    #if 0
    if (debug)
    fprintf(stderr,"a[%d]=%c  b[%d]=%c, a-b=%d, carry=%d\n",
      ai,a[ai],bi,b[bi],v,carry);
    #endif
  }
  for (;carry && ai>=0; ai--) {
    int v = a[ai] - carry;
    carry = 0;
    if (v<'0') v+=10, carry = 1;
    res[ai] = v;
  }
  }
  if (carry) return false; // a<b*10**shift
  // Skip leading zeros
  int skip;
  for (skip=0; skip<res.size() && res[skip] == '0'; skip++);
  if (skip==res.size()) {
    // a==b*10**shift
    skip--; // don't skip the final '0'
  }
  if (debug)
  cerr << "a="<<a<<endl;
  if (debug)
  cerr << "res="<<res<<endl;
  a = string(res,skip);
  return true;
}

bool sub(string& a, const string& b) {
  return sub_shift(a,b,0);
}

void sub_abs(string& a, string b) {
  if (sub(a,b)) return;
  swap(a,b);
  sub(a,b);
}

// t = t modulus gcd
void mod(string& t, const string& gcd) {
  assert(gcd.size() > 0 && gcd[0] != 0);
  for (int shift = t.size() - gcd.size() ; shift >= 0; shift --) {
    for (int ss,i=0; ss = sub_shift(t,gcd,shift) && i<11; i++) {
      if (i>=10) {
        fprintf(stderr,"sub_shift(%s,%s,%d))==%s\n",
          t.c_str(), gcd.c_str(), shift, (ss?"TRUE":"FALSE"));
      }
      assert(i<10);
      assert(gcd.size() > 0 && gcd[0] != 0);
      if (debug)
      fprintf(stderr,"sub_shift(%s,%s,%d))==%s\n",
        t.c_str(), gcd.c_str(), shift, (ss?"TRUE":"FALSE"));
    }
  }
}

string find_gcd(string a, string b) {
  if (debug)
  fprintf(stderr,"   gcd(%s,%s)\n",a.c_str(),b.c_str());
  assert(cmp(a,"0")!=0);
  assert(cmp(b,"0")!=0);
  while (1) {
    mod(a,b);
    if (cmp(a,"0")==0) return b;
    swap(a,b);
  }
}

int main()
{
  // Input
  scanf("%d\n",&N);
  if (debug)
  fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    if (debug)
    fprintf(stderr,"Case #%d: \n",x);

    string str;
    getline(cin,str);
    stringstream ss(str);
    int y;
    ss >> y;
    string base;
    ss >> base;
    string min_past(base);
    string gcd;
    if (debug)
    fprintf(stderr," %d/%d:%s\n",1,y,base.c_str());
    for (int i=1; i<y; i++) {
      string t;
      ss >> t;
      if (debug)
      fprintf(stderr," %d/%d:%s\n",i+1,y,t.c_str());
      if (cmp(t,min_past)<0) min_past = t;
      sub_abs(t,base);
      // t is now relative to base
      if (debug)
      fprintf(stderr,"   t=%s\n",t.c_str());
      if (cmp(t,"0")==0) continue;
      // remember first real diff (!=0)
      if (gcd.size() == 0) { gcd=t; continue;}
      // find gcd(gcd,t)
      if (cmp(t,"0")!=0) gcd = find_gcd(t,gcd);

      if (debug)
      fprintf(stderr,"   gcd=%s\n",gcd.c_str());
    }
    
    // So, we found gcd, now subtract min_pass
    if (debug) cerr << "gcd="<<gcd<< endl;
    if (debug) cerr << "min_past="<<min_past<<endl;
    string has_passed(min_past);
    mod(has_passed,gcd);
    if (debug) cerr << "min_past mod gcd = "<<has_passed<<endl;
    string to_go(gcd);
    if (cmp(has_passed,"0")==0) {
      // has_passed % gcd == 0  -> The apocalypse is now (maybe again)
      to_go = "0";
    }
    else {
      assert(sub(to_go,has_passed));
    }
    printf("Case #%d: %s\n",x,to_go.c_str());
  }
  return 0;
}
