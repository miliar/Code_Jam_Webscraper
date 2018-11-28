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



int main(void)
{
  iniciatiempo();
  FILE *entrada=fopen("A-small-attempt0.in","rt");
  FILE *salida=fopen("A-small-attempt0.out","wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);
  char aux[102400];
  for (int c=1;c<=casos;c++)
  {
    int n;
    fscanf(entrada,"%d",&n);
    vector<int> A,B;
    A.resize(n);
    B.resize(n);
    for (int i=0;i<n;i++)
    {
      fscanf(entrada,"%d",&A[i]);
    }
    sort(A.begin(),A.end());
    for (int i=0;i<n;i++)
    {
      fscanf(entrada,"%d",&B[i]);
    }
    sort(B.begin(),B.end());
    int64 res=0.0;
    for (int i=0;i<n;i++)
    {
      res+=((int64)A[i])*((int64)B[(n-i)-1]);
    }
    fprintf(salida,"Case #%d: %lld\n",c,res);
  }
  printf("Tiempo: %ld\n",tiempotranscurrido());
  fclose(salida);
  fclose(entrada);
}
//---------------------------------------------------------------------------
