#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef vector<int> scores;
typedef set<scores> scoreset;
vector<scoreset> scorestable;

inline void swap(int &x, int &y) { int t=x;x=y;y=t;}

void disp(vector<int> p)
{
    cout << "(" << p[0] <<", " << p[1] << ", " << p[2] << ")";
}

inline void _scores(scores &v, int a, int b, int c)
{      
       int l = v.size();
       for(int i=0;i<3-l;i++) v.push_back(0);
       v[0] = a; v[1] = b; v[2] = c;
       sort(v.begin(), v.end());
}

inline scores *_scores(int a, int b, int c)
{
    scores *s = new scores;
    _scores(*s, a, b, c);
    return s;
}

inline bool surprising(vector<int> n) { return (n[2]-n[0]) == 2; }
inline int best(vector<int> n) { return *max_element(n.begin(), n.end()); }

scoreset &getscores(int n)
{
    if(scorestable.size() < n+1)
    {
      if(n == 0)
      {
           scores *s = _scores(0,0,0);
           set<scores> *ss = new set<scores>;
           ss->insert(*s);
           scorestable.push_back(*ss);
      }
      else
      {
          set<scores> *ss = new set<scores>;

          set<scores> &prev = getscores(n-1);
          for(set<scores>::iterator i=prev.begin(); i!=prev.end();i++)
          {
              scores v;
              for(int t=0;t<3;t++)
              {
                  _scores(v, (*i)[0]+(t==0), (*i)[1]+(t==1), (*i)[2]+(t==2));
                  bool add=(v[2]-v[0]) <= 2;
                  for(set<scores>::iterator j=ss->begin(); j!=ss->end();j++)
                      if((*j)[0] == v[0] && (*j)[1] == v[1] && (*j)[2] == v[2])
                      {
                          add = false;
                          break;
                      }
                  
                  if(add)
                      ss->insert(v);
              }                
          }
          
          scorestable.push_back(*ss);
      }
    }

    return scorestable[n];
}

int m(vector<int> &v, int S, int p, vector<scores> *current=NULL)
{
    if(v.size() == 0)
    {
        int x=0;
        for(vector<scores>::iterator vi=current->begin(); vi!=current->end(); vi++)
        {
            int b = best(*vi);
            if(b<p) continue;            
            x++;
        }
        return x;
    }
    else
    {
        int n = v[0], x=-1;
        v.erase(v.begin());
        
        if(!current)
            current = new vector<scores>;
            
        scoreset s = getscores(n);
        for(scoreset::iterator i=s.begin();i!=s.end();i++)
        {
          if(S==0 && surprising(*i))
                continue;
          
          current->push_back(*i);
          x=max(m(v, S-surprising(*i), p, current), x);
          current->pop_back();
        }
        
        v.insert(v.begin(), n);
        
        return x;
    }
}
 
int main(int argc, char *argv[])
{
    char *fname;
    int T;    
    
    if(argc > 1) fname = argv[1];
    else fname = "B-small-attempt1.in";
    
    ifstream in(fname);
    in >> T;
    
    for(int C=1;C<=T;C++)
    {
        int N, S, p, n, x;
        vector<int> v;
        vector<int>::iterator vi;
        
        in >> N >> S >> p;
        for(int i=0;i<N;i++)
        {
            in >> n;
            v.push_back(n);
        }
        
        x = m(v, S, p);
        
        cout << "Case #" << C << ": ";
        cout << x << endl;
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}

