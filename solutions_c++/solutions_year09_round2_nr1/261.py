#include <iostream>
#include <sstream>
#include <vector>
#include <bitset>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

struct node {
  ~node()
  {
    delete r;
    delete l;
  }
  double w;
  string f;
  node* l;
  node* r;
};

void skip(string const& line, int& pos)
{
  while (line[pos] == ' ' && pos < line.size())
      ++pos;
}

void parse(node*& tree, string const& line, int& pos)
{
  tree = new node();
  while (line[pos] == ' ')
    ++pos;

  ++pos; //skip (
  skip(line, pos);
  //pos += 2; // skip 0.
  
  string number;
  while (isdigit(line[pos]) || line[pos] == '.')
    number += line[pos++];
  tree->w = atof(number.c_str());
  skip(line, pos);

  while (isalpha(line[pos]))
  {
    tree->f += line[pos];
    ++pos;
  }

  if (tree->f.empty())
  {
    tree->l = tree->r = 0;
  }
  else {
    parse(tree->l, line, pos);
    parse(tree->r, line, pos);
  }

  skip(line, pos);
  ++pos; // skip )
}

int main()
{  
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int tests;
  cin >> tests;

  for (int t = 0; t < tests; ++t)
  {
    int lines;
    cin >> lines;
    cin.ignore();

    node* root = 0;

    string line;
    string str;
    while (lines-- && getline(cin, str))
    {
       // if (str.size())
         // str.resize(str.size() - 1);
      line += str;
    }

    int pos = 0;
    parse(root, line, pos);

    cout << "Case #" << t + 1 << ":\n";

    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
      string animal;
      cin >> animal;
      int cnt;
      cin >> cnt;

      set<string> f;

      for (int j = 0; j < cnt; ++j)
      {
        cin >> str;
        f.insert(str);
      }

      long double p = 1;
      node* iter = root;
      while (true)
      {
        p *= iter->w;
        if (iter->l && iter->r)
        {
          if (f.count(iter->f)) 
          {
            iter = iter->l;
          }
          else
            iter = iter->r;
        }
        else
          break;
      }

      cout << setprecision(8) << fixed << p << "\n";
    }
      delete root;
  }

  return 0;
}