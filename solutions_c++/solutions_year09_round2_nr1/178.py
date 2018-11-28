// login: 001963
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>      
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstdio>
#include <numeric>

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define DBG(x) cout << #x << " = " << x << endl

typedef pair<int,int> ii;
typedef pair<ii,int> iii;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector< ii > vii;

#define DEBUG

struct node {
  string feature;
  double p;
  node* left;
  node* right;
};

int matching(const string& s,int i)
{
  assert(s[i] == '(');
  int b = 1;
  for (int j = i + 1;j < s.size();++j) {
    if (s[j] == '(') {
      ++b;
    } else if (s[j] == ')') {
      --b;
    }
    if (b == 0) {
      return j;
    }
  }
  
  return -1;
}

node* parse(const string& s)
{
  int i = 0;
  while (s[i] != '(') {
    i++;
  }
  int j = s.size() - 1;
  while (j > i && s[j] != ')') {
    --j;
  }
  
  int k = i + 1;
  while (!isdigit(s[k])) {
    ++k;
  }
  int p = k;
  string tmp;
  while (isdigit(s[p]) || s[p] == '.') {
    ++p;
  }
  tmp = s.substr(k,p - k + 1);
  node* r = new node;
  stringstream ss;
  ss << tmp;
  ss >> r->p;
  
  k = p;
  while (k < j && !isalpha(s[k])) {
    ++k;
  }
  
  if (k == j) {
    r->left = 0;
    r->right = 0;
    return r;
  } else {
    int q = k;
    while (q < j && isalpha(s[q])) {
      r->feature += s[q++];
    }
    
    while (q < j && s[q] != '(') {
      ++q;
    }
    int m;
    assert(s[q] == '(');
    if (s[q] == '(') {
      m = matching(s,q);
      assert(m != -1);
      r->left = parse(s.substr(q,m - q + 1));
    }
    q = m + 1;
    while (q < j && s[q] != '(') {
      ++q;
    }
    assert(s[q] == '(');
    if (s[q] == '(') {
      m = matching(s,q);
      assert(m != -1);
      r->right = parse(s.substr(q,m - q + 1));
    }
    
    return r;
  }
}

void out_tree(node* root, int d)
{
  cout << string(d,' ') << root->p;
  if (root->left == 0) {
    cout << endl;
  } else {
    cout << ' ' << root->feature << endl;
    out_tree(root->left,d + 2);
    out_tree(root->right,d + 2);
  }
}

int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif
  
  int N;
  cin >> N;
  
  for (int test = 1;test <= N;++test) {
    int L;
    string s;
    string t;
    cin >> L;
    getline(cin,t);
    for (int i = 0;i < L;++i) {
      getline(cin,t);
      s += (t + ' ');
    }
    int A;
    cin >> A;
    vector< vector< string > > animals(A);
    vector< string > names;
    for (int i = 0;i < A;++i) {
      string name,feature;
      int n;
      cin >> name >> n;
      names.push_back(name);
      for (int j = 0;j < n;++j) {
        cin >> feature;
        animals[i].push_back(feature);
      }
    }
    
    //cout << s << endl;
    
    node* root = parse(s);
    //out_tree(root,2);
    
    cout << "Case #" << test << ":" << endl;
    for (int i = 0;i < animals.size();++i) {
      double p = 1;
      node* c = root;
      for (;;) {
        p *= c->p;
        if ( c->left == 0 ) {
          break;
        } else {
          if ( find( ALL(animals[i]), (c->feature) ) != animals[i].end() ) {
            c = c->left;
          } else {
            c = c->right;
          }
        }
      }
      cout.precision(7);
      cout << fixed << p << endl;
    }
      
  }
    
  
  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  return 0;
}
