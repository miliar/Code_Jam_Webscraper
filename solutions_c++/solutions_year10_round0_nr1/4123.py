#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(int argc, char *argv[])
{
    //File-Inputstream festlegen
    fstream fin;
    fin.open("A-large.in", ios::in);
    
    //File-Outputstream festlegen
    fstream fout;
    fout.open("output.txt", ios::out);
    
    //AnzahlTestFälle 
    int cases;
    fin >> cases;
    
    //Parameter N und K
    int n,k;
    //Ergebnisvariable
    bool ergebnis;
    int zwischenZahl;
    int zaehler=0;
    
    while(cases != 0)
    {
        zaehler++;        
                
        //Daten einlesen
        fin >> n;
        fin >> k;
        

        zwischenZahl = (pow(2.0,n));
        ergebnis = ((k%zwischenZahl)==(zwischenZahl-1));
        
        cases --;
        
        if(ergebnis)  fout << "Case #" << zaehler << ": ON" << endl;
        if(!ergebnis) fout << "Case #" << zaehler << ": OFF" << endl;
    }
    fin.close();
    fout.close();
}
