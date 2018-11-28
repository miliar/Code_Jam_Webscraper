#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
char MAP[105][105];
double wp[105];
double op[105];
double oop[105];
int main (){
    int T,ca = 0,n,i,j,k;
    int cnt = 0,game;
    int a;
    double tmp;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%s",MAP[i]);
        }
        for(i=0;i<n;i++){
            cnt = 0;
            game = 0;
            for(j=0;j<n;j++){
                if(MAP[i][j] == '1' || MAP[i][j] == '0'){
                    game++;
                }
                if(MAP[i][j] == '1'){
                    cnt++;
                }
            }
            wp[i] = (double)cnt / (double)game;
        }
        for(k=0;k<n;k++){
            tmp = 0;
            a = 0;
            for(i=0;i<n;i++){
                if(k == i)continue;
                cnt = 0;
                game = 0;
                for(j=0;j<n;j++){
                    if(k == j)continue;
                    if(MAP[i][j] == '1' || MAP[i][j] == '0'){
                        game++;
                    }
                    if(MAP[i][j] == '1'){
                        cnt++;
                    }
                }
                //printf("%d wp %lf\n",i,(double)cnt/(double)game);
                if(MAP[k][i] != '.'){
                    tmp += (double)cnt / (double)game;
                    a++;
                }
            }        
            op[k] = tmp / (double)(a);
           // printf("op[k] = %lf\n",op[k]);
        }
        for(i=0;i<n;i++){
            tmp = 0;
            cnt = 0;
            for(j=0;j<n;j++){
                if(i == j)continue;
                if(MAP[i][j] != '.'){
                    cnt++;
                    tmp +=  op[j];
                }
            }
            oop[i] = tmp / (double)(cnt);
        }
        ca++;
        printf("Case #%d:\n",ca);
        for(i=0;i<n;i++)printf("%lf\n",wp[i]*0.25+op[i]*0.5+oop[i]*0.25);
        
    }
    return 0;
}
/*
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
*/
