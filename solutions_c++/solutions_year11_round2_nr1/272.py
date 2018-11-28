#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
using namespace std;
#define PB push_back

const int INF = 1000000000;

char s[110][110];

double wp[110], owp[110], oowp[110], WP[110], OWP[110];



int main(){
    int i, j, k, l, cas, re, n;
    freopen("A-large.in", "r", stdin); freopen("w.txt", "w", stdout);
    scanf("%d", &cas);
    for(re = 1; re <= cas; re++){
        printf("Case #%d:\n", re);
        scanf("%d", &n);
        for(i = 0; i < n; i++)
            scanf("%s", s[i]);
        for(i = 0; i < n; i++){
            int w = 0, t = 0;
            for(j = 0; j < n; j++){
                if(s[i][j] == '1')
                    w++;
                if(s[i][j] != '.')
                    t++;
            }
            wp[i] = w * 1.0 / t;
        }

        for(i = 0; i < n; i++){
            double WP = 0;
            int p = 0;
            for(j = 0; j < n; j++)if(j != i){
                int w = 0, t = 0;
                for(k = 0; k < n; k++)
                    if(k != i){
                        if(s[j][k] == '1')
                            w++;
                        if(s[j][k] != '.')
                            t++;
                    }

                if(s[i][j] != '.'){
                    WP += w * 1.0 / t;
                    p++;
                }
            }
            owp[i] = WP / p;
        }

        for(i = 0;  i < n; i++){
            double w = 0;
            int p = 0;
            for(j = 0; j < n; j++)
                if(i!=j && s[i][j] != '.'){
                    w += owp[j];
                    p++;
                }
            oowp[i] = w / p;
        }
          for(i = 0; i < n; i++)
            printf("%.15lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
}
