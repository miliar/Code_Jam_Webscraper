//---------------------------------------------------------------------------

#include <vcl.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sys/timeb.h>
#include <math.h>

using namespace std;

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif

long tiempoinicial,tiempototal;

void iniciatiempo(void)
{
 struct timeb t;
 ftime(&t);
 tiempoinicial=(long) ((1000 * t.time) + t.millitm );
 tiempototal=0;
}

void iniciatiempociclo(void)
{
 struct timeb t;
 ftime(&t);
 tiempoinicial=(long) ((1000 * t.time) + t.millitm );
}

long tiempotranscurrido(void)
{
 long tiempoactual;
 struct timeb t;
 ftime(&t);
 tiempoactual=(long) ((1000 * t.time) + t.millitm );
 long res=tiempoactual-tiempoinicial;
 tiempoinicial=tiempoactual;
 tiempototal+=res;
 return tiempototal;
}
//***************************************************************************

int memoria[1001];
vector<string> cadenas;
vector<string> nombres;

int damemin(unsigned int pos)
{
  if (pos>=cadenas.size())
    return 0;
  if (memoria[pos]>=0)
    return memoria[pos];
  int min=1000;
  for (unsigned int i=0;i<nombres.size();i++)
   {
    if (cadenas[pos]==nombres[i])
     continue;
    unsigned int j=pos;
    while (j<cadenas.size())
     {
      if (nombres[i]==cadenas[j])
       {
        break;
       }
      j++;
     }
    if (j>=cadenas.size())
     {
      memoria[pos]=0;
      return memoria[pos];
     }
    int actual=damemin(j)+1;
    if (actual<min)
      min=actual;
   }
  return memoria[pos]=min;
}

int main(void)
{
  iniciatiempo();
  FILE *entrada=fopen("A-large.in","rt");
  FILE *salida=fopen("A-large.out","wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);
  char aux[102400];
  for (int c=1;c<=casos;c++)
  {
    int S,Q;
    fscanf(entrada,"%d\n",&S);
    nombres.resize(S);
    for (int i=0;i<S;i++)
    {
      nombres[i]=fgets(aux,102400,entrada);
    }
    fscanf(entrada,"%d\n",&Q);
    cadenas.resize(Q);
    for (int i=0;i<Q;i++)
    {
      cadenas[i]=fgets(aux,102400,entrada);
    }
    memset(memoria,-1,sizeof(memoria));
    fprintf(salida,"Case #%d: %d\n",c,damemin(0));
  }
  AnsiString mensaje;
  mensaje="Tiempo: "+IntToStr(tiempotranscurrido());
  Application->MessageBoxA(mensaje.c_str(),"Listo",MB_OK);
  fclose(salida);
  fclose(entrada);
}
//---------------------------------------------------------------------------
