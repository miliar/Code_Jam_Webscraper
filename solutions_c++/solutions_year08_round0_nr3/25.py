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
double sector(double radio,double x)
{
  double area=acos(x/radio)*radio*radio;
  area-=sqrt(x*x*(radio*radio-x*x));
  return area;
}

double calcula(double f,double R,double t,double r,double g)
{
  //la mosca no cabe en los huecos
  g-=2.0*f;
  if (g<=0.0)
   return 1.0;
  r+=f;
  double rint=R-(t+f);
  f=0.0;
  //sumar cuadro por cuadro
  double x=r;
  double area=0.0;
  while ((x*x+r*r)<((rint)*(rint)))
  {
    double y=r;
    while ((x*x+y*y)<(rint)*(rint))
    {
      if ((x*x+(y+g)*(y+g))>((rint)*(rint)))
      {
        //no cabe la izquierda (tampoco va a caber la esquina)
        if (((x+g)*(x+g)+(y*y))>((rint)*(rint)))
        {
          //no cabe ni la izquierda ni la derecha, calcular la integral hasta el punto de interseccion
          double lim=sqrt((rint)*(rint)-y*y);
          area+=(sector(rint,x)-sector(rint,lim));//agregar el sector circular
          area-=2.0*y*(lim-x);//quitar el rectángulo debajo de y
        }
        else
        {
          //calcular la integral en todo
          area+=(sector(rint,x)-sector(rint,x+g));//agregar el sector circular
          area-=2.0*y*g;//quitar el rectángulo debajo de y
        }
      }
      else if (((x+g)*(x+g)+(y*y))>((rint)*(rint)))
      {
        //cabe izquierda pero no derecha (tampoco esquina)
        double a=sqrt((rint)*(rint)-(y+g)*(y+g));
        area+=2.0*g*(a-x);
        double b=sqrt((rint)*(rint)-y*y);
        area+=(sector(rint,a)-sector(rint,b));//agregar el sector circular
        area-=2.0*y*(b-a);//quitar el rectángulo debajo de y
      }
      else if (((x+g)*(x+g)+(y+g)*(y+g))>((rint)*(rint)))
      {
        //cabe izquiera y derecha pero no esquina
        double a=sqrt((rint)*(rint)-(y+g)*(y+g));
        area+=2.0*g*(a-x);
        area+=(sector(rint,a)-sector(rint,x+g));//agregar el sector circular
        area-=2.0*y*(x+g-a);//quitar el rectángulo debajo de y
      }
      else
      {
        //cabe todo
        area+=2.0*g*g;
      }
      y+=g+2.0*r;
    }
    x+=g+2.0*r;
  }
  return 1.0-2.0*area/(M_PI*R*R);
}

int main(void)
{
  iniciatiempo();
  FILE *entrada=fopen("C-large.in","rt");
  FILE *salida=fopen("C-large.out","wt");
  int casos;
  fscanf(entrada,"%d\n",&casos);
  char aux[102400];
  for (int c=1;c<=casos;c++)
  {
    double f, R, t, r , g;
    fscanf(entrada,"%lf %lf %lf %lf %lf", &f, &R, &t, &r , &g);
    fprintf(salida,"Case #%d: %0.06lf\n",c,calcula(f, R, t, r, g));
  }
  printf("Tiempo: %ld\n",tiempotranscurrido());
  fclose(salida);
  fclose(entrada);
}
//---------------------------------------------------------------------------
