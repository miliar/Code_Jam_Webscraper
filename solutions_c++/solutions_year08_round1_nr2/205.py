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

struct TCliente
{
  char preferencias[2000];
  int contadorlibres;
  int melted;
};

bool operator<(const TCliente &a,const TCliente &b)
{
  //preferir las que tienen menos libres
  if (a.contadorlibres!=b.contadorlibres)
  {
    return a.contadorlibres<b.contadorlibres;
  }
  //preferir las que tienen un melted cuando se puede
  return a.melted>b.melted;
}

char seleccion[2000];

int main(void)
{
  iniciatiempo();
  FILE *entrada=fopen("B-large.in","rt");
  FILE *salida=fopen("B-large.out","wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);

  for (int c=1;c<=casos;c++)
  {
    int N,M;
    fscanf(entrada,"%d\n",&N);
    fscanf(entrada,"%d\n",&M);
    memset(seleccion,'0',sizeof(seleccion));
    vector<TCliente> clientes;
    clientes.resize(M);
    for (int i=0;i<M;i++)
    {
      memset(clientes[i].preferencias,0,sizeof(clientes[i].preferencias));
      clientes[i].melted=-1;
      clientes[i].contadorlibres=0;
      int T;
      fscanf(entrada,"%d",&T);
      for (int t=0;t<T;t++)
      {
        int X,Y;
        fscanf(entrada," %d %d",&X,&Y);
        X--;
        if (Y==0)
        {
          clientes[i].preferencias[X]=1;
          clientes[i].contadorlibres++;
        }
        else
        {
          clientes[i].melted=X;
        }
      }
    }
    fprintf(salida,"Case #%d:",c);
    while (true)
    {
      if (clientes.size()==0)
      {
        //ya se puso todo
        for (int i=0;i<N;i++)
        {
          fprintf(salida," %c",seleccion[i]);
        }
        fprintf(salida,"\n");
        break;
      }
      sort(clientes.begin(),clientes.end());
      //ver si ya todas las que quedan pueden ser unmelted
      if (clientes[0].contadorlibres>0)
      {
        for (int i=0;i<N;i++)
        {
          fprintf(salida," %c",seleccion[i]);
        }
        fprintf(salida,"\n");
        break;
      }
      if (clientes[0].melted<0)
      {
        //no va melted pero todas sus opciones deben ir
        fprintf(salida," IMPOSSIBLE\n");
        break;
      }
      //esta debe ir melted
      seleccion[clientes[0].melted]='1';
      vector<TCliente> nuevos;
      nuevos.clear();
      for (int i=clientes.size()-1;i>0;i--)
      {
        if (clientes[0].melted==clientes[i].melted)
        {
          //este tambien va melted, no agregar
          continue;
        }
        //agregar a los nuevos
        nuevos.push_back();
        memcpy(&nuevos[nuevos.size()-1],&clientes[i],sizeof(clientes[i]));
        if (clientes[i].preferencias[clientes[0].melted]==1)
        {
          //una opcion menos porque este ya está en melted
          nuevos[nuevos.size()-1].contadorlibres--;
        }
      }
      clientes=nuevos;
    }
  }
  printf("Tiempo: %ld\n",tiempotranscurrido());
  fclose(salida);
  fclose(entrada);
}
//---------------------------------------------------------------------------
