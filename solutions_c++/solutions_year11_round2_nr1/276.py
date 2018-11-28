#include <stdio.h>

char s[101][101];
double wp[3][101];
int p[101],w[101];
int N;

void solve(int cas){
    int i,j,t;
    int a;
    double c;
    scanf("%d",&N);
    for (i=0;i<N;i++) scanf("%s",s[i]);
    for (i=0;i<N;i++){
        p[i] = w[i] = 0;
        for (j=0;j<N;j++){
            if (s[i][j]=='.') continue;
            p[i]++;
            if (s[i][j]=='1') w[i]++;
        }
        wp[0][i]=w[i]*1.0/(p[i]>0?p[i]:1);
    }
    for (i=0;i<N;i++){
        a = 0; c = 0.0;
        for (j=0;j<N;j++){
            if (s[i][j]!='.'){
                a++;
                if (s[i][j]=='0'){
                    if (p[j]>1) c+=(w[j]-1)*1.0/(p[j]-1);
                }else{
                    if (p[j]>1) c+=(w[j])*1.0/(p[j]-1);
                }
            }
        }
        wp[1][i]=c/(a>0?a:1);
    }
    for (i=0;i<N;i++){
        a = 0; c=0.0;
        for (j=0;j<N;j++){
            if (s[i][j]!='.'){
                a++;
                c+=wp[1][j];
            }
        }
        wp[2][i] = c/(a>0?a:1);
    }
    printf("Case #%d:\n",cas);
    //for (i=0;i<N;i++) printf("%.10lf %.10lf %.10lf\n",wp[0][i],wp[1][i],wp[2][i]);
    for (i=0;i<N;i++) printf("%.15lf\n",wp[0][i]*0.25+wp[1][i]*0.5+wp[2][i]*0.25);
}

int main(){
    int t,cas;
    scanf("%d",&t);
    for (cas=1;cas<=t;cas++) solve(cas);
    return 0;
}

