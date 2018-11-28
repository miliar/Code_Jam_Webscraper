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


int memoria[10001][2];//minimo de pasos para lograr que el nodo tenga cierto estado
int nodo[10001][2];
int M;

const int infinito=-2;

int dameminimo(int n,int estado)
{
  if (n>((M-1)/2))
  {
    //es una hoja
    return memoria[n][estado];
  }
  if (memoria[n][estado]==infinito)
  {
    return infinito;
  }
  if (memoria[n][estado]>=0)
  {
    return memoria[n][estado];
  }
  //no se ha calculado
  if (nodo[n][1]==0)
  {
    //no cambiar
    if (nodo[n][0]==0)
    {
      //or
      if (estado==0)
      {
        if (dameminimo(2*n+1,0)==infinito)
        {
          return infinito;
        }
        if (dameminimo(2*n,0)==infinito)
        {
          return infinito;
        }
        return memoria[n][estado]=dameminimo(2*n,0)+dameminimo(2*n+1,0);
      }
      //estado=1
      memoria[n][estado]=dameminimo(2*n,1);
      if (memoria[n][estado]==infinito)
      {
        return memoria[n][estado]=dameminimo(2*n+1,1);
      }
      if (dameminimo(2*n+1,1)!=infinito)
      {
        if (dameminimo(2*n,1)>dameminimo(2*n+1,1))
        {
          return memoria[n][estado]=dameminimo(2*n+1,1);
        }
      }
      return memoria[n][estado];
    }
    else
    {
      //and
      if (estado==1)
      {
        if (dameminimo(2*n+1,1)==infinito)
        {
          return infinito;
        }
        if (dameminimo(2*n,1)==infinito)
        {
          return infinito;
        }
        return memoria[n][estado]=dameminimo(2*n,1)+dameminimo(2*n+1,1);
      }
      //estado=0
      memoria[n][estado]=dameminimo(2*n,0);
      if (memoria[n][estado]==infinito)
      {
        return memoria[n][estado]=dameminimo(2*n+1,0);
      }
      if (dameminimo(2*n+1,0)!=infinito)
      {
        if (dameminimo(2*n,0)>dameminimo(2*n+1,0))
        {
          return memoria[n][estado]=dameminimo(2*n+1,0);
        }
      }
      return memoria[n][estado];
    }
  }
  //se puede cambiar
  memoria[n][estado]=infinito;
  if (estado==0)
  {
    //and con alguno 0
    if (dameminimo(2*n,0)!=infinito)
    {
      if (dameminimo(2*n+1,0)==infinito)
      {
        memoria[n][estado]=1+dameminimo(2*n,0)-nodo[n][0];
      }
      else
      {
        if (dameminimo(2*n,0)<dameminimo(2*n+1,0))
        {
          memoria[n][estado]=1+dameminimo(2*n,0)-nodo[n][0];
        }
        else
        {
          memoria[n][estado]=1+dameminimo(2*n+1,0)-nodo[n][0];
        }
      }
    }
    else
    {
      if (dameminimo(2*n+1,0)!=infinito)
      {
        memoria[n][estado]=1+dameminimo(2*n+1,0)-nodo[n][0];
      }
    }

    //or con 2 ceros
    if ((dameminimo(2*n,0)!=infinito)&&(dameminimo(2*n+1,0)!=infinito))
    {
      int res=nodo[n][0]+dameminimo(2*n,0)+dameminimo(2*n+1,0);
      if (memoria[n][estado]==infinito)
      {
        memoria[n][estado]=res;
      }
      else
      {
        if (res<memoria[n][estado])
        {
          memoria[n][estado]=res;
        }
      }
    }
  }
  else
  {
    //or con alguno 1
    if (dameminimo(2*n,1)!=infinito)
    {
      if (dameminimo(2*n+1,1)==infinito)
      {
        memoria[n][estado]=dameminimo(2*n,1)+nodo[n][0];
      }
      else
      {
        if (dameminimo(2*n,1)<dameminimo(2*n+1,1))
        {
          memoria[n][estado]=dameminimo(2*n,1)+nodo[n][0];
        }
        else
        {
          memoria[n][estado]=dameminimo(2*n+1,1)+nodo[n][0];
        }
      }
    }
    else
    {
      if (dameminimo(2*n+1,1)!=infinito)
      {
        memoria[n][estado]=dameminimo(2*n+1,1)+nodo[n][0];
      }
    }
    //and con 2 unos
    if ((dameminimo(2*n,1)!=infinito)&&(dameminimo(2*n+1,1)!=infinito))
    {
      int res=1-nodo[n][0]+dameminimo(2*n,1)+dameminimo(2*n+1,1);
      if (memoria[n][estado]==infinito)
      {
        memoria[n][estado]=res;
      }
      else
      {
        if (res<memoria[n][estado])
        {
          memoria[n][estado]=res;
        }
      }
    }
  }
  return memoria[n][estado];
}



int main(void)
{
  iniciatiempo();
  string nombre="A-large";
  FILE *entrada=fopen((nombre+".in").c_str(),"rt");
  FILE *salida=fopen((nombre+".out").c_str(),"wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);
  char aux[102400];
  for (int c=1;c<=casos;c++)
  {
    memset(memoria,-1,sizeof(memoria));
    int V;
    fscanf(entrada,"%d %d",&M,&V);
    for (int i=1;i<=(M-1)/2;i++)
    {
      fscanf(entrada,"%d %d",&nodo[i][0],&nodo[i][1]);
    }
    for (int i=1;i<=(M+1)/2;i++)
    {
      int est;
      fscanf(entrada,"%d",&est);
      memoria[i+(M-1)/2][est]=0;
      memoria[i+(M-1)/2][1-est]=infinito;
    }
    fprintf(salida,"Case #%d: ",c);
    if (dameminimo(1,V)==infinito)
    {
      fprintf(salida,"IMPOSSIBLE\n");
    }
    else
    {
      fprintf(salida,"%d\n",dameminimo(1,V));
    }
  }
  printf("Tiempo: %ld\n",tiempotranscurrido());
  fclose(salida);
  fclose(entrada);
  return 0;
}
//---------------------------------------------------------------------------
