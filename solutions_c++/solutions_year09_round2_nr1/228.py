#include <iostream>
#include <string>
#include <set>

using namespace std;

class tree
{
public:
  string name;
  double weight;
  tree *left;
  tree *right;
  tree ()
  {
    weight = 1;
    name = "";
    left = 0;
    right = 0;
  }
  ~tree ()
  {
    delete left;
    delete right;
  }
};

istream &operator >> (istream &in, tree *t)
{
  char c;
  in >> c;
  in >> t->weight;
  in >> c;
  if (c != ')')
  {
    in.unget();
    in >> t->name;
    t->left = new tree;
    in >> t->left;
    t->right = new tree;
    in >> t->right;
    in >> c;
  }
  return in;
}

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int n;
  cin >> n;
  cout.precision(7);
  for (int t = 1; t <= n; t++)
  {
    cout << "Case #" << t << ":" << endl;
    int l;
    cin >> l;
    tree *T = new tree;
    cin >> T;
    int a;
    cin >> a;
    for (int i = 0; i < a; i++)
    {
      string name;
      int num;
      cin >> name >> num;
      set <string> prop;
      for (int j = 0; j < num; j++)
      {
        string s;
        cin >> s;
        prop.insert(s);
      }
      tree *cur = T;
      double p = 1;
      while (cur->name != "")
      {
        p *= cur->weight;
        if (prop.find(cur->name) != prop.end())
        {
          cur = cur->left;
        }
        else
        {
          cur = cur->right;
        }
      }
      p *= cur->weight;
      cout << p << endl;
    }
  }
  return 0;
}