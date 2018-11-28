#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int n;
int pos[1100][4];
double limits[4][2];
int teste, t;
int main() {
    int i;
    int z;
    scanf("%d\n", &teste);
    for (t=0; t<teste; t++){
        scanf("%d\n", &n);
        for (i=0; i<n; i++) {
            scanf("%d %d %d %d\n", &pos[i][0], &pos[i][1], &pos[i][2], &pos[i][3]);
        }
        double a = 0;
        double b = 10000000;
        double c;
        for (z=0; z<50; z++){
            c = (a+b)/2;
            for (i=0; i<4; i++) {
                limits[i][0]=-10000000;
                limits[i][1]=10000000;
            }
            for (i=0; i<n; i++) {
                limits[0][0]=max(limits[0][0], pos[i][0]+pos[i][1]+pos[i][2]-c*pos[i][3]);
                limits[0][1]=min(limits[0][1], pos[i][0]+pos[i][1]+pos[i][2]+c*pos[i][3]);
                limits[1][0]=max(limits[1][0], pos[i][0]+pos[i][1]-pos[i][2]-c*pos[i][3]);
                limits[1][1]=min(limits[1][1], pos[i][0]+pos[i][1]-pos[i][2]+c*pos[i][3]);
                limits[2][0]=max(limits[2][0], pos[i][0]-pos[i][1]+pos[i][2]-c*pos[i][3]);
                limits[2][1]=min(limits[2][1], pos[i][0]-pos[i][1]+pos[i][2]+c*pos[i][3]);
                limits[3][0]=max(limits[3][0], pos[i][0]-pos[i][1]-pos[i][2]-c*pos[i][3]);
                limits[3][1]=min(limits[3][1], pos[i][0]-pos[i][1]-pos[i][2]+c*pos[i][3]);
            }
            for (i=0; i<4; i++) {
                if (limits[i][0]-1e-9>limits[i][1]) break;
            }
            if (i==4) {
                b=c;
            }
            else a=c;         
        }
        printf("Case #%d: %lf\n", t+1, c);
    }
    return 0;    
}
