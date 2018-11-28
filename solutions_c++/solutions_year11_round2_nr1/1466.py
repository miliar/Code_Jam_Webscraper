#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
char s[110][110];
double wp[110], owp[110], oowp[110];
int main()
{
    int nCase, n, con = 1;
    int x, y, a, b;
    double sum;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &nCase);
    while(nCase--){
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
            scanf("%s", s[i]);
        for(int i = 0; i < n; i++){
            x = y = 0;
            for(int j = 0; j < n; j++){
                if(s[i][j] != '.'){
                    y++;
                    if(s[i][j] == '1') x++;
                }
            }
            if(y) wp[i] = (double)x / y;
            else wp[i] = 0;
        }
        for(int i = 0; i < n; i++){
            sum = 0; y = 0;
            for(int j = 0; j < n; j++){
                if(s[i][j] != '.'){
                    a = b = 0;
                    for(int k = 0; k < n; k++){
                        if(s[j][k] != '.' && i != k){
                            b++;
                            if(s[j][k] == '1') a++;
                        }
                    }
                    if(b) sum += (double)a / b;
                    y++;
                }
            }
            if(y) owp[i] = sum / y;
            else owp[i] = 0;
        }
        for(int i = 0; i < n; i++){
            sum = 0; y = 0;
            for(int j = 0; j < n; j++){
                if(s[i][j] != '.' && i != j){
                    sum += owp[j];
                    y++;
                }
            }
            if(y) oowp[i] = sum / y;
            else oowp[i] = 0;
        }
        printf("Case #%d:\n", con++);
        for(int i = 0; i < n; i++){
            //printf("%lf %lf %lf\n", wp[i], owp[i], oowp[i]);
            printf("%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
