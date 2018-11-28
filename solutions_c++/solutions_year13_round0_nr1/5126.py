#ifndef OBJET_H
#define OBJET_H

#include <string>
#include <fstream>
#include <iostream>

using namespace std;

class Objet
{
public:
    Objet();
    bool gagnant(char p);
    bool gameNotEnded();
    char tab[4][4];
    string solve();
};

#endif // OBJET_H
