#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream stream("C:/B-small-attempt3.in");
    ofstream result("C:/result.txt");

if(stream && result)
{
    string line;
    int nb_cases, nb_googlers, sup_cases, lim, r;
    double tot;
    getline(stream, line);
    istringstream ss(line);
    ss >> nb_cases;
    for(int i=1; i<=nb_cases; i++)
    {
        r=0;
        stream  >> nb_googlers;
        stream >> sup_cases;
        stream >> lim;
        for(int j=0; j<nb_googlers; j++)
        {
            stream >> tot;
            tot/=3;
            if((ceil(tot))>=lim)
            {
                r++;
            }
            else if((ceil(tot)+1)>=lim && (ceil(tot)+1)<=10 && sup_cases>0  && tot!=0)
            {
                r++;
                sup_cases--;
            }
        }
         result << "Case #" << i << ": " << r;
         if(i!=nb_cases)
         {
             result << endl;
         }
    }
}
else
{
    result << "ERREUR: Impossible d'ouvrir le fichier en lecture." << endl;
}
    return 0;
}
