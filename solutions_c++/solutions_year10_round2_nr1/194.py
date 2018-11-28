#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <boost/foreach.hpp>
#include <boost/unordered_map.hpp>

using namespace std;

// stolen from gostai libport
  // Find \a v in the whole \a c.
  template<typename Container>
  inline typename Container::iterator
  find(Container& c, const typename Container::value_type& v)
  {
    return std::find(c.begin(), c.end(), v);
  }

  
  // Is \a v member of \a c?
  template<typename Container>
  inline bool
  has(const Container& c, const typename Container::value_type& v)
  {
    // We specify the instance to solve a conflict between the
    // two finds above, that compete against each other because
    // the parameter Container can embed a "const".
    return find<Container>(c, v) != end(c);
  }

std::string getLine()
{
  char line[4096];
  cin.getline(line, 4096);
  return line;
}

//unique strings not path elements
typedef boost::unordered_map<string, int> tsymbols;
boost::unordered_map<string, int> symbols;
int nSymbols;

struct elem
{
  elem():name(-1){};
  elem(int n): name(n) {}
  int name;
  std::vector<elem> children;
  bool operator == (const elem& b) const {return name == b.name;}
};


int process(vector<vector<int> > existing, vector<vector<int> > tocreate)
{
  // create existing tree structure
  elem root;
  for (int i=0; i<existing.size(); ++i)
  {
    vector<int>& path = existing[i];
    elem* curr = &root;
    for (int j=0; j<path.size(); ++j)
    {
      vector<elem>::iterator i = find(curr->children, path[j]);
      if (i == curr->children.end())
      {
	curr->children.push_back(elem(path[j]));
	curr = &curr->children.back();
      }
      else
	curr = &(*i);
    }
  }

  // Now insert tocreate, counting insertions
  int res = 0;
  for (int i=0; i<tocreate.size(); ++i)
  {
    vector<int>& path = tocreate[i];
    elem* curr = &root;
    for (int j=0; j<path.size(); ++j)
    {
      vector<elem>::iterator i = find(curr->children, path[j]);
      if (i==curr->children.end())
      {
	//cerr <<"child " << curr->name <<" " << path[j] << endl;
	curr->children.push_back(elem(path[j]));
	++res;
	curr = &curr->children.back();
      }
      else
	curr = &(*i);
    }
  }
  return res;
}


std::vector<int> hash(string s)
{
  s = s.substr(1, s.npos);
  std::vector<int> res;
  while (!s.empty())
  {
    string curr = s;
    int p = s.find_first_of('/');
    if (p != s.npos)
    {
      curr = s.substr(0, p);
      s = s.substr(p+1, s.npos);
    }
    else
      s = "";
    // fetch symbol
    tsymbols::iterator i = symbols.find(curr);
    if (i == symbols.end())
    {
      res.push_back(nSymbols);
      symbols[curr] = nSymbols++;
    }
    else
      res.push_back(i->second);
    //cerr << curr <<":" << res.back() << " ";
  }
  //cerr << endl;
  return res;
}

int main()
{
  int T;
  cin >> T;
  for (int t=0; t<T; ++t)
  {
    symbols.clear();
    nSymbols = 0;
    int E, C;
    cin >> E  >> C;
    getLine();
    vector<vector<int> > existing;
    vector<vector<int> > tocreate;
    for (int l=0; l<E; ++l)
    {
      string p = getLine();
      existing.push_back(hash(p));
    }
    for (int l=0; l<C; ++l)
    {
      string p = getLine();
      tocreate.push_back(hash(p));
    }
    int r = process(existing, tocreate);
    cout << "Case #" << (t+1) <<": " << r  << std::endl;
  }
}
