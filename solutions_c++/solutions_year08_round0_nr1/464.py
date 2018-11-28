#include <iostream>
#include <string>
#include <vector>
using namespace std;

//typedef unsigned long long tull;
const int MAX = 100000;

int main() 
{
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  int N;
  cin >> N;

  vector<string> SE;
  vector<int> sw;
  string search_engine, query;
  int S,Q, cm;

  for (int inn=0; inn<N; ++inn)
  {
    SE.clear();
    sw.clear();
    cin >> S;
    getline(cin, search_engine);
    for (int i=0; i<S; ++i)
    {
      getline(cin, search_engine);
      //cin >> search_engine;
      SE.push_back(search_engine);
      sw.push_back(0);
    }
    //sw.push_back(0);

    cin >> Q;
    if (Q>0)
    {
      getline(cin, query);
      for (int i=0; i<Q-1; ++i)
      {
        //cin >> query;
        getline(cin, query);
        //j = 0;
        //for (vector<string>::iterator qit= SE.begin(); qit != SE.end(); ++qit)
        for (int SEit=0; SEit < S; ++SEit)
        {
          //if (*qit == query)
          if (SE[SEit] == query)
          {
            cm=MAX;
            for (int swit=0; swit < S; ++swit)
            {
              if (swit != SEit)
                if (sw[swit] < cm)
                  cm = sw[swit];
            }
            sw[SEit] = cm+1;
          }
         // else
           // ++j;
        }
      }
      getline(cin, query);
      int SEit=0; 
      while ((SEit < S) && (SE[SEit] != query))
        ++SEit;

      cm=MAX;
      for (int swit=0; swit < S; ++swit)
      {
       if (swit != SEit)
         if (sw[swit] < cm)
           cm = sw[swit];
      }
      cout << "Case #" << inn+1 << ": " << cm << endl;
    }
    else
    {
      cout << "Case #" << inn+1 << ": 0" << endl;
    }
 
  }
  return 0;
}
