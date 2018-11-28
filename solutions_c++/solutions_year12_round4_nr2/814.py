#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
const int nb_vaches_max = 1000+10 ;
const int nb_iter_max = 50000  ;
 
int nb_vaches ;
double Sx , Sy ;
int Xmax , Ymax ;
int longueur_bras[nb_vaches_max] ;
 
inline double carre( double a)
{
  return a*a;
}
 
struct point
{
  point( double a = 0 , double b = 0 ) : x(a),y(b) { }
  double x , y ;
};
 
inline double note( double d, double d2 )
{
  const double eps = 0.5 ;
  d2 = d2*d2 ;
  if(d < d2+eps )
    return d2-d ;
  else
    return 0. ;
}
 
void set_inter( double & val , int min , int max )
{
  if( val < min )
    val = min ;
  if( val > max )
    val = max ;
 
}
 
double dist ( point a , point b)
{
  return carre(a.x - b.x) + carre(a.y - b.y);
}
 
struct element
{
  point v[ nb_vaches_max ];
  double score ;
 
  void noter()
  {
    score = 0 ;
    for( int v1 = 0 ; v1 < nb_vaches ; v1++ )
      for(int v2 = v1+1 ; v2 < nb_vaches ; v2++ )
	score += note( dist(v[v1],v[v2]),longueur_bras[v1]+longueur_bras[v2]);
  }


  element ()
  {
 
    for( int vache = 0 ; vache < nb_vaches ; vache++ )
      v[ vache ] = point( 0 , 0 );
    noter();
  }

 
  void update()
  {
    int vache = rand()%nb_vaches ;
    v[ vache ].x += Sx * double(rand()%3 - 1)  ;
    v[ vache ].y += Sy * double(rand()%3 - 1) ;
 
    set_inter( v[vache].x , 0 , Xmax );
    set_inter( v[vache].y , 0 , Ymax );
    noter();
  }
 
  void aff()
  {
    for( int vache = 0 ; vache < nb_vaches ; vache++ )
      printf("%.2lf %.2lf%c", v[ vache ].x ,v[ vache ].y,vache==nb_vaches-1?'\n':' ');
  }
};
 
 
element recuit()
{
  element r_best ;
  double temp = 1000 * 1000 ; 
  while(true)
    {
 
      Sx = Xmax ;
      Sy = Ymax ;
      temp = 1000 * 1000  ;
      element cur;
      cur.update();
      element best = cur ;
      int nb_iter = 0;
 
      while( nb_iter < nb_iter_max )
	{
	  if(r_best.score == 0. )
	    return r_best ;
		  

	  cur = best;
	  cur.update();
 
	  if( cur.score < best.score || ((double(rand())/RAND_MAX) < (cur.score-best.score) * temp / (1000*1000) ))
	    {
	      best = cur ;
	      if( best.score < r_best.score )
		{
		  r_best = best;
		  		}
	    }
	  temp *= 0.9995 ;
	  Sx   *= 0.9995 ;
	  Sy   *= 0.9995 ;
	  nb_iter++;
	}
    }
}

void algo()
{
  srand( 405 );
  scanf("%d %d %d",&nb_vaches , &Xmax , &Ymax );
  for( int i = 0 ; i < nb_vaches ; i++ )
    scanf("%d",longueur_bras+i);
  element e = recuit();
  e.aff();
}
 
int main()
{
  int T ;
  scanf("%d",&T);
  for( int i = 0 ; i < T ; i++ )
    {
      printf("Case #%d: ",i+1);
      algo();
    }
 return 0;
}
