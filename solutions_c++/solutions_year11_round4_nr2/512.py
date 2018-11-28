#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <complex>

using namespace std ;

const int Tm = 505 ;
typedef complex<double> cd ;
cd grille[Tm][Tm] ;
cd sum   [Tm][Tm] ;
int sumi [Tm][Tm] ;
int gri  [Tm][Tm] ;

char ligne[Tm] ;
int r,c,d;

bool check(int k)
{
//  printf("\n\n%d\n\n",k);
  for(int y = 0 ; y <= r-k ; y++ )
    for(int x = 0 ; x <= c-k ; x++ )
    {
       const cd tot = sum[y][x]+sum[y+k][x+k]-sum[y+k][x]-sum[y][x+k]-grille[y][x]-grille[y+k-1][x]-grille[y][x+k-1]-grille[y+k-1][x+k-1];
       const int toti = sumi[y][x]+sumi[y+k][x+k]-sumi[y+k][x]-sumi[y][x+k]-gri[y][x]-gri[y+k-1][x]-gri[y][x+k-1]-gri[y+k-1][x+k-1];
       const cd tot2 = cd(toti,0.)*(cd((double)x+(double)(k-1)/2.,(double)y+(double)(k-1)/2.));
       //printf("%d %d -> %lf,%lf  == %lf,%lf | %d\n ",x,y,tot.real(),tot.imag(),tot2.real(),tot2.imag(),toti);
       if(tot==tot2)
         return true ;
    }
  return false ;
}

void algo()
{
  fill(sumi[0],sumi[Tm],0);
  fill(sum[0],sum[Tm],cd(0.,0.));
  scanf("%d %d %d",&r,&c,&d);

  for(int y = 0 ; y < r ; y++ )
  {
     scanf("%s",ligne);
     for(int x = 0 ; x < c ; x++ )
     {
       grille[y][x] = cd(x,y)*cd(ligne[x]-'0',0) ;
       gri   [y][x] = ligne[x]-'0'; 
       //printf(">%d %lf %lf %d<",ligne[x]-'0',grille[y][x].real(),grille[y][x].imag(),gri[y][x]);
     }
  }
  for(int y = 0 ; y < r ; y++ )
  {
    cd tot = cd(0.,0.) ;  
    int toti =  0;
    for(int x = 0 ; x < c ; x++ )
    {
       toti+= gri   [y][x] ;
       tot += grille[y][x] ;
       sum [y+1][x+1] = sum [y][x+1] +tot;
       sumi[y+1][x+1] = sumi[y][x+1]+toti;
       //printf("%2.3lf,%2.3lf ",sum[y+1][x+1].real(),sum[y+1][x+1].imag());
    }
    //printf("\n");
  }
  for(int k = min(r,c) ; k > 2 ; k-- )
    if( check(k) )
      {
        printf("%d",k);
        return ;
      }
  printf("IMPOSSIBLE");
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int i = 1 ; i <= t ; i++ )
    {
      printf("Case #%d: ",i);
      algo();
      printf("\n");
    }
  return 0;
}
