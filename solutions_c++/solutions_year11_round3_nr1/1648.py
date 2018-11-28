#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <limits>
#include <set>
#include <list>
#include <map>
//#include <multimap>

#define ABSD(a,b) ((a) >= (b)? (a) - (b): (b) - (a))

#define MKPAIR(a,b) ((a) >= (b)? make_pair((a),(b)): make_pair((b),(a)))

using namespace std;

template<typename T>
ostream& operator<<(ostream &out, vector<T> const& l)
{
  typename vector<T>::const_iterator it = l.begin(), end = l.end();
  
  if (it != end)
    out << *it++;
  
  for (; it != end; ++it)
  {
    out << *it;
  }

  
  return out;
}

bool compute(size_t r, size_t c, vector<vector<char> > & p)
{
  for (size_t i = 0; i < r; ++i)
  {
    for (size_t j = 0; j < c; ++j)
    {
      if (p[i][j] == '#')
      {
        if (i == (r-1) || j == (c-1))
          return false;
        if (p[i+1][j] != '#' || p[i][j+1] != '#'|| p[i+1][j+1] != '#')
          return false;
        p[i][j] = '/';
        p[i+1][j] = '\\';
        p[i][j+1] = '\\';
        p[i+1][j+1] = '/';
      }
    }
  }
  return true;
}

int main()
{
	int cases;
	cin >> cases;
	for (int nc = 1; nc <= cases; ++nc)
	{
    size_t r, c;
    cin >> r >> c;
    vector<vector<char> > p(r, vector<char>(c, '.'));
    for (size_t i = 0; i < r; ++i)
    {
      for (size_t j = 0; j < c; ++j)
      {
        cin >> p[i][j];
      }
    }
    
    bool res = compute(r, c, p);
    
    cout << "Case #" << nc << ": " << endl;
    
    if (res == 0)
      cout << "Impossible";
    else
    {
      cout << p[0];
      for (size_t i = 1; i < p.size(); ++i)
      {
        cout << endl << p[i];
        /*
        for (size_t j = 0; j < c; ++j)
        {
          cout << p[i][j];
        }
        */
      }
    }
		cout << endl;
	}
}
