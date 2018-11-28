#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <tuple>

using namespace std ;

int X, S,R,ti,N;
double t ;
void algo()
{
  scanf("%d %d %d %d %d",&X,&S,&R,&ti,&N);
  t = ti;
  vector< tuple<int,int,int> > walks; 
  vector< tuple<int,int,int> > inter; 
  for(int i = 0 ; i < N ; i++ )
    {
      int b,e,w;
      scanf("%d %d %d",&b,&e,&w);
      walks.push_back(tuple<int,int,int>(b,e,w));
    }
  sort(walks.begin(),walks.end());
  int prec = 0;
  for( size_t i = 0 ; i < walks.size() ; i++ )
  {
    tuple<int,int,int> x = walks[i];
    inter.push_back(tuple<int,int,int>(S,prec,get<0>(x)));  
    inter.push_back(tuple<int,int,int>(S+get<2>(x),get<0>(x),get<1>(x)));
    prec = (get<1>(x));  
  }
  inter.push_back(tuple<int,int,int>(S,prec,X));
  sort(inter.begin(),inter.end());
  double tps = 0. ;
  for( size_t i = 0 ; i < inter.size() ; i++ )
  {
    tuple<int,int,int> x = inter[i];

    const double vitesse = R-S+(get<0>(x)) ;
    const double dist = get<2>(x)-get<1>(x);
    const double couru = min(dist/vitesse,t) ;
    t-=couru;
    tps += couru + (dist-vitesse*couru)/(get<0>(x)) ;
  }
  printf("%.10lf",tps);
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int i = 1 ; i <= t ; i++ )
    {
      printf("Case #%d:",i);
      algo();
      printf("\n");
    }
  return 0;
}
