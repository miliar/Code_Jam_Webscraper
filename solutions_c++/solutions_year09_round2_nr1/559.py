int N;

#include <stdio.h>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
using namespace std;

int i;

double w[400];
string feature[400];
int t[400]; // 0 = end
int f[400];

string buf;
int p;

set<string> wanted;

bool isblank(char c)  { return c==' ' || c=='\n' || c=='\r' ; }

string gettok() {
  while (isblank(buf[p])) p++;
  if (buf[p] == ')') return buf.substr(p++,1);
  if (buf[p] == '(') return buf.substr(p++,1);
  int a = p;
  while (!isblank(buf[p]) && buf[p]!=')' && buf[p]!='(') p++;
  return buf.substr(a,p-a);
}

void parsetree() {
  string s;
  int x = i++;
  while (isblank(buf[p])) p++;
  assert(buf[p]=='('); p++;
  while (isblank(buf[p])) p++;
  s = gettok();
  w[x] = atof(s.c_str());
  t[x] = 0;
  f[x] = 0;
  s = gettok();
  if (s==")") {
    feature[x] = "";
    return;
  }
  feature[x] = s;
  t[x] = i;
  parsetree();
  f[x] = i;
  parsetree();

  s = gettok();
  assert(s==")");
}

double run_tree(int x, double val) {
  val *= w[x];
  if (feature[x] == "") return val;
  fprintf(stderr,"t[%d]=%d f[%d]=%d\n",x, t[x], x, f[x]);
  assert(t[x] != 0);
  assert(f[x] != 0);
  if (wanted.find(feature[x]) != wanted.end()) return run_tree(t[x],val);
  else return run_tree(f[x],val);
}

int main()
{
  // Input
  scanf("%d\n",&N);
  
  for (int n=1; n<=N; n++) {
    int L;
    scanf("%d\n",&L);
    buf = ""; 
    while (L-- > 0) {
      string str;
      getline(cin,str);
      buf += str;
    }
    cerr << buf << endl;
    p=0;
    const int first = 1;
    i=first;
    parsetree();
    printf("Case #%d:\n",n);
    int A;
    scanf("%d\n",&A);
    for (int a=0; a<A; a++) {
      string str;
      getline(cin,str);
      stringstream ss(str);
      string animal;
      int N;
      string f;
      wanted.clear();
      ss >> animal;
      ss >> N;
      for (int i=0; i<N; i++) {
        ss >> f;
        wanted.insert(f);
      }
      double prop_cute = run_tree(first, 1.0);
      printf("%.7f\n", prop_cute);
    }
  }
  return 0;
}
