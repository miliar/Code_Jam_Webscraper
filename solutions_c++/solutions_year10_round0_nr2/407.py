#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cassert>
using namespace std;
#define psb push_back
#define mpr make_pair
#define infinity 1000000010
#define mineps 1e-8
#define sqr(x) ((x)*(x))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))
#define LL long long
#define UC unsigned long
#define UI unsigned int
#define pi 3.14159265358979323846 
inline int cmp(double x) {
  if (fabs(x) < mineps) return 0;
  else if (x < 0) return -1;
  else return 1;       
}
//////////////////////////////////////////////
//Start here

class BigInteger {
      
  public:      
    vector<int> dat;
    
    BigInteger() {}
    BigInteger(string str) {
      dat.clear();
      for(int i = 0; i < str.size(); i++)  dat.psb(str[i]-'0');                  
    }
    string output() {
      string ret; 
      for(int i = 0; i < dat.size(); i++)  ret.psb(dat[i]+'0');
      return ret;       
    }
    bool empty() {return dat.empty(); }
    void clear() {dat.clear(); }
    int size() {return dat.size(); }
    void push_back(int x) {assert(0<=x&&x<10); dat.psb(x); }
    
    int operator[] (int p) {assert(0<=p && p<dat.size()); return dat[p]; }
    friend bool operator< (BigInteger a, BigInteger b);
    friend BigInteger operator- (BigInteger a, BigInteger b);
    friend BigInteger operator% (BigInteger a, BigInteger b);
    friend BigInteger operator+ (BigInteger a, BigInteger b);
      
};

int T, n;
vector<BigInteger> a;
BigInteger maxT, ans;

char tstr[300];

bool operator< (BigInteger a, BigInteger b) {
  if (a.size() < b.size()) return true;
  else if (a.size() > b.size()) return false;
  else {
    for(int i = 0; i < a.size(); i++) 
      if (a[i] < b[i]) return true;
      else if (a[i] > b[i]) return false;     
    return false;
  }
}

BigInteger operator- (BigInteger a, BigInteger b) { //must satisfy a >= b
  string str;
  int p1 = a.size()-1, p2 = b.size()-1;
  int delta = 0;
  while (p1 >= 0 && p2 >= 0) {
    int t = a[p1] - delta - b[p2];
    if (t >= 0) delta = 0; else {delta = 1; t += 10; };
    str.psb(t+'0');
    p1--; p2--;
  }
  assert(p2 < 0);
  while (p1 >= 0) {
    int t = a[p1] - delta;
    if (t >= 0) delta = 0; else {delta = 1; t += 10; };
    str.psb(t+'0'); 
    p1--;      
  }
  
  int p = str.length()-1;
  while (p >= 0 && str[p] == '0') p --;
  BigInteger ret;
  for(int i = p; i >= 0; i--) ret.psb(str[i]-'0');
  if (ret.empty()) ret.psb(0);
  return ret;
}

BigInteger operator+ (BigInteger a, BigInteger b) {
  string str;
  int p1 = a.size()-1, p2 = b.size()-1;
  int delta = 0;
  while (p1 >= 0 && p2 >= 0) {
    int t = a[p1] + b[p2] + delta;
    if (t < 10) delta = 0; else {t -= 10; delta = 1; };
    str.psb(t+'0');
    p1 --; p2 --;
  }
  while (p1 >= 0) {
    int t = a[p1] + delta;
    if (t < 10) delta = 0; else {t -= 10; delta = 1; };
    str.psb(t+'0');
    p1--;   
  }
  while (p2 >= 0) {
    int t = b[p2] + delta;
    if (t < 10) delta = 0; else {t -= 10; delta = 1; };
    str.psb(t+'0');
    p2--;      
  }
  
  if (delta == 1) str.psb('1');
  
  int p = str.length()-1;
  while (p >= 0 && str[p] == '0') p --;
  BigInteger ret;
  for(int i = p; i >= 0; i--) ret.psb(str[i]-'0');
  if (ret.empty()) ret.psb(0);
  return ret;    
}

BigInteger s[100];
int sp;

BigInteger operator% (BigInteger a, BigInteger b) {
           
  //printf("%s mod %s = ", a.output().c_str(), b.output().c_str());
           
  sp = 0;
  BigInteger ret = a;
  s[sp] = b;
  while (!(a < s[sp])) {
    sp ++;
    s[sp] = s[sp-1] + s[sp-1];
  }
  
  for(int i = sp; i >= 0; i--)
    if (!(ret < s[i])) ret = ret - s[i];
    
  //puts(ret.output().c_str());
    
  return ret;      
           
}

BigInteger gcd(BigInteger a, BigInteger b) { //must satisfy a > b
  BigInteger now = a % b;
  if (now.size() == 1 && now[0] == 0) return b;
  else return gcd(b, now);
}

int main() {

  freopen("B-small.in", "rt", stdin);
  freopen("B-small.out", "wt", stdout);
    
  scanf("%d\n", &T);
  for(int tn = 1; tn <= T; tn++) {
          
    memset(tstr,0,sizeof(tstr));
    gets(tstr);
    string str = tstr;
    int p = str.find_first_of(" ");
    sscanf(str.substr(0, p).c_str(), "%d", &n);
    str.erase(0, p+1);
    
    a.clear();
    str += " ";
    for(int i = 0; i < n; i++) {
      int p = str.find_first_of(" ");
      BigInteger now(str.substr(0, p));
      str.erase(0, p+1);
      a.psb(now);        
    }  
    
    //for(int i = 0; i < a.size(); i++)  puts(a[i].output().c_str()); 
    
    maxT.clear();
    for(int i = 0; i < n; i++)
      for(int j = 0; j < n; j++)
        if (i != j && a[i] < a[j]) {
          BigInteger now = a[j] - a[i];
          if (maxT.empty()) maxT = now; 
          else maxT = (maxT < now)? gcd(now, maxT) : gcd(maxT, now);;
        }
        
    BigInteger now = a[0] % maxT;
    if (!(now.size()==1 && now[0]==0)) now = maxT - now;
    str = now.output();
    printf("Case #%d: %s\n", tn, str.c_str());        
          
  }
  
  return 0;
  
}
