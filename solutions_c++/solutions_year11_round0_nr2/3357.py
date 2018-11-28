#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int main()
{
    int T, C, D, N, i,j,k;
    vector <string> combi;
    vector <string> opone;
    string aux;
    string invoca;

    cin >> T;

    for(i=0;i<T;i++){
        combi.clear();
        opone.clear();
        cin >> C;
        for(j=0;j<C;j++){
            cin >> aux;
            combi.push_back(aux);
        }
        cin >> D;
        for(j=0;j<D;j++){
            cin >> aux;
            opone.push_back(aux);
        }
        cin >> aux;
        cin >> invoca;
        j=0;
        string parte2 = invoca;
        string parte1;
        string ultimas2;
        bool cambio = false;

        do{

            parte1.append(parte2.substr(0,1));
            parte2.erase(0,1);
            if(parte1.size()>1){
                ultimas2 = parte1.substr(parte1.size()-2,2);
                //cout << parte1 << ":"<< parte2 << ","<< ultimas2 <<endl;
                cambio = false;
                for(k=0;k<combi.size();k++){
                    if(combi[k].substr(0,2) == ultimas2){ parte1.erase(parte1.size()-2,2); parte1.append(combi[k].substr(2,1)); cambio = true; }
                    else if(combi[k].substr(1,1).append(combi[k].substr(0,1)) == ultimas2){ parte1.erase(parte1.size()-2,2); parte1.append(combi[k].substr(2,1)); cambio = true; j--; }
                }

                if(!cambio){
                    for(k=0;k<opone.size();k++){
                        if(parte1.find(opone[k].substr(0,1)) != string::npos && parte1.find(opone[k].substr(1,1)) != string::npos ){ parte1=""; j=0; cambio = true;}
                    }
                }
            }
            j++;

        }while(parte2.size()>0);

        cout << "Case #" << i+1<< ": [";
        for(k=0;k<parte1.size();k++){
            if(k>0) cout << ", ";
            cout << parte1[k];
        }
        parte1.clear();
        parte2.clear();
        invoca.clear();
        cout << "]"<< endl;

    }
    return 0;
}
