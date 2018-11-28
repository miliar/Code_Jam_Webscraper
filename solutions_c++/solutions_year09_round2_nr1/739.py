#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef long long i64_t;

struct tree
{
  tree* left, *right;
  double p;
  string f;
  tree() : left(0), right(0) {}
};

tree* read_tree()
{
  char c;
  cin >> c;
  while (isspace(c))
  {
    c = getchar();
  }
  assert(c == '(');
  tree* r = new tree;
  cin >> r->p;
  c = getchar();
  while (isspace(c))
  {
    c = getchar();
  }
  if (c == ')')
  {
    return r;
  }
  else
  {
    cin.unget();
    cin >> r->f;
    r->left = read_tree();
    r->right = read_tree();
    c = getchar();
    while (isspace(c))
    {
      c = getchar();
    }
    assert(c==')');
    return r;
  }
  assert(0 && "Never reached");
  return 0;
}

int main()
{
  int N; cin >> N; cin.ignore();
  for (int n = 1; n <= N; ++n)
  {
    string tmp_;
    getline(cin, tmp_);
    tree* r = read_tree();
    int A; cin >> A; cin.ignore();
    cout << "Case #" << n << ": " << endl;
    cout.flush();
    for (int i = 1; i <= A; ++i)
    {
      string tmp;
      cin >> tmp;
      int np; cin >> np;
      set<string> props;
      for (int j = 0; j < np; ++j)
      {
        string s; cin >> s;
        props.insert(s);
      }
      /*if (np == 0) */getline(cin, tmp);
      tree* r1 = r;
      double res = 1.;
      while (r1)
      {
        res *= r1->p;
        if (props.find(r1->f) != props.end())
        {
          r1 = r1->left;
        }
        else
        {
          r1 = r1->right;
        }
      }
      cout << fixed << setprecision(10) << res << endl;
    }
    
  }
  return 0;
}
