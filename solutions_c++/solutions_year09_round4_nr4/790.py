#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

double x[4],y[4],r[4];
int n;

double doTest(){
    double Min = 1e60;
    if (n == 1)
        return r[0];
    if (n == 2){
        return max(r[0],r[1]);
        //return (sqrt((x[0] - x[1]) * (x[0] - x[1]) + (y[0] - y[1]) * (y[0] - y[1])) + r[0] + r[1]) / 2.;
    }
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (i == j)
                continue;
            for (int k = 0; k < 3; k++){
                if (i == k || j == k) continue;
                double c1 = (sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) + r[i] + r[j]) / 2;
                double c2 = r[k];
                Min = min(Min, max(c1,c2));
            }
        }
    }
    return Min;
    //printf("%.10lf\n",Min);    
}

int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    int T;scanf("%d",&T);
    for (int i = 0; i < T; i++){
        scanf("%d",&n);
        for (int j = 0; j < n; j++)
            scanf("%lf%lf%lf",&x[j],&y[j],&r[j]);
        printf("Case #%d: %.10lf\n",i+1,doTest());        
    }
                 
    return 0;
}