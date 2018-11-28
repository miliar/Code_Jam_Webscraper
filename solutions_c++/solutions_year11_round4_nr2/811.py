#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define EPS 0.000000001

using namespace std;
char B[501];
int W[501][501],R,C;

double abs(double a){
       return a<0?-a:a;
       }

int tryf(int r, int c, int s){
    if(r+s>R||c+s>C) return 0;
    double my=0,mx=0,m=0;
    for(int i=r;i<r+s;i++)
            for(int j=c;j<c+s;j++) {
                    if((i==r&&j==c)||(i==r&&j==c+s-1)||(i==r+s-1&&j==c)||(i==r+s-1&&j==c+s-1)) continue;
                    //printf("%d %d\n",i,j);
                    m += (double)W[i][j];
                    my += (double)W[i][j]*((double)i+0.5);
                    mx += (double)W[i][j]*((double)j+0.5);
            }
    double x = (double)mx/(double)m;
    double y = (double)my/(double)m;
    //printf("%d %d %lf %lf - %lf %lf\n",r,c,x,y,((double)r+(double)s/2.0),((double)c+(double)s/2.0));
    if(abs(y-((double)r+(double)s/2.0))<=EPS&&abs(x-((double)c+(double)s/2.0))<=EPS) return 1;
    return 0;
}

int possible(int size){
    //printf("%d\n",size);
    for(int i=0;i<R;i++){
            for(int j=0;j<C;j++) {
                    if(tryf(i,j,size))
                                     return 1;
            }
    }
    return 0;
}

main() {
       int T,tc,tot,D;
       FILE *in = fopen("B3.in","r");
       FILE *out = fopen("B3.out","w");
       fscanf(in,"%d",&T);
       for(int tc=1;tc<=T;tc++) {
               fscanf(in,"%d %d %d",&R,&C,&D);
               for(int i=0;i<R;i++) {
                       fscanf(in,"%s",B);
                       for(int j=0;j<C;j++)
                               W[i][j] = B[j]-'0'+D;
               }
               tot = R;
               tot <?= C;
               for(;tot>=3&&!possible(tot);tot--);
               if(tot>=3){
               fprintf(out,"Case #%d: %d\n",tc,tot);
               fprintf(stdout,"Case #%d: %d\n",tc,tot);
               }else{
                     fprintf(out,"Case #%d: IMPOSSIBLE\n",tc);
               fprintf(stdout,"Case #%d: IMPOSSIBLE\n",tc);
                     }
       }
       fclose(out);
       system("PAUSE");
}
