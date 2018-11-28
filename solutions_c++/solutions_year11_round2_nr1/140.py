#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

char a[200][200];
double wp[200], wpw[200][200], owp[200], rpi[200];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for(int tt = 0; tt < t; tt++){
        int n;
        scanf("%d\n", &n);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                scanf("%c", &a[i][j]);
            }
            scanf("\n");
        }
        for(int i = 0; i < n; i++){
            int all = 0;
            int good = 0;
            for(int j = 0; j < n; j++){
                if(a[i][j] != '.'){
                    all++;
                    if(a[i][j] == '1'){
                        good++;
                    }
                }
            }
            wp[i] = (double)good / all;
            for(int j = 0; j < n; j++){
                if(i != j){
                    all = 0;
                    good = 0;
                    for(int z = 0; z < n; z++){
                        if(z != j){
                            if(a[i][z] != '.'){
                                all++;
                                if(a[i][z] == '1'){
                                    good++;
                                }
                            }
                        }
                    }
                    wpw[i][j] = (double)good / all;
                }
            }
        }
        for(int i = 0; i < n; i++){
            owp[i] = 0;
            int sz = 0;
            for(int j = 0; j < n; j++){
                if(a[i][j] != '.'){
                    owp[i] += wpw[j][i];
                    sz++;
                }
            }
            owp[i] /= sz;
        }
        for(int i = 0; i < n; i++){
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i];
            double sum = 0;
            int sz = 0;
            for(int j = 0; j < n; j++){
                if(a[i][j] != '.'){
                    sum += owp[j];
                    sz++;
                }
            }
            rpi[i] += 0.25 * sum / sz;
        }
        printf("Case #%d:\n", tt + 1);
        for(int i = 0; i < n; i++){
            printf("%.18lf\n", rpi[i]);
        }
    }
    return 0;
}
