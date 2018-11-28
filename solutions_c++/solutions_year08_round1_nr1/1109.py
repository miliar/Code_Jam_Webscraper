#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <strstream> 

using namespace std;


void Sort(int* SRC, int LENGTH);
void SortB(int* SRC, int LENGTH);
int MakeMin(int*X, int *Y, int length);

typedef struct Lnode {
int data;
struct Lnode *next;
struct Lnode *last;
}Lnode,*Llist;

int main(int argc, char *argv[])
{
  ifstream filein("A-small-attempt4.in.txt");
  ofstream oFile( "1.out" );
  string casesin;
  int cases;
  string Nin;
  int N;
  getline(filein, casesin);
  cases = atoi(casesin.c_str());
//  cout << cases << endl;
  for (int i = 0; i < cases; i++)
  {
    filein >> Nin;
    N = atoi(Nin.c_str());
    int* X = new int[N];
    int* Y = new int[N];
    for(int i=0;i<N;i++)
    {
        string temp;
        filein>>temp;
        X[i] = atoi(temp.c_str());
    }
    for(int i=0;i<N;i++)
    {
        string temp;
        filein>>temp;
        Y[i] = atoi(temp.c_str());
    }
    Sort(X, N);
    SortB(Y, N);
    //int result = MakeMin(X,Y,N);
    int result = 0;
    for(int i=0;i<N;i++)
    {
        result += X[i] * Y[i];
    }
    cout << "result:";
    cout << result << endl;
    oFile << "Case #"<< i + 1 << ": "<<result << endl;
  }
  filein.close();
  system("PAUSE");	
  return 0;
}

/*MIN TO MAX*/
void Sort(int* SRC, int LENGTH)
{
    for(int i = 0; i < LENGTH; i++)
        for (int j = i+1; j<LENGTH; j++)
           if(SRC[j]< SRC[i])
           {
              int t = SRC[j];
              SRC[j] = SRC[i];
              SRC[i] = t;
           }
}
void SortB(int* SRC, int LENGTH)
{
    for(int i = 0; i < LENGTH; i++)
        for (int j = i+1; j<LENGTH; j++)
           if(SRC[j]> SRC[i])
           {
              int t = SRC[j];
              SRC[j] = SRC[i];
              SRC[i] = t;
           }
}

int MakeMin(int*X, int *Y, int length)
{
    Llist startX = new Lnode;
    Llist startY = new Lnode;
    startX->next = NULL;
    startY->next = NULL;
    Llist ptrX = startX;
    Llist ptrY = startY;
    Llist ptrXend = NULL;
    Llist ptrYend = NULL;
    for(int i = 0;i< length;i++)
    {
        Lnode *temp = ptrX;
        ptrX->next = new Lnode;
        ptrX = ptrX->next;
        ptrX->data = X[i];
        ptrX->last = temp;
        temp = ptrY;
        ptrY->next = new Lnode;
        ptrY = ptrY->next;
        ptrY->data = Y[i];
        ptrY->last = temp;
    }
    ptrXend = ptrX;
    ptrYend = ptrY;
    ptrX->next = NULL;
    ptrY->next = NULL;
    ptrX = startX->next;
    ptrY = startY->next;
    int result = 0;
    while(ptrX != NULL && ptrY != NULL)
    {
        if(ptrX->data < 0)
        {
          if(ptrX->data < ptrY->data)
          {
          result +=ptrX->data * ptrYend->data;
          ptrX = ptrX->next;
          if(ptrX != NULL)
          {
          delete(ptrX->last);
          ptrX->last = NULL;
          }
          ptrYend = ptrYend->last;
          if(ptrYend != NULL)
          {
          delete(ptrYend->next);
          ptrYend->next = NULL;
          }
          continue;
          }
        }       
        if(ptrY->data < 0)
        {
          result +=ptrY->data * ptrXend->data;
          ptrY = ptrY->next;
          if(ptrY != NULL)
          {
          delete(ptrY->last);
          ptrY->last = NULL;
          }
          ptrXend = ptrXend->last;
          if(ptrXend != NULL)
          {
          delete(ptrXend->next);
          ptrXend->next = NULL;
          }
          continue;
        }
        if(ptrX->data == 0)
        {
        if(ptrX->data < ptrY->data)
           {
          result +=ptrX->data * ptrYend->data;
          ptrX = ptrX->next;
          if(ptrX != NULL)
          {
          delete(ptrX->last);
          ptrX->last = NULL;
          }
          ptrYend = ptrYend->last;
          if(ptrYend != NULL)
          {
          delete(ptrYend->next);
          ptrYend->next = NULL;
          }
          continue;
          }
        }       
        if(ptrY->data == 0)
        {
          result +=ptrY->data * ptrXend->data;
          ptrY = ptrY->next;
          if(ptrY != NULL)
          {
          delete(ptrY->last);
          ptrY->last = NULL;
          }
          ptrXend = ptrXend->last;
          if(ptrXend != NULL)
          {
          delete(ptrXend->next);
          ptrXend->next = NULL;
          }
          continue;
        }
        if(ptrX->data > 0)
        {
          if(ptrX->data < ptrY->data)
           {
          result +=ptrX->data * ptrY->data;
          ptrX = ptrX->next;
          if(ptrX != NULL)
          {
          delete(ptrX->last);
          ptrX->last = NULL;
          }
          ptrY = ptrY->next;
          if(ptrY != NULL)
          {
          delete(ptrY->last);
          ptrY->last = NULL;
          }
          continue;
          }
        }
        if(ptrY->data > 0)
        {
          result +=ptrY->data * ptrX->data;
          ptrX = ptrX->next;
          if(ptrX != NULL)
          {
          delete(ptrX->last);
          ptrX->last = NULL;
          }
          ptrY = ptrY->next;
          if(ptrY != NULL)
          {
          delete(ptrYend->next);
          ptrYend->next = NULL;
          }
          continue;
        }
       
    }
    return result;
}

int getMax(Lnode* Src)
{
    Lnode* ptr = Src;
    if(ptr == NULL)
        return 0;
    while(ptr->next)
    {
        ptr = ptr->next;
    }
    return ptr->data;
}

int getMinOverZero(Lnode* Src)
{
    Lnode* ptr = Src;
    if(ptr == NULL)
        return 1/0;
    while(ptr->next)
    {
        ptr = ptr->next;
        if(ptr->data > 0)
          break;
    }
    return ptr->data;
}
