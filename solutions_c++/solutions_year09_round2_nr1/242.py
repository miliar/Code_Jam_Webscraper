#include <iostream>
#include <sstream>
#include <cstring>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define For(i,a,b) for (i = a; i != b; i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define GI ({int t; scanf("%d\n",&t);t;})
#define pb push_back
map<string,bool> M;
struct node {
  int index;
  string feat;
  double prob;
  struct node *left, *right;
}*T[3000];
char line[2000];
string str;
int ct = 0;
int ind;
inline bool isdig(char ch) {
  return ch >= '0' && ch <= '9';
}
inline bool isalp(char ch) {
  return ch >= 'a' && ch <= 'z';
}
node* build() {
  int nod = ct++;
  T[nod] = new node;
  T[nod]->index = nod;
  T[nod]->left = NULL;
  T[nod]->right = NULL;
  T[nod]->feat = "";
  T[nod]->prob = 0;
  bool l = false, r = false;
  bool n = false;
  bool dec = false;
  double b = 1.0;
  while (ind < str.length()) {
    if (str[ind] == '(') {
      if (!l) {
	l = true;
	T[nod]->left = new node;
	ind++;
	T[nod]->left = build();
	continue;
      }
      r = true;
      T[nod]->right = new node;
      ind++;
      T[nod]->right = build();
      continue;
    }
    if (str[ind] == ' ') {
      n = false;
      ind++;
      continue;
    }
    if (str[ind] == ')') {
      ind++;
      return T[nod];
    }
    if (isdig(str[ind]) || str[ind] == '.') {
      n = true;
      if (str[ind] == '.') {
	dec = true;
	b /= 10.0;
	ind++;
	continue;
      }
      if (!dec) {
	T[nod]->prob += str[ind++]-'0';
	continue;
      }
      T[nod]->prob += b*(str[ind++]-'0');
      b /= 10.0;
      continue;
    }
    if (isalp(str[ind])) {
      T[nod]->feat += str[ind++];
    }
  }
  return T[nod];
}
void print(node* nod) {
  if (!nod)
    return;
  cout << nod->index << " " << nod->feat << " " << nod->prob << endl;
  print(nod->left);
  print(nod->right);
}
double calc(node* nod) {
  if (!nod)
    return 1.0;
  if (M[nod->feat]) {
    return nod->prob*calc(nod->left);
  }
  return nod->prob*calc(nod->right);
}
main() {
  int t  = GI;
  int cas;
  For(cas,1,t+1) {
    ct = 0;
    str = "";
    cout << "Case #" << cas << ":\n";
    int L = GI;
    int i;
    Rep (i,L) {
      cin.getline(line,2000);
      if (i) {
	str += " ";
      }
      str += line;
    }
    //cout << " str = " << str << endl;
    ind = 1;
    build();
    int A = GI;
    while (A--) {
      M.clear();
      string animal;
      cin >> animal;
      int n;
      cin >> n;
      while (n--) {
	cin >> animal;
	M[animal] = true;
      }
      printf("%.7lf\n",calc(T[0]));
    }
    //print(T[0]);
  }
}
