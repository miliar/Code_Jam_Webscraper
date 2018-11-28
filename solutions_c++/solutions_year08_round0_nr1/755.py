#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>


using namespace std;

int main()
{
    ifstream entrada("A-large.in");
    ofstream saida("A-large.out");

    int ncases;
    map<string, int> engines; // engine + first occurrence
    vector<string> queries;

    entrada >> ncases;

    for (int ccase = 1; ccase <= ncases; ccase++){

        int nengines, nqueries;
        string engine, query;

        entrada >> nengines;
        getline(entrada, engine); // Due to endline after the nengines?

        for (int i = 0; i < nengines; i++){
            getline(entrada, engine);
            engines[engine] = -1;
        }

        entrada >> nqueries;
        getline(entrada, engine); // Due to endline after the nqueries?

        for (int i = 0; i < nqueries; i++){
            getline(entrada, query);
            queries.push_back(query);
        }

        // Defining the first engine
        int maxpos = -1, nswitches = 0;
        string currengine = "";

        for (int i = 0; i < nqueries; i++){
            if (engines[queries[i]] == -1){
                engines[queries[i]] = i;
                if (i > maxpos){
                    currengine = queries[i];
                    maxpos = i;
                }
            }
        }
        //cout << "Caso " << ccase << endl << "        currengine: " << currengine << ", com maxpos = " << maxpos << endl;

        // No occurrences = best engine
        bool found = false;
        for (map<string, int>::iterator it = engines.begin(); it != engines.end(); it++){
            if (it->second == -1){
                found = true;
                //cout << "        achou " << it->first << endl;
                break;
            }
        }

        if (!found){

            int currpos = maxpos;

            while (currpos < nqueries - 1){
                string newengine;
                for (int i = currpos; i < nqueries; i++){
                    if ((queries[i] != currengine) && (engines[queries[i]] < currpos)){
                        engines[queries[i]] = i;
                        if (i > maxpos){
                            newengine = queries[i];
                            maxpos = i;
                        }
                    }
                }

                for (map<string, int>::iterator it = engines.begin(); it != engines.end(); it++){
                    if ((it->first != currengine) && (it->second < currpos)){
                        newengine = it->first;
                        maxpos = nqueries - 1;
                        break;
                    }
                }

                //cout << "        de " << currengine << " para "  << newengine << " a partir da linha " << maxpos << endl;
                currengine = newengine;
                nswitches++;
                currpos = maxpos;
            }

            if ((nqueries > 0)&&(queries[nqueries - 1] == currengine))
                nswitches++;
        }

        saida << "Case #" << ccase << ": " << nswitches;
        if (ccase < ncases)
            saida << endl;
        engines.clear();
        queries.clear();
    }

    entrada.close();
    saida.close();
    return 0;
}
