#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

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
    size_t ta;
    is >> ta;
    is.ignore();

    size_t na;
    is >> na;
    is.ignore();

    size_t nb;
    is >> nb;
    is.ignore();

    vector<size_t> sa[2];
    vector<size_t> sb[2];
    {
      struct Helper
      {
        static void init_schedule(istream &is, vector<size_t> s[2], size_t c)
        {
          for (size_t p= 0; p < 2; ++p)
            s[p].reserve(c);

          string t;
          for (size_t n= 0; n < c; ++n)
          {
            for (size_t p= 0; p < 2; ++p)
            {
              is >> t;
              istringstream iss(t);
              size_t h, m;
              iss >> h;
              iss.ignore();
              iss >> m;
              iss.ignore();
              s[p].push_back(h * 60 + m);
            }
          }

          for (size_t p= 0; p < 2; ++p)
            sort(s[p].begin(), s[p].end());
        }
      };

      Helper::init_schedule(is, sa, na);
      Helper::init_schedule(is, sb, nb);
    }

    size_t ca= sa[0].size();
    size_t cb= sb[0].size();
    {
      struct Helper
      {
        static size_t calc_reserve(vector<size_t> s1, vector<size_t> s2, size_t ta)
        {
          size_t res= 0;

          int i= (int)s1.size();
          for (int n= (int)s2.size()-1; n > -1; --n)
          {
            for (--i; i > -1; --i)
            {
              if (s1[i] + ta <= s2[n])
              {
                ++res;
                break;
              }
            }
            if (i < 0)
              break;
          }

          return res;
        }
      };

      ca-= Helper::calc_reserve(sb[1], sa[0], ta);
      cb-= Helper::calc_reserve(sa[1], sb[0], ta);
    }

    os << "Case #" << c+1 << ": " << ca << " " << cb << endl;
    if ((ca < 0) || (cb < 0))
      throw exception();
  }

  return 0;
}
