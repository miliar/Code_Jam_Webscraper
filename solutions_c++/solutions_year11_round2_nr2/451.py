#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXC 300
long double P[MAXC];//points
int V[MAXC];//vendros
int T[MAXC];
int d, c;

bool fun(long double s){
    //printf("fun: %Lf\n", s);
    bool error=false;
    for(int i=0; i<c; i++){
        T[i]=V[i];
    }
    long double last = P[0]-s+d;//ostatnia dostepna pozyja
    T[0]--;
    int i=0;
    while(i<c){
        if(T[i]<=0){
            i++;
        }else{
            T[i]--;    
            if(last<P[i]){
                last = max(last, P[i]-s);    
            }else{
                if(last>P[i]+s){
                    error=true;
                    break;
                }else{
                    last = last;
                }
            }
            last += d;
        }
    }
    return !error;
}

int main(){
    int t;
    scanf("%d", &t);
    for(int q=1; q<=t; q++){
        long double ans = 0;
        scanf("%d%d", &c, &d);
        for(int i=0; i<c; i++){
            scanf("%Lf%d", &P[i], &V[i]);
        }
        long double l = 0.0;
        long double r = 1152921504606846976.0L;
        while((r-l)>0.0000001L){
            long double s = (l+r)/2; 
            if(fun(s)){
                r=s; 
            }else{
                l=s; 
            }
        }
        printf("Case #%d: %.10Lf\n", q, l); 
    }
    return 0;
}
