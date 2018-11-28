//save the universe

#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

  typedef std::vector < std::string > vecS;
  
  void readCase(std::ifstream &inputFileStream, vecS &engines, vecS &queries)
  {
    int nengines, nqueries;
    std::string line;
    inputFileStream >> nengines;
    std::getline(inputFileStream, line);
    for (int i = 0; i < nengines; i++)
    {
      std::string engineName;
      std::getline(inputFileStream, engineName);
      engines.push_back(engineName);
    }

    inputFileStream >> nqueries;
    std::getline(inputFileStream, line);

    
    for (int i = 0; i < nqueries; i++)
    {
      std::string queryName;
      std::getline(inputFileStream, queryName);
      queries.push_back(queryName);
    }
  }
      

  int solveCase(const vecS &engines, const vecS &queries)
  {
//Given: N, m, S = {1....N}, K member of S^m
//Output: P member S^m such that P[i] != K[i] and P has a minimal number of
//  switches

//Method of attack: Suppose let Q[i] be the set of all P[i] that have s(i) switches.
//  To determine Q[i+1],
//    find all elements of Q[i] that don't equal K[i+1]
//    if there are any
//      Q[i+1] = Q[i]
//      s[i+1] = s[i]
//    else
//      Q[i+1] = S / K[i+1]
//      s[i+1] = s[i]+1
//
//
    std::set<std::string> Q;
    int s = 0;
    for (int i = 0; i < engines.size(); i++)
    {
      Q.insert(engines[i]);
    }
    for (int i = 0; i < queries.size(); i++)
    {

      for (std::set<std::string>::iterator r = Q.begin();
           r != Q.end();
           ++r)
      {
         if (queries[i] == *r)
         {
            Q.erase(r);
            break;
         }
      }
      if (Q.empty())
      {
        s++;
        Q.clear();
        for (int j = 0; j < engines.size(); j++)
        {
          if (queries[i] != engines[j])
            Q.insert(engines[j]);
        }
      }


    }
    return s;
  }
  


  int main(int argc, char **argv)
  {
    int ncases;

    std::ifstream inputFileStream(argv[1]);
    inputFileStream >> ncases;

    for (int i=0; i < ncases; i++)
    {
      vecS engines;
      vecS queries;
      readCase(inputFileStream, engines, queries);
      int nswitches = solveCase(engines, queries);
      std::cout <<"Case #"<<i+1<<": "<<nswitches<<"\n";
    }
  }
