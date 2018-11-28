#include <cstdlib>
#include <iostream>
#include <fstream>

#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    int nengines, nsearches;
    
    std::ifstream in("A-large.in");
    std::ofstream out("A-large.out");
        
    string TestCases;
    std::getline(in,TestCases);
    int testcases = strtol(TestCases.c_str(), 0, 10);
    
    string NEngines, NSearches;
    string Engine, Search;
    
    std::vector<std::string> Engines;
    std::queue<std::string> UsedEngines;
    std::vector<std::string> Searches;

    int where, count;
    for(int i=1; i<=testcases; i++)
    {
       Engines.clear();
       while(!UsedEngines.empty()) UsedEngines.pop();
            
       count = 0;     
       std::getline(in, NEngines);
       nengines = strtol(NEngines.c_str(), 0, 10);

       for(int j=0; j<nengines; j++)
       {
           std::getline(in, Engine);
           Engines.push_back(Engine);
       }
       
       std::sort(Engines.begin(), Engines.end());
      
       std::getline(in, NSearches);
       nsearches = strtol(NSearches.c_str(), 0, 10);
                       
       for(int k=0; k<nsearches; k++)
       {
           std::getline(in, Search);

           where = std::find(Engines.begin(), Engines.end(), Search)-Engines.begin();

           if(where != Engines.end()-Engines.begin())
           {
             UsedEngines.push(Engines.at(where));
             Engines.erase(Engines.begin()+where);
           }
           if(Engines.empty())
           {
              while(UsedEngines.size()>1)
              {
                Engines.push_back(UsedEngines.front());
                UsedEngines.pop();
              }
              sort(Engines.begin(), Engines.end());
              count++;
           }
        }
        out << "Case #" << i << ": " << count << endl;
    }
    in.close();
    out.close();
   
    system("PAUSE");
    return EXIT_SUCCESS;
}
