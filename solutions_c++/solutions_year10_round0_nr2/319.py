#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <assert.h>
#include <bitset>
#include <functional>
#include <utility>
#include <iomanip>
#include <cctype>
//#include <ext/hash_set>
//#include <ext/hash_map>

using namespace std;
// using namespace __gnu_cxx;


#define MAX 200

char read_char(ifstream& in) {char c; in >> c; in.unget();return c;}

void add(int a[MAX], int b[MAX]) {
  int r=0;
  for (int i=0; i<MAX; i++) {
    
    int aa =a[i];
    a[i] = (aa+b[i]+r)%2;
    
    if(aa+b[i]+r>=2) r = 0; else r = 1;
  }
}

void sub(int a[MAX], int b[MAX]) {
  int r=0;
  for (int i=0; i<MAX; i++) {
    
    int aa=a[i];
    if(aa%2 == (b[i]+r)%2) a[i] = 0; else a[i] = 1;
    
    if(b[i]+r>aa) r = 1; else r = 0;
  }
}

void sub_(int a[MAX], int b[MAX], int c[MAX]) {
  int r=0;
  for (int i=0; i<MAX; i++) {
    
    if(a[i]%2 == (b[i]+r)%2) c[i] = 0; else c[i] = 1;
    
    if(b[i]+r>a[i]) r = 1; else r = 0;
  }
}

int equal(int a[MAX], int b[MAX]) {
  for (int i=MAX-1; i>=0; i--) {
    if (a[i]<b[i]) return 1;
    if (a[i]>b[i]) return -1;
  }
  return 0;
}

bool even(int a[MAX]) {
  return a[0]==0;
}

void div2(int a[MAX]) {
  for (int i=0; i<MAX-1; i++)
    a[i]=a[i+1];
  a[MAX-1] = 0;
}

void mul2(int a[MAX]) {
  for (int i=MAX-1; i>=1; i--)
    a[i] = a[i-1];
  a[0] = 0;
}

void copy(int a[MAX], int b[MAX]) {
  for (int i=0; i<MAX; i++)
    a[i] = b[i];
}

void pgcd(int a[MAX], int b[MAX], int c[MAX]) {
  
  if (equal(a,b)==0) {
    copy(c, a);
    return;
  }
  
  if (even(a) && even(b)) {
    div2(a);
    div2(b);
    pgcd(a, b, c);
    mul2(c);
    return;
  }

  if (even(a)) {
    div2(a);
    pgcd(a, b, c);
    return;
  }

  if (even(b)) {
    div2(b);
    pgcd(a, b, c);
    return;
  }

  if (equal(a,b)==-1) {
    sub(a,b);
    div2(a);
    pgcd(a,b,c);
    return;
  }

  sub(b, a);
  div2(b);
  pgcd(a,b,c);
  return;
}

void mul2k(int a[MAX], int k) {

  for (int i=MAX-1; i>=k; i--) a[i]=a[i-k];

  for (int i=0; i<k; i++) a[i]=0;
}

void F(int b[MAX], int r[MAX], int k) {  

  if (k==0)
    return;
  
  int mul[MAX];
  copy(mul, b);
  mul2k(mul, k-1);
  
  if (equal(r, mul)==1) {
    F(b, r, k-1);
    return;
  }
  
  int subb[MAX];  
  sub_(r, mul, subb);
  copy(r, subb);

  F(b, r, k-1);
  return;
}

void reste(int a[MAX], int b[MAX], int rr[MAX]) {
  int bb[MAX]; 
  copy(bb, b);
  copy(rr, a);
  
  F(bb, rr, MAX);
  return;
}

void div2_base10 (int a[55]) { 
  a[0]/=2;
  for (int i=1; i<55; i++) {
    if (a[i]%2==1)
      a[i-1]+=5;
    a[i]/=2;
  }
}

void mul2_base10 (int a[55]) {
  int r=0;
  for (int i=0; i<55; i++) {
    int s = r+2*a[i];
    if (s>=10) r=1; else r=0;
    a[i]=s%10;
  }
}

bool zero_base10(int a[55]) {
  for (int i=0; i<55; i++) {
    if(a[i]!=0)
      return false;
  }
  return true;
}

bool zero_base2(int a[MAX]) {
  for (int i=0; i<MAX; i++) {
    if(a[i]!=0)
      return false;
  }
  return true;
}

void toBinary(int a[55], int c[MAX]) {// unité=a[0]
  int b[MAX];
  for (int i=0; i<MAX; i++) b[i]=0;
  for (int i=0; i<MAX; i++) c[i]=0;

  int n=0;
  while(!zero_base10(a)) {
    mul2(b);
    if (a[0]%2==1) {
      b[0]=1;
    }
    div2_base10(a);
    n++;
  }

  for (int i=0; i<n; i++) {
    c[i]=b[n-1-i];
  }
}

void toDec(int a[MAX], int b[55]) {

  for (int i=0; i<55; i++) b[i]=0;
  for (int i=MAX-1; i>=0; i--) {
    mul2_base10(b);
    if (a[i]==1) b[0]++;
  }
}


int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    
    // recuperation de l'input et conversion en binaire
    int n;
    in >> n;
    read_char(in); // one space
    
    int tab[n][55];
    int t[n][MAX];
    for (int i=0; i<n; i++) for (int j=0; j<55; j++) tab[i][j]=0;

    for(int i=0; i<n; i++) {    
      string s;
      in >> s;
      int l = s.length();
      for (int j=l-1; j>=0; j--) {
	tab[i][l-1-j]=(int) (s[j]-'0');
      } 

      toBinary(tab[i], t[i]);

    }

   
    // Calcul
    int d1[MAX];
    int d2[MAX];

    int I, J;
    bool bb=true;
    for (I=0; bb && I<n; I++) {
      for (J=I+1; bb && J<n; J++) {
	if(equal(t[I],t[J])!=0)
	  bb=false;
      }
    }I--;J--; assert(equal(t[I],t[J])!=0);
    if (equal(t[I], t[J])==1)
      sub_(t[J], t[I], d1);
    else 
      sub_(t[I], t[J], d1);
   
    
    for (int i=0; i<n; i++) {
      int gcd[MAX];

      if (equal(t[I], t[i])==0) continue;    

      if (equal(t[I], t[i])==1)
	sub_(t[i], t[0], d2);
      else 
	sub_(t[0], t[i], d2);

      pgcd(d1, d2, gcd);

      copy(d1, gcd);
      
    }
        
    int res[MAX]; 
    reste(t[0], d1, res);
    
    if(zero_base2(res)) {
      out << "Case #" << test+1 << ": 0" << endl;
      continue;
    }

    int sol2[MAX];
    sub_(d1, res, sol2);
        
    // conversion en decimal et output
    int sol10[55];
    toDec(sol2, sol10);

    out << "Case #" << test+1 << ": ";
    bool b = true;
    for (int i=54; i>=0; i--) {
      if (b && sol10[i]==0)
	continue;
      else {
	b = false;
	out << sol10[i];
      }
    }
    out << endl;
        
  }
}

