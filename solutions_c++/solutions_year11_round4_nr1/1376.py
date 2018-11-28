#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>


using namespace std;



#define clr(x) memset((x), 0, sizeof(x))
#define Foru(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define foru(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define MAX 3005

struct way{
  int speed;
  long double begin, end;
};

way ways[MAX];

int compare1(const void * ia, const void * ib){      // to sort list of ints (in ranktoindex) according to d in stalks[index].d;
  if ((*(way*)ia).speed > (*(way*)ib).speed) return 1; else return -1;
}

int compare2(const void * ia, const void * ib){      // to sort list of ints (in ranktoindex) according to d in stalks[index].d;
  if ((*(way*)ia).begin > (*(way*)ib).begin) return 1; else return -1;
}


int main(){
  int T;
  scanf("%d\n",&T);
  foru(i, T){
    int X,S,R,tt,N;
    scanf("%d %d %d %d %d\n",&X,&S,&R,&tt,&N);
    long double t = tt; 
    int b,e;
    foru(j, N){
      scanf("%d %d %d\n",&b,&e,&ways[j].speed);
      ways[j].begin = b;  
      ways[j].end = e;
    }  
    foru(j, N) ways[j].speed += S;
    qsort(ways,N,sizeof(way),compare2);
 //   foru(j, N){ printf("%Lf %Lf %d\n",ways[j].begin,ways[j].end,ways[j].speed);}
    long double pos = 0;
    int j = 0;
    int add = 0;
    foru(j,N){
      if (pos < ways[j].begin){
        ways[N+add].begin = pos;
        ways[N+add].end = ways[j].begin;
        ways[N+add].speed = S;
        add++;
        
      }
      pos = ways[j].end;
    }
    if (pos < X){
      ways[N+add].begin = pos;
        ways[N+add].end = X;
        ways[N+add].speed = S;
        add++;
    }
    N += add;
  //      foru(j, N){ printf("%Lf %Lf %d\n",ways[j].begin,ways[j].end,ways[j].speed);}
    qsort(ways,N,sizeof(way),compare1);
   // foru(j, N){ printf("%Lf %Lf %d\n",ways[j].begin,ways[j].end,ways[j].speed);}
    j = 0;
    add = 0;
    if (R > S){
      while ((t > 0.0001) && (j < N)){
        long double tmpt = ((long double)ways[j].end-ways[j].begin)/(ways[j].speed+R-S);
        if (t > tmpt-0.0001){
   //       printf("hallo");
          t -= tmpt;
          ways[j].speed += (R-S);
        }else{
    //      printf("%Lf\n",t);
          ways[N+add].end = ways[j].end;
          ways[N+add].speed = ways[j].speed;
          ways[N+add].begin = ways[j].begin+(ways[j].speed + R - S) * t;
          ways[j].end = ways[N+add].begin;
          ways[j].speed += (R-S);
          add++;
          t = 0;
        }
        j++;         
      }
      N += add;
    }
    double time = 0;
    foru(j, N){ time += (double)(ways[j].end - ways[j].begin) / ways[j].speed; 
  //  printf("%Lf %Lf %d %lf\n",ways[j].begin,ways[j].end,ways[j].speed,time);
    }
    printf("Case #%d: %lf\n",i+1,time);
  }
  return 0;
} 
