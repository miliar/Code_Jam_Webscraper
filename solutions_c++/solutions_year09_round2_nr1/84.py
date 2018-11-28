#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std; 

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)


struct node {
 string name;
 double p;
 int ch[2];
};

const int maxt=1000000;

node tree[maxt];
char t[maxt], s[maxt];
set<string> h;
int n;
int T;    

double solve(int x) {
 if (tree[x].ch[0]==-1) 
  return tree[x].p;

 if (h.count(tree[x].name))
  return tree[x].p*solve(tree[x].ch[0]);
 else return tree[x].p*solve(tree[x].ch[1]);
}


int main() {
 freopen("a.in", "r", stdin);
 freopen("a.out", "w", stdout);

 int nt; scanf("%d", &nt);  gets(s);

 for (int tc=1; tc<=nt; ++tc) {
  int nl; scanf("%d", &nl); gets(t);

  n=0;

  for (int i=0; i<nl; ++i) {
   gets(t);
   int m=strlen(t);
   for (int j=0; j<m; ++j)
    s[n++]=t[j];
  }
     
  T=0;


  stack<int> st;
  stack<int> type;

  for (int i=0; i<n; ++i) if (s[i]=='(') {
    ++i;
   
    int m=0;
    for (; s[i]==' '; ++i);
    for (; (s[i]>='0' && s[i]<='9') || s[i]=='.'; ++i)
     t[m++]=s[i];
    t[m]=0;
    double p; sscanf(t, "%lf", &p);

    for (; s[i]==' '; ++i);

    if (s[i]==')') {
     tree[T].p=p;
     tree[T].ch[0]=-1;

     if (!st.empty()) {
      int par=st.top();
      int tp=type.top();
      type.pop();
      st.pop();
      tree[par].ch[tp]=T;
     }
     ++T;
    } else {
     string name;

     for (; s[i]>='a' && s[i]<='z'; ++i)
      name+=s[i];

     if (!st.empty()) {
      int par=st.top();
      int tp=type.top();
      type.pop();
      st.pop();
      tree[par].ch[tp]=T;
     }

     tree[T].name=name;
     tree[T].p=p;

     st.push(T);
     st.push(T);
     type.push(1);
     type.push(0);
     T++;   
     }    

   }

  

  int m;
  cin>>m;

  printf("Case #%d:\n", tc);
  for (int i=0; i<m; ++i) {
   string name; cin>> name;
   h.clear();
   int k; cin>>k;
   for (int j=0; j<k; ++j) {
    string q; cin>> q;
    h.insert(q);
   }
   double res=solve(0);
   printf("%.7f\n", res);

  }

 }
   
  
  
 

 return 0;
}
