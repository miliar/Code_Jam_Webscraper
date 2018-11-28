#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>

using namespace std;

bool isRecycledPair(int i, int j){
    std::stringstream ssi;
    ssi << i;
    std::stringstream ssj;
    ssj << j;
    std::queue<char> qi;
    std::queue<char> qj;

    for(int k = 0; k < ssi.str().length();k++){ //Creation files
        qi.push(ssi.str()[k]);
        qj.push(ssj.str()[k]);
    }

    for(int k = 0; k < ssi.str().length();k++){
        char c = qi.front();
        qi.pop();
        qi.push(c);
        if(qi==qj){
            return true;
        }
    }

    return false;
}

int main()
{
    // Ouverture du fichier, trouve le nombre de tests cases


    ostringstream oss; //Le fichier resultat sera contenu dans ce ostringstream

    //ifstream fichier("test.txt"); //ouverture du fichier
    ifstream fichier("C-small-attempt0.in"); //ouverture du fichier
    //ifstream fichier("A-large-practice.in"); //ouverture du fichier

    if(fichier){

        int numberOfTestCases; //le nombre total de cas à tester (premiere ligne de chaque input file
        cout << "Ouverture du fichier reussie, debut du traitement" << endl;
        fichier >> numberOfTestCases;

        //Traitement de chaque cas Test
        for(int i = 0; i<numberOfTestCases ;i++){
            cout << "cas " << i+1 << endl;
            int A;
            fichier>>A;
            int B;
            fichier>>B;
            int nbREPONSE = 0;

            for(int j = A; j < B; j++){
                for(int k = j+1; k <=B; k++ ){
                    if(isRecycledPair(j,k)){
                        nbREPONSE++;
                    }
                }
            }

            // Traitement du test case
            oss << "Case #" << (i+1) << ": " << nbREPONSE << endl;
        }


        //Affichage dans le fichier
        ofstream fichier2("result.txt");
        if(fichier2){
            cout << "Affichage de la solution dans le fichier " << "result.txt" << endl;
            fichier2 << oss.str();
            fichier2.close();
            fichier2.clear();
        }
        else
            cout << "Affichage dans le fichier result.txt a echoue"<< endl;

    }
    return 0;
}
