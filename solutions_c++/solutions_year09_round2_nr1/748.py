#include <iostream>
#include <cassert>
#include <memory>
#include <set>
#include <iomanip>

using namespace std;

struct node
{
  double p;
  string feature;
  auto_ptr<node> left;
  auto_ptr<node> right;
};

inline void SkipWhiteSpaces()
{
  char c = cin.peek();
  while(c == ' ' || c == '\n')
  {
    cin.ignore();
    c = cin.peek();
  }
}

struct strless : public binary_function <string, string, bool> 
{ 
  bool operator()(const string& left, const string& right) const { 
    return (left.compare(right) < 0); 
  } 
}; 

void ReadNode(auto_ptr<node>& n)
{
  SkipWhiteSpaces();

  cin >> n->p;

  SkipWhiteSpaces();

  char c = cin.peek();

  if (c == ')')
  {
    cin.ignore();
  }
  else
  {
    while(c != ' ' && c != '\n' && c != '(')
    {
      cin.ignore();
      n->feature += c;
      c = cin.peek();;
    }

    SkipWhiteSpaces();

    assert(cin.peek() == '(');
    cin.ignore();

    n->left.reset(new node);
    ReadNode(n->left);

    SkipWhiteSpaces();

    assert(cin.peek() == '(');
    cin.ignore();

    n->right.reset(new node);
    ReadNode(n->right);

    SkipWhiteSpaces();
    assert(cin.peek() == ')');
    cin.ignore();
  }
}

double CalcNode(double val, const auto_ptr<node>& n, const set<string, strless>& features)
{
  double res = val * n->p;

  if (n->feature.empty())
  {
    return res;
  }
  else
  {
    if (features.find(n->feature) != features.end())
    {
      return CalcNode(res, n->left, features);
    }
    else
    {
      return CalcNode(res, n->right, features);
    }
  }
}

int main()
{
  int N = 0;
  cin >> N;

  for (int i = 0; i < N; ++i)
  {
    int L = 0;
    cin >> L;

    auto_ptr<node> root(new node);

    char c = 0;
    while(c != '(')
    {
      cin.get(c);
    }

    ReadNode(root);

    int A = 0;
    cin >> A;

    cout << "Case #" << (i + 1) << ": " << endl;

    for (int j = 0; j < A; ++j)
    {
      char name[20];
      cin >> name;

      int n = 0;
      cin >> n;

      set<std::string, strless> features;
      for (int k = 0; k < n; ++k)
      {
        char feature[20];
        cin >> feature;

        features.insert(string(feature));
      }

      double res = CalcNode(1, root, features);

      cout << fixed << setprecision(7) << res << endl;
    }
  }
  
  return 0;
}

