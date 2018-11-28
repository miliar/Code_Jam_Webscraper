#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int wp[100];
double owp[100], oowp[100];
int gameswp[100];
char mat[100][100];

int main(){
    int T,N;
    int c = 1;
    char tmp;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &N);
        
        for(int i = 0; i < N; ++i){
            int acum = 0;
            int num = 0;
            for(int j = 0; j < N; ++j){
                cin >> tmp;
                mat[i][j] = tmp;
                if(tmp == '1')
                    acum += 1;
                if(tmp == '1' || tmp == '0')
                    num += 1;
            }
            gameswp[i] = num;
            wp[i] = acum;
        }
        memset(oowp,0,sizeof(oowp));
        for(int i = 0; i < N; ++i){
            int acum = 0;
            int num = 0;
            double tmp = 0;
            double cnt = 0.0;
            for(int j = 0; j < N; ++j){
                if(mat[i][j] != '.'){
                    cnt += 1.0;
                    acum = wp[j];
                    num = gameswp[j];
                    if(mat[j][i] == '1'){
                        acum -= 1;
                        num -= 1;
                    }
                    if(mat[j][i] == '0'){
                        num -= 1;
                    }
                    tmp += (double)acum/(double)num;
                }
            }
            owp[i] = tmp/(double)(cnt);
        }
        
        for(int i = 0; i < N; ++i){
            double acum = 0.0;
            double cnt = 0.0;
            for(int j = 0; j < N; ++j){
                if(mat[i][j] != '.'){
                    acum += owp[j];
                    cnt += 1.0;
                }
            }
            oowp[i] = acum/cnt;
        }
        
        printf("Case #%d:\n",c++);
        for(int i = 0; i < N; ++i){
            double a = (double)wp[i]/(double)gameswp[i];
            //printf("%lf --- %lf --- %lf\n",a,owp[i],oowp[i]);
            printf("%.12lf\n",0.25*a + 0.5*owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
