//---------------------------------------------------------------------------

#include <vcl.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
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

struct Tviaje
{
  int salida,llegada;
  int estacionsalida;
};

bool operator<(const Tviaje &a,const Tviaje &b)
{
  if (a.salida!=b.salida)
   return a.salida<b.salida;
  if (a.llegada!=b.llegada)
   return a.llegada<b.llegada;
  return a.estacionsalida<b.estacionsalida;
}

int main(void)
{
  iniciatiempo();
  FILE *entrada=fopen("B-large.in","rt");
  FILE *salida=fopen("B-large.out","wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);
  char aux[102400];
  for (int c=1;c<=casos;c++)
  {
    vector<Tviaje> viajes;
    viajes.clear();
    int tiempovuelta,NA,NB;
    fscanf(entrada,"%d\n%d %d\n",&tiempovuelta,&NA,&NB);
    viajes.resize(NA+NB);
    for (int i=0;i<NA;i++)
    {
      int hsal,msal,hlle,mlle;
      fscanf(entrada,"%d:%d %d:%d\n",&hsal,&msal,&hlle,&mlle);
      viajes[i].salida=hsal*60+msal;
      viajes[i].llegada=hlle*60+mlle+tiempovuelta;
      viajes[i].estacionsalida=0;
    }
    for (int i=0;i<NB;i++)
    {
      int hsal,msal,hlle,mlle;
      fscanf(entrada,"%d:%d %d:%d\n",&hsal,&msal,&hlle,&mlle);
      viajes[NA+i].salida=hsal*60+msal;
      viajes[NA+i].llegada=hlle*60+mlle+tiempovuelta;
      viajes[NA+i].estacionsalida=1;
    }
    sort(viajes.begin(),viajes.end());
    int trenes[2];
    trenes[0]=trenes[1]=0;
    vector<int> llegadas[2];
    llegadas[0].clear();
    llegadas[1].clear();
    unsigned int poslle[2];
    unsigned int pos=0;
    poslle[0]=poslle[1]=0;
    while (pos<viajes.size())
    {
      if (llegadas[viajes[pos].estacionsalida].size()<=poslle[viajes[pos].estacionsalida])
      {
        //no hay trenes en espera, agregar un tren más
        trenes[viajes[pos].estacionsalida]++;
      }
      else if (llegadas[viajes[pos].estacionsalida][poslle[viajes[pos].estacionsalida]]>viajes[pos].salida)
      {
        //van allegar trenes después, agregar uno más
        trenes[viajes[pos].estacionsalida]++;
      }
      else
      {
        //hay trenes en espera
        poslle[viajes[pos].estacionsalida]++;
      }
      //agregar la llegada de este tren a la estacion de llegada
      llegadas[1-viajes[pos].estacionsalida].push_back(viajes[pos].llegada);
      sort(llegadas[1-viajes[pos].estacionsalida].begin(),llegadas[1-viajes[pos].estacionsalida].end());
      pos++;
    }
    fprintf(salida,"Case #%d: %d %d\n",c,trenes[0],trenes[1]);
  }
  AnsiString mensaje;
  mensaje="Tiempo: "+IntToStr(tiempotranscurrido());
  Application->MessageBoxA(mensaje.c_str(),"Listo",MB_OK);
  fclose(salida);
  fclose(entrada);
}
//---------------------------------------------------------------------------
