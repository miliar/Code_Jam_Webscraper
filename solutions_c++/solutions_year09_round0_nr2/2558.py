/*
  Google Code Jam
  
  problema: Watersheds
  http://code.google.com/codejam/contest/dashboard?c=90101#s=p1
*/
#include <iostream.h>
#include <string.h>
#include <list.h>

class Celula {
public:
    char group;
	Celula* caida;
    int valor;
    int l;
    int c;
    Celula(int l, int c) {
      this->l = l;
      this->c = c;
    }
};

Celula* matriz[100][100];
int hMapa, wMapa;
char ultClassif;

void preparaMatriz()
{
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++)
      matriz[i][j] = new Celula(i, j);  
}

void destroiMatriz()
{
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++)
      delete matriz[i][j];
}

void classifica(int lin, int col) 
{
  Celula* c = matriz[lin][col];

  if (c->group != 0)
    return;

  Celula* analisar[4];
  if (lin == 0)
    analisar[0] = NULL;
  else
    analisar[0] = matriz[lin-1][col];
  
  if (col == 0)
    analisar[1] = NULL;
  else
    analisar[1] = matriz[lin][col-1];
    
  if (col == (wMapa-1))
    analisar[2] = NULL;
  else
    analisar[2] = matriz[lin][col+1];
    
  if (lin == (hMapa-1))
    analisar[3] = NULL;
  else
    analisar[3] = matriz[lin+1][col];

  int menor = c->valor;
  for (int i = 0; i < 4; i++)
  {
    Celula* an = analisar[i];
    if (an != NULL)
    {
      if (an->valor < menor)
      {
        c->caida = an;
        menor = an->valor;
      }
    }
  }

  //É uma poça
  if (c->caida == NULL)
  {
    c->group = ultClassif++;
  }
  else
  { 
    classifica(c->caida->l, c->caida->c); 
    c->group = c->caida->group;
  } 
}

int main(void)
{
  preparaMatriz();
  int mapas;
  cin >> mapas;
  
  for (int iMapa = 0; iMapa < mapas; iMapa++)
  {
    cin >> hMapa >> wMapa;
    ultClassif = 'a';
        
    for (int lin = 0; lin < hMapa; lin++)
    {
      for (int col = 0; col < wMapa; col++)
      {
        int valor;
        cin >> valor;
        matriz[lin][col]->valor = valor;
        matriz[lin][col]->caida = NULL;
        matriz[lin][col]->group = 0;
      }
    }

    cout << "Case #" << (iMapa+1) << ":" << endl;
    
    for (int lin = 0; lin < hMapa; lin++)
    {
      for (int col = 0; col < wMapa; col++)
      {
        classifica(lin, col);        
        cout << matriz[lin][col]->group;
        if (col < wMapa)
           cout << " ";
      }
      cout << endl;
    }
  }
  
  destroiMatriz();
  return 0;   
}
