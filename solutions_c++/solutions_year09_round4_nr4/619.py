#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct plant{
    int X, Y, R;
}p[3];

int T, N;

double dis(int x, int y){
    return sqrt(  (p[x].X-p[y].X)*(p[x].X-p[y].X)+(p[x].Y-p[y].Y)*(p[x].Y-p[y].Y) );
}

int main(){
    scanf("%d", &T);
    for(int nCase=1;nCase<=T;nCase++){
        scanf("%d", &N);
        for(int i=0;i<N;i++)
            scanf("%d%d%d", &p[i].X, &p[i].Y, &p[i].R);
        printf("Case #%d: ", nCase);
        if(N==1) cout<<p[0].R<<endl;
        else if(N==2) cout<<max(p[0].R, p[1].R)<<endl;
        else{
            double Min=9999;
            for(int i=0;i<3;i++){
                 Min = min(Min, max((double)p[i].R, (dis((i+1)%3, (i+2)%3)+p[(i+1)%3].R+p[(i+2)%3].R)/2  ) );
            }
            cout<<Min<<endl;
        }
    }
    return 0;
}
