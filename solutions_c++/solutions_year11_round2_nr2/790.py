#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;
typedef unsigned int uInt;
typedef long long int llInt;

int C, D;
int V;
double H[1048576];

double abs(double x) {return (x<0.0)?-x:x;}

double min(double x, double y){
  if(x<y) return x;
  return y;  
}
double max(double x, double y){
  if(x>y) return x;
  return y;  
}

bool can_be(double dist){
    double last = H[0] - dist;
    //cout << "can_be("<< dist << ")" << endl;
    //cout << "last= " << last << endl;
    
    for(int i=1; i<V; i++){
      last = max(H[i]-dist, last + D);
      if(last - dist - H[i] > 0.0) return false;
      //cout << "last= " << last << endl;
    }  
    return true;
}

#define M1_3 0.333333333333
#define M2_3 0.666666666666
double min_diff = 0.0000001;

double bin_search(double from, double to){
  
  if(from == to || (to - from - min_diff <= 0)) return from;
  //cout << "bin_search("<<from << "," << to << ") : " << to - from << endl;
  
  double mid = (from + to) / 2.0;
  if(can_be(mid)) return bin_search(from, mid);
  else            return bin_search(mid, to);
}

int main()
{
  int T;
  scanf("%d", &T);
  
  REP(t, T){
    V=0;
    int min_p;
    int max_p;
      
    scanf("%d%d", &C, &D);
    REP(c, C){
      int p, v;
      scanf("%d%d", &p, &v);
      if(p>max_p) max_p=p;
      if(p<min_p) min_p=p;
      
      REP(i, v)   {
        H[V++] = (double) p;  
      }
    }
    
    llInt length = ((llInt)(V-1))*((llInt)D);
    printf("Case #%d: %.10f\n", t+1, bin_search(0.0, length)); 
  }

  
  return 0;
}
