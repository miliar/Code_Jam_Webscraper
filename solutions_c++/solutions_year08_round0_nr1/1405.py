#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <list>
#include <algorithm>

using namespace std;

template<class T>
void k_readline(istream &in, T &t)
{
  string line;
  getline(in, line);
  istringstream ss(line);
  ss >> t;
}

struct Path
{
  int switches;
  string engine;
  int nextpos;

  Path(int aswitches, string aengine, int anextpos)
    : switches(aswitches), engine(aengine), nextpos(anextpos)
  {}
};


int calculate(const vector<string> &engines, const vector<string> &keywords)
{
  list<Path> routes;

  for(int i=0; i<engines.size(); i++)
  {
    routes.push_back(Path(0, engines[i], 0));
  }

  while(true)
  {
    Path fr = routes.front();
    int i=fr.nextpos;
    for(; i<keywords.size(); i++)
    {
      if(keywords[i] == fr.engine)
      {
        routes.erase(routes.begin());
        for(int a=0; a<engines.size(); a++)
        {
          if( engines[a] != fr.engine )
          {
            list<Path>::iterator it=routes.begin();
            while(it != routes.end())
            {
              if( (it->engine == fr.engine) &&
                  (it->nextpos <= i)
                )
              {
                list<Path>::iterator it2 = it;
                it++;
                routes.erase(it2);
              }
              else
              {
                it++;
              }
            }

            routes.push_back(Path(fr.switches+1, engines[a], i));
            //cout << routes.size() << endl;
          }
        }
        break;
      }
    }
    if(i==keywords.size()) return fr.switches;
  }
}

int main(int argc, char *argv[])
{
  ifstream in(argv[1]);

  unsigned n;

  string line;

  k_readline(in, n);

  for(unsigned i=1; i<=n; i++)
  {
    unsigned ne,nk;

    k_readline(in, ne);
    vector<string> engines;
    for(unsigned count=0; count<ne; count++)
    {
      string s;
      getline(in, s);
      engines.push_back(s);
    }
    k_readline(in, nk);
    vector<string> keywords;
    for(unsigned count=0; count<nk; count++)
    {
      string s;
      getline(in, s);
      keywords.push_back(s);
    }

    cout << "Case #" << i << ": " << calculate(engines,keywords) << endl;
  }

  return 0;
}
