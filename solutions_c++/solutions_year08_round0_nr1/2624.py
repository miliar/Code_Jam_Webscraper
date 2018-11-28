#include <stdio>
#include <string>

int main(void)
{
  int NumCasos, n, k, j, NumSE, NumQueries, num_usadas, num_precisa;

  FILE *fin=fopen("p:\\A-large.in", "r");
  FILE *fout=fopen("p:\\saida.txt", "w");
  char ListaSE[100][100], ListaQueries[1000][100], *query;
  bool BoolSE[100];
  fscanf(fin, "%d", &NumCasos);
  for (n=0; n<NumCasos; n++)
  {
    fscanf(fin, "%d", &NumSE);
    fgetc(fin);
    for (k=0; k<NumSE; k++)
    {
      memset(ListaSE[k], 0, 100);
      fgets(ListaSE[k], 100, fin);
    }

    fscanf(fin, "%d", &NumQueries);  
    fgetc(fin);
    for (k=0; k<NumQueries; k++)
    {
      memset(ListaQueries[k], 0, 100);
      fgets(ListaQueries[k], 100, fin);
    }

    num_usadas=num_precisa=0;
    memset(BoolSE, 0, 100*sizeof(bool));
    for (k=0; k<NumQueries; k++)
    {
      query=ListaQueries[k];
      for (j=0; j<NumSE; j++)
      {
        if (!strcmp(query, ListaSE[j]))
        {
          if (!BoolSE[j])
          {
            BoolSE[j]=true;
            num_usadas++;
            if (num_usadas==NumSE)
            {      
              num_usadas=1;
              memset(BoolSE, 0, 100*sizeof(bool));
              BoolSE[j]=true;
              num_precisa++;
            }
          }   
          break;
        }
      }
    }
    fprintf(fout, "Case #%d: %d\n", n+1, num_precisa);
  }
  printf("%d", n);
  fclose(fin);
  fclose(fout);
}     
//---------------------------------------------------------------------------
