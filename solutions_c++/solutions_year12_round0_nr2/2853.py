#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    // Ouverture du fichier, trouve le nombre de tests cases


    ostringstream oss; //Le fichier resultat sera contenu dans ce ostringstream

    //ifstream fichier("test.txt"); //ouverture du fichier
    //ifstream fichier("B-small-attempt3.in"); //ouverture du fichier
    ifstream fichier("B-large.in"); //ouverture du fichier

    if(fichier){

        int numberOfTestCases; //le nombre total de cas à tester (premiere ligne de chaque input file
        cout << "Ouverture du fichier reussie, debut du traitement" << endl;
        fichier >> numberOfTestCases;

        //Traitement de chaque cas Test
        for(int i = 0; i<numberOfTestCases ;i++){

            //cout << "cas " << i+1 << endl;
            int nbGooglers;
            fichier >>nbGooglers;
            //cout << "nbGooglers" << nbGooglers << endl;
            int nbSurp;
            fichier >> nbSurp;
            int p;
            fichier >> p;
            int tmp;
            int nbREPONSE = 0;
            for(int j = 0; j<nbGooglers ;j++){
                fichier >> tmp;
                if(tmp == 0 && p==0 ){
                    nbREPONSE++;
                }
                else if(tmp==0 && p!=0){

                }
                else if( ((tmp/3)>p-1) || ( ((tmp/3)==p-1) && tmp%3!=0) ){

                    nbREPONSE++;

                }
                else if( nbSurp > 0 && (( (tmp/3)==p-1) || ( ((tmp/3)==p-2) && tmp%3==2) )){

                    nbREPONSE++;
                    nbSurp--;

                }
            }

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
