#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


class Engine{
    public:
    string name;
    int distance;  //from the first query : -1 means infinite
    int id;
    bool alreadyFound;

    Engine(string name, int count){
        alreadyFound = false;
        this->name = name;
        this->distance = -1;
        id = count;
        count++;
    }
};

int findEngine(string query, vector<Engine> engines){
    vector<Engine>::iterator it;
    for(it = engines.begin(); it < engines.end(); it++){
        if (query == it->name) return it->id;
    }
    return -1;
}

int main ()
{
   string line;
   vector<Engine> engines;
   line.clear();
   ifstream infile("A-large.in");
   FILE * output;
   output = fopen ("output.out","w");
   getline(infile, line);
   //gets the number of cases
   unsigned int ncases = atoi(line.c_str());
   for(int i = 0; i < ncases; i++){
       engines.clear();
       int count = 0;
       getline(infile, line);
       //number of engines
       unsigned int nengines = atoi(line.c_str());
       for(int j = 0; j < nengines; j++){
          getline(infile, line);
          Engine *nova = new Engine(line,count);
          engines.push_back(*nova);
          count++;
       }

       //number of queries
       getline(infile, line);
       unsigned int nqueries = atoi(line.c_str());
       vector<int> queries;
       queries.clear();
       for(int q = 0; q < nqueries; q++){
           getline(infile, line);
           queries.push_back(findEngine(line,engines));
       }

       //lets find the engine most far from the first query
       vector<int> useengine;
       useengine.clear();

       vector<int>::iterator it;
       int pos = 0;
       int position = 0;
       bool complete = false;
       int chosen = 0;
       while(!complete){
       complete = true;
       for(pos; pos< queries.size(); pos++){
               int query = queries.at(pos);
               if (query == -1 || engines.at(query).alreadyFound) continue;
               engines.at(query).alreadyFound = true;
               Engine teste = engines.at(query);
               engines.at(query).distance = pos;
               chosen = engines.at(query).id;   //q is the id of the engine
               position = pos;
               complete = false;
       }

       //lets see if an engine has a -1 distance
       vector<Engine>::iterator ite;
       for(ite = engines.begin(); ite < engines.end(); ite++){
           if (ite->distance == -1){
               chosen = ite->id;
               position = 9999999;
               complete = true;
           }
       }

       pos = position;
       //the best engine is in the end of the vector
       //lets count the number of switches necessary

       vector<Engine>::iterator it;
       for(it = engines.begin(); it < engines.end(); it++){
           it->alreadyFound = false;
           it->distance = -1;
       }
       engines.at(chosen).alreadyFound = true;
       engines.at(chosen).distance = pos;
       useengine.push_back(chosen);
       }
       int chosenEng = useengine.front();
       int nswitches = 0;
       vector<int>::iterator it2;
       for(it2 = queries.begin(); it2 < queries.end(); it2++){
               int query = *it2;
               if (query == -1) continue;
               if (query == chosenEng){
                   nswitches++;
                   int temp = useengine.size();
                   chosenEng = useengine.at(nswitches);
               }
       }
   fprintf (output, "Case #%d: %d\n",i+1, nswitches);
   }
   fclose (output);
}
