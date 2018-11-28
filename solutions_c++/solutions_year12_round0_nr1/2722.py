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
    ifstream fichier("A-small-attempt2.in"); //ouverture du fichier
    //ifstream fichier("A-large-practice.in"); //ouverture du fichier

    if(fichier){



        int numberOfTestCases; //le nombre total de cas à tester (premiere ligne de chaque input file
        cout << "Ouverture du fichier reussie, debut du traitement" << endl;
        fichier >> numberOfTestCases;
        cout << numberOfTestCases;

        char c;

        string ligne;
        getline(fichier,ligne); //Lecture de la fin de la ligne 0

        //Traitement de chaque cas Test
        for(int i = 0; i<numberOfTestCases ;i++){
            ostringstream oss2;

            getline(fichier,ligne); //Lecture de la premiere ligne

            for(int j = 0; j<ligne.length(); j++){
                if(ligne[j]==' ')
                    oss2<< ' ';
                else if(ligne[j]=='e')
                    oss2<< 'o';
                else if(ligne[j]=='j')
                    oss2<< 'u';
                else if(ligne[j]=='p')
                    oss2<< 'r';
                else if(ligne[j]=='m')
                    oss2<< 'l';
                else if(ligne[j]=='y')
                    oss2<< 'a';
                else if(ligne[j]=='s')
                    oss2<< 'n';
                else if(ligne[j]=='l')
                    oss2<< 'g';
                else if(ligne[j]=='c')
                    oss2<< 'e';
                else if(ligne[j]=='k')
                    oss2<< 'i';
                else if(ligne[j]=='d')
                    oss2<< 's';
                else if(ligne[j]=='x')
                    oss2<< 'm';
                else if(ligne[j]=='v')
                    oss2<< 'p';
                else if(ligne[j]=='n')
                    oss2<< 'b';
                else if(ligne[j]=='r')
                    oss2<< 't';
                else if(ligne[j]=='i')
                    oss2<< 'd';
                else if(ligne[j]=='p')
                    oss2<< 'r';
                else if(ligne[j]=='b')
                    oss2<< 'h';
                else if(ligne[j]=='t')
                    oss2<< 'w';
                else if(ligne[j]=='a')
                    oss2<< 'y';
                else if(ligne[j]=='h')
                    oss2<< 'x';
                else if(ligne[j]=='w')
                    oss2<< 'f';
                else if(ligne[j]=='f')
                    oss2<< 'c';
                else if(ligne[j]=='u')
                    oss2<< 'j';
                else if(ligne[j]=='g')
                    oss2<< 'v';
                else if(ligne[j]=='o')
                    oss2<< 'k';
                else if(ligne[j]=='z')
                    oss2<< 'q';
                else if(ligne[j]=='q')
                    oss2<< 'z';

            }
                cout << oss2.str() << endl;
            // Traitement du test case
            oss << "Case #" << (i+1) << ": " << oss2.str() << endl;
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
