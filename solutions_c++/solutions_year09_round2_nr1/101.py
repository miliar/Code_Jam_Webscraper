#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

struct Tree
{
  double w;
  string s;
  Tree *t1, *t2;
};

char cur;

Tree *readtree()
{
  if (cur == '(') {
    Tree *p = new Tree;
    p->t1 = NULL;
    p->t2 = NULL;
    cin >> p->w;
    cin >> cur;
    if (cur == ')') {
      cin >> cur;
      //cout << p << p->w << endl;
      return p;
    }
    cin.unget();
    cin >> p->s;
    cin >> cur;
    p->t1 = readtree();
    p->t2 = readtree();
    cin >> cur;
    //cout << p << p->w << p->s << p->t1 << p->t2 << endl;
    return p;
  } else {
    return NULL;
  }
}

double walk(vector<string> x, Tree *p)
{
  if (!p) return 1;
  if (!p->t1) return p->w;
  double v;
  if (find(x.begin(), x.end(), p->s) != x.end()) {
    v = walk(x, p->t1);
  } else {
    v = walk(x, p->t2);
  }
  return p->w * v;
}

int main()
{
  int cas;
  int N;

  cin >> N;

  for (cas = 1; cas <= N; cas++) {
    int L;
    cin >> L;

    cin >> cur;
    Tree *p = readtree();
    cin.unget();

    int n;
    cin >> n;
    cout << "Case #" << cas << ":" << endl;
    for (int i = 0; i < n; i++) {
      string s;
      int k;
      vector<string> x;
      cin >> s;
      cin >> k;
      for (int j = 0; j < k; j++) {
        string p;
        cin >> p;
        x.push_back(p);
      }
      double v = walk(x, p);
      cout << fixed << v << endl;
    }
  }

  return 0;
}

