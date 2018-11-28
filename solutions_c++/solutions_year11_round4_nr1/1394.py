#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
using namespace std;

struct W{
    int l;
    int w;
};

int compare (const void * a, const void * b)
{
  W A = *(W*)a;
  W B = *(W*)b;
  return A.w-B.w;
}

int gcd(int a, int b){
    if(a==0) return b;
    if(b==0) return a;
    if(a>b) return gcd(b, a%b);
    return gcd(a, b%a);
}


int main(){
    freopen("in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest;
    cin >> ntest;
		
		for(int test=1;test<=ntest;++test) {
			int S, R, X, N, b, e, w, i, j, total=0;
			double t;
			cin >> X >> S >> R >> t >> N;
            W wa[N];
            for(i=0 ; i< N ;i++){
                cin >> b >> e >> w;
                wa[i].l = e-b;
                wa[i].w = w;
                total += e-b;
            }
            qsort(wa, N, sizeof(W), compare);
			double r=0.0;
			int sum=0;
            if(t>=X){
                for(i=0 ; i<N ; i++){
                    r+=(double)wa[i].l/(wa[i].w+R);
                    sum += wa[i].l;
                }
                r+=(double)(X-sum)/(R);
            }
            else if(total==X){
                for(i=0 ; i<N ; i++){                    
                    if((double)wa[i].l<=t*(wa[i].w+R)){
                        r+=(double)wa[i].l/(wa[i].w+R);
                        t -= (double)wa[i].l/(wa[i].w+R);
                    }
                    else if(t>0.0){
                        r+=t;
                        r+=((double)wa[i].l-t*(wa[i].w+R))/(wa[i].w+S);
                        t =0; 
                    }
                    else{
                        r+=(double)wa[i].l/(wa[i].w+S);
                    }
                }
            }
            else{
                total = X-total;
                if((double)total>=t*R){                    
                    r+=t;
                    r+=((double)total-t*R)/S;
                    t=0;
                }
                else {
                    r+=(double)(total)/(R);                    
                    t -= (double)(total)/(R);
                }
                
                for(i=0 ; i<N ; i++){                    
                    if((double)wa[i].l<=t*(wa[i].w+R)){
                        r+=(double)wa[i].l/(wa[i].w+R);
                        t -= (double)wa[i].l/(wa[i].w+R);
                    }
                    else if(t>0.0){
                        r+=t;
                        r+=((double)wa[i].l-t*(wa[i].w+R))/(wa[i].w+S);
                        t =0; 
                    }
                    else{
                        r+=(double)wa[i].l/(wa[i].w+S);
                    }
                }
            }
            cout << "Case #"<<test<<": ";
            printf("%.10lf\n", r);
		}
    return 0;
}
