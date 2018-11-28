#include <iostream.h>

class Cell {
public:
    char group;
	Cell* sink;
    int Height;
    int l;
    int c;
    Cell(int l, int c) {
      this->l = l;
      this->c = c;
    }
};

Cell* matrix[100][100];
int hSize, vSize;
char lastGroup;

void initMatrix()
{
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++)
      matrix[i][j] = new Cell(i, j);  
}

void endMatrix()
{
  for (int i = 0; i < 100; i++)
    for (int j = 0; j < 100; j++)
      delete matrix[i][j];
}

void classifica(int lin, int col) 
{
  Cell* c = matrix[lin][col];

  if (c->group != 0)
    return;

  Cell* analise[4];
  if (lin == 0)
    analise[0] = NULL;
  else
    analise[0] = matrix[lin-1][col];
  
  if (col == 0)
    analise[1] = NULL;
  else
    analise[1] = matrix[lin][col-1];
    
  if (col == (vSize-1))
    analise[2] = NULL;
  else
    analise[2] = matrix[lin][col+1];
    
  if (lin == (hSize-1))
    analise[3] = NULL;
  else
    analise[3] = matrix[lin+1][col];

  int menor = c->Height;
  for (int i = 0; i < 4; i++)
  {
    Cell* an = analise[i];
    if (an != NULL)
    {
      if (an->Height < menor)
      {
        c->sink = an;
        menor = an->Height;
      }
    }
  }

  //É uma poça
  if (c->sink == NULL)
  {
    c->group = lastGroup++;
  }
  else
  { 
    classifica(c->sink->l, c->sink->c); 
    c->group = c->sink->group;
  } 
}

int main(void)
{
  initMatrix();
  int mapas;
  cin >> mapas;
  
  for (int iMapa = 0; iMapa < mapas; iMapa++)
  {
    cin >> hSize >> vSize;
    lastGroup = 'a';
        
    for (int lin = 0; lin < hSize; lin++)
    {
      for (int col = 0; col < vSize; col++)
      {
        int Height;
        cin >> Height;
        matrix[lin][col]->Height = Height;
        matrix[lin][col]->sink = NULL;
        matrix[lin][col]->group = 0;
      }
    }

    cout << "Case #" << (iMapa+1) << ":" << endl;
    
    for (int lin = 0; lin < hSize; lin++)
    {
      for (int col = 0; col < vSize; col++)
      {
        classifica(lin, col);        
        cout << matrix[lin][col]->group;
        if (col < vSize)
           cout << " ";
      }
      cout << endl;
    }
  }
  
  endMatrix();
  return 0;   
}
