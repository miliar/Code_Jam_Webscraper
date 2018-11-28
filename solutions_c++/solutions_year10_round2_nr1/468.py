#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
using namespace std;

//<macros>
#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define aout std::cout << "Case #" << (case_id+1) << ": "
//</macros>

//<libs>
//</libs>

int num_cases, case_id=0;

struct node
{
    string name;
    vector<node> children;
};

int mkdir(node& n, const vector<string>& path, int i)
{
  if (path.size() == 0 || i == path.size()-1)
    return 0;

  assert (n.name == path[i]);
  int j;
  rep(j, n.children.size())
  {
    if (n.children[j].name == path[i+1])
      break;
  }
  
  int cost = 0;

  if (j == n.children.size())
  {
    cost = 1;
    node child;
    child.name = path[i+1];
    n.children.push_back(child);
  }

  return cost + mkdir(n.children[j], path, i+1);
}

vector<string> split(string& str, char delim)
{
  vector<string> res;
  
  string dir = "";
  int pos;
  rep(pos, str.length())
  {
    if (str[pos] == '/')
    {
      res.push_back(dir);
      dir = "";
    }
    else
      dir += str[pos];
  }

  if (dir.length() > 0)
    res.push_back(dir);

  return res;
}

void solve()
{
  node root;
  root.name="";
  
  int N, M; cin >> N >> M;
  string dir;
  int n,m;
  rep(n, N)
  {
    cin>>dir;
    mkdir(root, split(dir, '/'), 0);
  }
  int cost = 0;
  rep(m, M)
  {
    cin >> dir;
    cost += mkdir(root, split(dir, '/'), 0);
  }

  aout << cost << endl;    
}

int main()
{
  std::cin >> num_cases;

  rep(case_id, num_cases)
  {
    solve();
  }
}

