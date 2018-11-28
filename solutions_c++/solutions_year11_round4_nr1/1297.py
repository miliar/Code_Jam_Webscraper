#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

#define EPS 0.000001

typedef struct walkway {
       int b;
       int e;
       int w; 
        
} Walk;        

bool cmp(Walk a, Walk b) {
     if(a.w == b.w)
            return a.b < b.b;
     return a.w < b.w;     
}     

double calcular(int s,int r,double taux, int t, Walk walks[], int n) {
       double total = 0;
             for(int i = 0;i < n;i++) {
                     if(taux - EPS > 0) {
                                double t2 = ((double)(walks[i].e - walks[i].b))/((double)(walks[i].w + r));
                                if(t2 < taux) {
                                      taux -= t2;
                                      total += t2;          
                                }
                                else {
                                     total += taux;
                                     double x = ((double)(walks[i].w + r))*taux;
                                     taux = 0;
                                     total += ((double)(walks[i].e - walks[i].b)-x)/((double)(walks[i].w + s));     
                                }
                                //printf("hello!\n");              
                     }
                     else {
                          total += ((double)(walks[i].e - walks[i].b))/((double)(walks[i].w + s));  
                     } 
                     //printf("%llf\n",total); 
             }                  
       return total;                  
}       

int main() {
    int t;
    scanf("%d",&t);    
    for(int i = 1;i <= t;i++) {
            int x,s,r,t,n;
            Walk walks[1010];
            scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
            int aux = x;
            for(int j = 0;j < n;j++) {
                    scanf("%d %d %d",&(walks[j].b),&(walks[j].e),&(walks[j].w));
                    aux = aux - (walks[j].e - walks[j].b);
                   // printf("aux = %d\n",aux);        
            }
            sort(walks,walks+n,cmp);
            double total = 0;
            double taux = ((double)aux)/((double)r);
            //printf("%d %d %llf\n",aux,r,taux); 
            if((double)t < taux + EPS) {
                 total += t;
                 aux -= r*t;
                 //printf("aux = %d\n",aux);
                 total += ((double)aux)/((double)s);
                 total += calcular(s,r,0,t,walks,n);
            }
            else {
                 total += taux;
                 taux = t - taux;
                 //printf("%llf %llf\n",total,taux);
                 total += calcular(s,r,taux,t,walks,n);     
            }     
            printf("Case #%d: %llf\n",i,total);
    }
    return 0;
}
