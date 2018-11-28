#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


char translateChar(char ch)
{
    char tab1[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
    int tab2[27] = {24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16,26};

    int f(0);
    while (tab1[f] != ch)
    {
        ++f;
    }
    return tab1[tab2[f]];

}

int main()
{
    ifstream infile("A.in");  //Ouverture d'un fichier en lecture

    if(!infile)
    {
        cout << "ERREUR: Impossible d'ouvrir le fichier en lecture." << endl;
    }

    ofstream outfile("A.out"); //On essaye d'ouvrir le fichier

    if(!outfile)
    {
        cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
    }

    string g[100];

    getline(infile,g[0]);

    int testCases = atoi(g[0].c_str());

    for(int t(1);t <= testCases;++t)
    {
        getline(infile,g[t]);
        for (int s(0);s < g[t].size();++s)
        {
            g[t][s] = translateChar(g[t][s]);
        }
        outfile << "Case #" << t << ": " << g[t] << endl;
    }









    return 0;
}
