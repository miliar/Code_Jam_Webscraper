#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD; 
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

void scase(int CID){
  int W;
  int L,U,G;
  scanf("%d%d%d%d",&W,&L,&U,&G);
  PII l[L+1],u[U+1];
  REP(i,L)scanf("%d%d",&l[i].st,&l[i].nd);
  REP(i,U)scanf("%d%d",&u[i].st,&u[i].nd); 
  l[L] = l[L-1];
  PDD l2[L+U],u2[L+U];
  int i = 0, j = 0, k = 0;
  while(1){    
    if(l[i].st == u[j].st){
      l2[k].st = l[i].st;
      l2[k].nd = l[i].nd;      
      u2[k].st = u[j].st; 
      u2[k].nd = u[j].nd;    
      ++k;                    
      if(l[i].st == W)break; 
      ++i;++j;            
    }else if(l[i].st < u[j].st){
      l2[k].st = l[i].st;
      l2[k].nd = l[i].nd;      
      u2[k].st = l[i].st; 
      u2[k].nd = (l[i].st - u[j-1].st)/(double)(u[j].st - u[j-1].st) * (u[j].nd - u[j-1].nd) + u[j-1].nd;
      i++;
      ++k;      
    }else{
      u2[k].st = u[j].st;
      u2[k].nd = u[j].nd;      
      l2[k].st = u[j].st; 
      l2[k].nd = (u[j].st - l[i-1].st)/(double)(l[i].st - l[i-1].st) * (l[i].nd - l[i-1].nd) + l[i-1].nd;
      j++;
      ++k;    
    }      
  }  
  printf("Case #%d:\n",CID);
  
  double area = 0;
  double area2[k];
  REP(i,k-1){
    area += (area2[i] = ((u2[i+1].st - u2[i].st) * (u2[i+1].nd - l2[i+1].nd + u2[i].nd - l2[i].nd) / 2));
//    printf("%d %lf %lf %lf %lf\n",i,(u2[i+1].st - u2[i].st), (u2[i+1].nd - l2[i+1].nd + u2[i].nd - l2[i].nd), u2[i].st,area2[i]);
  }
  
  FOR(i,1,G){
    double a = area / G * i;
    REP(i,k){
      if(a >= area2[i])a -= area2[i];
      else{
        double L = u2[i].nd - l2[i].nd;
        double R = u2[i+1].nd - l2[i+1].nd;        
        double D = u2[i+1].st - u2[i].st;
        double p = 0, q = D;
        while(p  + 1e-8 < q){
          double s = (p+q)/2;
          double aa = ((2 * L + (R-L) * s / D) * s)/2;
          if(aa < a) p = s;
          else q = s;
        }
        printf("%0.9lf\n",u2[i].st + p);
        break;
      }
    }
  }
}

int main(){
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
