//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
  : TForm(Owner)
{
}
//---------------------------------------------------------------------------

int sort_function_normal( const void *a, const void *b)
{
   return *((int *)a)-*((int *)b);
}
//---------------------------------------------------------------------------

int sort_function_inverso( const void *a, const void *b)
{
   return *((int *)b)-*((int *)a);
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
  int n, NumCasos, k, j, tam_vet, total;
  long double ipart;
  FILE *fin=fopen("p:\\A-small-attempt1.in", "r");
  FILE *fout=fopen("p:\\saida.txt", "w");
  fscanf(fin, "%d", &NumCasos);
  int x[1000], y[1000];
  for (n=0; n<NumCasos; n++)
  {
    fscanf(fin, "%d", &tam_vet);
    for (k=0; k<tam_vet; k++)
      fscanf(fin, "%d", &(x[k]));
    for (k=0; k<tam_vet; k++)
      fscanf(fin, "%d", &(y[k]));
    qsort(x, tam_vet, sizeof(int), sort_function_normal);
    qsort(y, tam_vet, sizeof(int), sort_function_inverso);
    total=0;
    for (k=0; k<tam_vet; k++)
      total+=x[k]*y[k];
    fprintf(fout, "Case #%d: %d\n", n+1, total);
  }
  fclose(fin);
  fclose(fout);  
}
//---------------------------------------------------------------------------
