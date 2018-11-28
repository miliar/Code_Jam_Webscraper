/*
  Google Code Jam
  
  problema: Alien Language
  http://code.google.com/codejam/contest/dashboard?c=90101#s=p0
*/
#include <iostream.h>
#include <string.h>

bool existe(char* string, char caractere)
{
  int t = strlen(string);
  for (int i = 0; i < t; i++)
  {
    if (string[i] == caractere)
      return true;
  }
  return false;
}
int main(void)
{
  int tamanhoPalavra, qtdPalavras, casosTeste;
  cin >> tamanhoPalavra >> qtdPalavras >> casosTeste;
  
  char palavras[5000][15];
  
  for (int i = 0; i < qtdPalavras; i++)
  {
      cin >> palavras[i];
      //cout << palavras[i] << endl;
  }
    
  for (int i = 0; i < casosTeste; i++)
  {
      int result = qtdPalavras;    
      char teste[256];
      char matriz[256][256];
      
      cin >> teste;
      int t = strlen(teste);
      int x = 0, y = 0;
      bool abrePar = false;
      for (int j = 0; j < t; j++)
      {
          if (teste[j] == '(')
          {
             abrePar = true;
             continue;
          }
          else if (teste[j] == ')')
          {
             abrePar = false;
             x++;
             y = 0;
             continue;
          }             
          matriz[x][y] = teste[j];
          matriz[x][y+1] = '\0';          
          if (abrePar)
             y++;
          else
             x++;
      }
      
      //for (int ix = 0; ix < x; ix++)
        //  cout << matriz[ix] << endl;
      
      for (int iPalavra = 0; iPalavra < qtdPalavras; iPalavra++)
      {
          bool ok = true;
          for (int iLetra = 0; iLetra < tamanhoPalavra; iLetra++)
          {       
              if (!existe(matriz[iLetra], palavras[iPalavra][iLetra]))
              {
                 ok = false;
                 break;
              }
          }
          if (!ok)
             result--;
      }     
      
      cout << "Case #" << (i + 1) << ": " << result << endl;
  }
}
