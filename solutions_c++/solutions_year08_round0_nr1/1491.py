/*
ID: kazastankas
PROG: saving_the_universe
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
int cases, engines, queries, modified, lastmod, numswitch;
string query;
struct search_engine {
       public:
              string name;
              int earliest;
};
int main() {
    fin >> cases;
    for (int i=0;i<cases;i++) {
        fin >> engines;
        search_engine names[engines];
        // woo file streams leave newlines behind
        getline(fin,query);
        for (int j=0;j<engines;j++) {
            // set up structs to keep track of when the engine has to change
            getline(fin,names[j].name);
            names[j].earliest=1001;
        }
        fin >> queries;
        // woo file streams leave newlines behind
        getline(fin,query);
        modified=0;
        lastmod=-1;
        numswitch=0;
        for (int k=0;k<queries;k++) {
            getline(fin,query);
            // modify to keep first occurence of a given engine
            for (int l=0;l<engines;l++) {
                if (names[l].name==query) {
                   if (k<names[l].earliest) {
                      // if engine was not seen before, it is now
                      if (names[l].earliest==1001) modified++;
                      names[l].earliest=k;
                   }
                   lastmod=l;
                }
            }
            // when all engines have been seen
            if (modified==engines) {
               // effectively take the most recent one - set everything else back
               // for open usage
               for (int m=0;m<engines;m++) {
                   if (lastmod!=m) names[m].earliest=1001;
               }
               // we've already seen an engine - the engine that we used before switching
               modified=1;
               // increment switches
               numswitch++;
            }
        }
        fout << "Case #" << i+1 << ": " << numswitch << endl;
    }
    return 0;
}

