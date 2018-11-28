#include <cstdio>
#include <iostream>
#define S 101
using namespace std;

int main(int argc, const char *argv[]){
    int m,n=0, t[S][S]; 
    int w[S], g[S];
    float wp[S], owp[S], oowp[S];
    char c;
    scanf("%d " , &n);
    for(int i=0; i<n; ++i){
        scanf("%d ", &m);
        for(int j=0; j<m+1; ++j){
            for(int k=0; k<m+1; ++k){
                t[j][k]=0;
            }
        }
        for(int j = 0; j<m; ++j){
            g[j]=0;
            wp[j] = 0;
            w[j] = 0;
            owp[j]=0;
            oowp[j]=0;
            for(int k=0; k<m; ++k){
                cin >> c;
                if(c=='1') {
                    t[j][k] = 2;
                    w[j]++;
                }
                if(c=='0')
                    t[j][k] = 1;
                if(c!='.')
                    g[j]++;
            }
            if(g[j]>0)
            wp[j] = float(w[j])/float(g[j]);
        }
        for(int j=0; j<m; ++j){
            float sum=0;
            int gm = 0;
            for(int k=0; k<m; ++k){
                if(t[j][k]>0){
                    sum= sum + float(w[k]-(t[k][j]==2?1:0))/float(g[k]-1);
                    gm++;
//                    printf("::%f\n", float(w[k]-(t[k][j]==2?1:0))/float(g[k]-1));

                } 
            }
            owp[j]=sum/float(gm);
//            printf("%f\n", owp[j]);
        }

        for(int j=0; j<m; ++j){
            float sum = 0;
            int l = 0;
            for(int k=0; k<m; ++k){
                if(t[j][k]>0){
                    sum+=owp[k];
                    l++;}
            }
            oowp[j] = sum/float(l);
//            printf(">>%f\n", oowp[j]);
        }
        printf("Case #%d:\n", i+1);
        for(int j=0; j<m; ++j){
            printf("%f\n", 0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j]);
        }
 //       printf("%d\n", n);
    }
    return 0;
}
