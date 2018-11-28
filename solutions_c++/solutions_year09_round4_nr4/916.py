#include<cstdio>
#include<cmath>

double x[5],y[5],r[5];
int n,tc;

double sqr(double a){return a*a;}
double finddist(int i, int j){
  return (sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]))+r[i]+r[j])/2;
}
double max(double a, double b){if (a>b)return a; return b;}
double min(double a, double b){if (a<b)return a; return b;}
int main(){
 scanf("%d",&tc);
 for (int ti = 1; ti <= tc; ti++){
     scanf("%d",&n);
     for (int i = 1; i <= n; i++){
         scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);    
     }
     double res;    
     if (n == 3){
     res = max(finddist(1,2),r[3]);
     res = min(res,max(finddist(1,3),r[2]));
     res = min(res,max(finddist(2,3),r[1]));
     }else if (n == 2) res = min(finddist(1,2),max(r[1],r[2]));
     else res = r[1];
     printf("Case #%d: %.6lf\n",ti,res);

 }   
}
