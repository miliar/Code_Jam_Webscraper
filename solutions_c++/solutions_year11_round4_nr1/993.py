#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

struct way{
    int s,e,w;
    
    way(){}
    
    way(int _s, int _e, int _w){
        s = _s; e = _e; w = _w;
    }
    
    bool operator < (way X)const{
        return w < X.w;
    }
}A[1000],B[2001];

double solve(int N, int S, int R, double t){
    double ret = 0;
    
    for(int i = 0;i < N;++i){
        //printf("%d %d %d\n",B[i].s,B[i].e,B[i].w);
        double D = B[i].e - B[i].s;
        
        if(t > 0){
            double dx = (R + B[i].w) * t;
            double dt = D * t / dx;
            
            dt = min(dt,t);
            t -= dt;
            
            double dt2 = (D - (R + B[i].w) * dt) / (S + B[i].w);
            
            ret += dt + dt2;
            //cout << dt + dt2 << endl;
        }else{
            ret += D / (S + B[i].w);
            //cout << D / (S + B[i].w) << endl;
        }
    }
    
    return ret;
}

int main(){
    int TC,X,S,R,trun,N,sz;
    
    scanf("%d",&TC);
    
    for(int tc = 1;tc <= TC;++tc){
        scanf("%d %d %d %d %d",&X,&S,&R,&trun,&N);
        
        for(int i = 0;i < N;++i)
            scanf("%d %d %d",&A[i].s,&A[i].e,&A[i].w);
        
        for(int i = 0;i < N;++i)
            for(int j = i + 1;j < N;++j)
                if(A[i].s > A[j].s)
                    swap(A[i],A[j]);
        
        sz = 0;
        
        for(int i = 0,j = 0;i != X;){
            if(j < N){
                if(A[j].s == i){
                    B[sz++] = way(i,A[j].e,A[j].w);
                    i = A[j].e;
                    ++j;
                }else{
                    B[sz++] = way(i,A[j].s,0);
                    i = A[j].s;
                }
            }else{
                B[sz++] = way(i,X,0);
                i = X;
            }
        }
        
        sort(B,B + sz);
        printf("Case #%d: %.9f\n",tc,solve(sz,S,R,(double)trun));
    }
    
    return 0;
}
