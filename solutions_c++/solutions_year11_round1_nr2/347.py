//---------------------------------------------------------------------------

#include <stdio.h>
#include <mem.h>
#pragma hdrstop

//---------------------------------------------------------------------------
char D[10000][11];
char letras[30];
char tam[10000],pasos[10000];
char *FirstNonCommon;
int N,M;
int portamano[10][10000];
int conttamano[10];
int possible[2][10000];
int Npos;

#pragma argsused
int main(int argc, char* argv[])
{
  int T;
  scanf("%d\n",&T);
  for (int t=1;t<=T;t++)
  {
    //get dictionary
    scanf("%d %d\n",&N,&M);
    for (int i=0;i<10;i++)
    {
      conttamano[i]=0;
    }
    for (int i=0;i<N;i++)
    {
      scanf("%s\n",D[i]);
      int pos=0;
      while (D[i][pos]!=0)
        pos++;
      tam[i]=pos;
      portamano[pos-1][conttamano[pos-1]]=i;
      conttamano[pos-1]++;
    }
    printf("Case #%d:",t);
    for (int m=0;m<M;m++)
    {
      scanf("%s\n",letras);
      int mejor=0;
      int mejorpuntos=0;
      for (int tam=1;tam<=10;tam++)
      {
        N=conttamano[tam-1];
        for (int j=0;j<N;j++)
        {
          int ID=portamano[tam-1][j];
          char mascara[10];
          memcpy(possible[0],portamano[tam-1],sizeof(possible[0][0])*N);
          int puntos=0;
          int P=N;
          int pos=0;
          int faltan=tam;
          while ((P>1)&&(faltan>0))
          {
            int inc=1;
            for (int i=0;i<tam;i++)
            {
              if (D[ID][i]==letras[pos])
              {
                mascara[i]=1;
                faltan--;
                inc=0;
              }
              else
              {
                mascara[i]=0;
              }
            }

            int NP=0;
            bool letraesta=false;
            for (int k=0;k<P;k++)
            {
              //quitar las palabras incompatibles
              bool dejar=true;
              int ID2=possible[pos&1][k];
              for (int i=0;i<tam;i++)
              {
                if ((mascara[i]==1)&&(letras[pos]!=D[ID2][i]))
                {
                  dejar=false;
                }
                if ((mascara[i]==0)&&(letras[pos]==D[ID2][i]))
                {
                  dejar=false;
                }
                if (D[ID2][i]==letras[pos])
                {
                  letraesta=true;
                }
              }
              if (dejar)
              {
                possible[(pos&1)^1][NP]=ID2;
                NP++;
              }
            }
            P=NP;
            if (letraesta)
            {
              puntos+=inc;
            }
            pos++;
          }
          if (puntos>mejorpuntos)
          {
            mejorpuntos=puntos;
            mejor=ID;
          }
          else if (puntos==mejorpuntos)
          {
            if (mejor>ID)
            {
              mejor=ID;
            }
          }
        }
      }
      printf(" %s",D[mejor]);
    }

    printf("\n");
  }
  return 0;
}
//---------------------------------------------------------------------------

