#include <string>
#include <iostream>
#include <map>

using namespace std;

typedef map<const string, int> EngineMap;

const int INF = 100000000;

void resetEngines(EngineMap &engines)
{
   EngineMap::iterator curE = engines.begin();
   EngineMap::iterator endE = engines.end();
   while(curE != endE)
   {
      (*curE).second=INF;
      curE++;
   }
}

int maxDistance(EngineMap &engines)
{
   int max = 0;
   string sel; //?
   EngineMap::iterator curE = engines.begin();
   EngineMap::iterator endE = engines.end();
   while(curE != endE && max<INF)
   {
      max = (*curE).second > max? (*curE).second : max;
      curE++;
   }
   return max;
}

int main()
{
   string eol;
   int nProblem;
   cin >> nProblem;

   for(int iProblem=1; iProblem<=nProblem; iProblem++)
   {
      int nSwitches = 0;
      EngineMap engines;

      int nEngines;
      cin >> nEngines;
      getline(cin, eol);

      for(int iEngine=0; iEngine<nEngines; iEngine++)
      {
         string engineName;
         getline(cin, engineName);
         engines[engineName]=INF;
      }

      int nQueries;
      cin >> nQueries;
      getline(cin, eol);
      int iDistance = 1;

      for(int iQuery=0; iQuery<nQueries; iQuery++)
      {
         string query;
         getline(cin, query);
         engines[query] = iDistance++;
         if(maxDistance(engines) < INF)
         {
            nSwitches++;
            resetEngines(engines);
            engines[query] = iDistance = 1;
         }
      }

      cout << "Case #" << iProblem << ": " << nSwitches  << endl;
   }   
}

//======================================================================== END
