#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#define MAXN 105

using namespace std;
int N;
char map[MAXN][MAXN];
struct team{
    double wp,owp,oowp;
    void init(){
        wp=owp=oowp=0;
    }
}ts[MAXN];

double RPI(int x){
    return 0.25*ts[x].wp+0.5*ts[x].owp+0.25*ts[x].oowp;
}
double WP(int x){
    double s=0,w=0;
    for(int i=0;i<N;i++){
        if(map[x][i]=='1'){s++,w++;}
        else if(map[x][i]=='0'){s++;}
    }
    return w/s;
}
double WP2(int x,int y){
    double s=0,w=0;
    for(int i=0;i<N;i++){
        if(i==y)continue;
        else if(map[x][i]=='1'){s++,w++;}
        else if(map[x][i]=='0'){s++;}
    }
    return w/s;
}
double OWP(int x){
    double s=0,r=0;
    for(int i=0;i<N;i++){
        if(map[x][i]!='.'){
            r+=WP2(i,x);
            s++;
        }
    }
    return r/s;
}
double OOWP(int x){
    double s=0,r=0;
    for(int i=0;i<N;i++){
        if(map[x][i]!='.'){
            r+=ts[i].owp;
            s++;
        }
    }
    return r/s;
}
int main(){
    int T;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2out.txt","w",stdout);
    scanf("%d",&T);
    for(int _case=1;_case<=T;_case++){
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf(" %s",map[i]);
        }
        for(int i=0;i<N;i++){
            ts[i].init();
            ts[i].wp=WP(i);
        }
        for(int i=0;i<N;i++){
            ts[i].owp=OWP(i);
        }
        for(int i=0;i<N;i++){
            ts[i].oowp=OOWP(i);
        }
        printf("Case #%d:\n",_case);

        for(int i=0;i<N;i++){
            printf("%.12lf\n",RPI(i));
        }
    }
    return 0;
}
