/*
  Google Code Jam
  
  problema: Welcome to Code Jam
  http://code.google.com/codejam/contest/dashboard?c=90101#s=p2
*/
#include <iostream.h>
#include <string.h>

char Welcome[20] = "welcome to code jam";
int MaxNivel = 18;

int qtvezes(char* frase, int &tamFrase, int pontoIni, int nivel)
{
    //cout << "Nivel: " << nivel << endl;
    if (nivel > MaxNivel)
        return 1;
        /*
    {
       int result = 0;
       for(int i = pontoIni; i < tamFrase; i++)
           if (Welcome[nivel] == frase[i])
               result++;
       return result;
    }*/
    //cout << frase << "   " << tamFrase << "  " << pontoIni << "  " << nivel << endl;
    int result = 0;
    for(int i = pontoIni; i < tamFrase; i++)
    {
        if (Welcome[nivel] == frase[i])
        {
            //cout << frase[i];
            result += qtvezes(frase, tamFrase, i + 1, nivel + 1);
            //cout << endl;
        }
    }

    return result;
}
int main(void)
{
    int qtdTestes;
    cin >> qtdTestes;
    cin.ignore();    
    for (int iTeste = 0; iTeste < qtdTestes; iTeste++)
    {
        char frase[512];
        cin.getline(frase, 512);
        //cout << "Frase:" << frase << endl;
        //return 0;
        int t = strlen(frase);
        int qt = qtvezes(frase, t, 0, 0);
        printf("Case #%d: %04d\n", iTeste+1, qt);
        //cout << "Case #" << (iTeste + 1) << ": " << qt << endl;
    }
}
