#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <inttypes.h>

using namespace std;

#define MAX 1024

struct t_est{
    double d,v;
} est[MAX];

int comp(const void *a, const void *b)
{
    struct t_est *ia = (struct t_est *)a;
    struct t_est *ib = (struct t_est *)b;

    if(ia->v - ib->v > 0) return 1;
    else if( ia->v - ib->v == 0) return 0;
    else return -1;
}

int main(){
    FILE *fin = fopen("A-large.in","r");
    FILE *fout = fopen("A2.out","w");
    int nt;
    fscanf(fin,"%d",&nt);
    double X,S,R,t;
    int N;
    for(int teste = 1 ; teste <= nt ; teste++){
        fscanf(fin,"%lf %lf %lf %lf %d",&X,&S,&R,&t,&N);
        double dS =0;
        double B,E;

        for(int i = 0; i < N ; i++){
            fscanf(fin,"%lf %lf %lf",&B,&E,&est[i].v);
            est[i].v += S;
            est[i].d = E - B;
            dS += E - B;
        }
        est[N].v = S;
        est[N].d = X - dS;
        N = N + 1;

        qsort(est,N,sizeof(struct t_est),comp);

        double ans = 0.0;
        double tu = t;
        for(int i = 0 ; i < N ; i++){
            if(est[i].d - (est[i].v + R - S)*tu >= 0){
                ans += tu + (((est[i].d - (est[i].v + R - S)*tu))/est[i].v);
                tu = 0;
            }
            else{
                double te = est[i].d/(est[i].v + R - S);
                ans += te;
                tu -= te;
            }
        }
        fprintf(fout,"Case #%d: %lf\n",teste,ans);
    }
    return 0;

}
