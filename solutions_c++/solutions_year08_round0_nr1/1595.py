#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>
#include <set>
#include <string>

using namespace std;

int main(size_t argc, const char * argv[])
{
  if (1 == argc)
    return -1;

  ifstream is(argv[1]);
  ofstream os("data.out");

  size_t cc;
  is >> cc;

  for (size_t c= 0; c < cc; ++c)
  {
    set<string> sn;
    {
      size_t k;
      is >> k;
      string t;
      getline(is, t);
      for (size_t n= 0; n < k; ++n)
      {
        getline(is, t);
        sn.insert(t);
      }
    }
    list<string> qn;
    {
      size_t k;
      is >> k;
      string t;
      getline(is, t);
      for (size_t n= 0; n < k; ++n)
      {
        getline(is, t);
        qn.push_back(t);
      }
    }

    size_t s= 0;
    {
      set<string> v= sn;
      for (list<string>::const_iterator i= qn.begin(), i_end= qn.end(); i != i_end; ++i)
      {
        v.erase(*i);

        if (0 == v.size())
        {
          ++s;
          v= sn;
          v.erase(*i);
        }
      }
    }

    os << "Case #" << c+1 << ": " << s << endl;
  }

  return 0;
}
