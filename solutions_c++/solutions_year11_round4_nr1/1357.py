#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

struct Tt {
  int b;
  int e;
  int w;
};

bool myfunction (Tt i,Tt j) { return (i.w<j.w); }

Tt lis[1010];

int main(){

  int TT;
  scanf("%d", &TT);
  for(int T = 0; T < TT; T++){
    
    int x, s, r, t , n;
    int b, e, w;
    double eps=1e-8;
    scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
    int wdist=0;
    double wtime =0.0;

    for(int i=0; i<n; i++){
      scanf("%d %d %d", &lis[i].b, &lis[i].e, &lis[i].w);
	wdist += lis[i].e - lis[i].b;
	wtime += ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+s));
    }
    
    sort(lis, lis+n, myfunction);
    double ti = (double)t;
    
    //ce ne bo tekel po tekocih
    if((double)(x-wdist)/r >= ti-eps){
      double diss = ti*r;
      wtime += ti;
      wtime += (double)(x-wdist-diss)/s;
      printf("Case #%d: %.10f\n", T+1, wtime);
    } else {
      ti -= (double)(x-wdist)/r;
      wtime += (double)(x-wdist)/r;
      
     // cout << wtime << endl;
      for(int i=0; i<n; i++){
	if(ti<eps) break;
	if(ti >= ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+r))){
	  //ce lohk runn all way
	  ti -= ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+r));
	  wtime -= ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+s));
	  wtime += ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+r));
	} else {
	  //lohk samo del poti
	  double diss = ti*(r+lis[i].w);
	  wtime -= ((double)(lis[i].e-lis[i].b))/((double)(lis[i].w+s));
	  wtime += ((double)(lis[i].e-lis[i].b-diss))/((double)(lis[i].w+s));
	  wtime += ((double)(diss))/((double)(lis[i].w+r));
	  break;
	}
      }
      
      printf("Case #%d: %.10f\n", T+1, wtime);
    }


    
      
   /* for(int i=0; i<n; i++){
      printf("%d %d %d\n", l[i].b, l[i].e, l[i].w);
    }*/
    
    
    //printf("Case #%d: %d\n", T+1, 2);
  }
  
  return 0;
}