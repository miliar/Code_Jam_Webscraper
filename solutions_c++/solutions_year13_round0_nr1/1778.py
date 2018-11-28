#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int main() {

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");

    int i,j,z,x,o,tt,bx1,bx2,bo1,bo2,ttt,rx[5],ro[5],cx[5],co[5];
    char s[5][5];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        for(i=0; i<4; i++) {
            cx[i]=0; rx[i]=0;
            co[i]=0; ro[i]=0;
        }

        z=1; x=0; o=0;

        for(i=0; i<4; i++) {
            fscanf(ff,"%s", &s[i]);
            for(j=0; j<4; j++) {
                if (s[i][j]=='.') z=0;
                if (s[i][j]=='X') {
                    rx[i]++;
                    cx[j]++;
                }
                if (s[i][j]=='O') {
                    ro[i]++;
                    co[j]++;
                }
                if (s[i][j]=='T') {
                    rx[i]++;
                    cx[j]++;
                    ro[i]++;
                    co[j]++;
                }
            }
        }

        bx1=1; bx2=1; bo1=1; bo2=1;
        for(i=0; i<4; i++) {
            if (s[i][i]!='X' && s[i][i]!='T') bx1=0;
            if (s[i][3-i]!='X' && s[i][3-i]!='T') bx2=0;
            if (s[i][i]!='O' && s[i][i]!='T') bo1=0;
            if (s[i][3-i]!='O' && s[i][3-i]!='T') bo2=0;
        }

        if (bx1 || bx2) x=1;
        if (bo1 || bo2) o=1;

        for(i=0; i<4; i++) {
            if (rx[i]==4 || cx[i]==4) x=1;
            if (ro[i]==4 || co[i]==4) o=1;
        }

        if (x) fprintf(gg,"Case #%d: X won\n", tt);
        else if (o) fprintf(gg,"Case #%d: O won\n", tt);
        else if (z) fprintf(gg,"Case #%d: Draw\n", tt);
        else fprintf(gg,"Case #%d: Game has not completed\n", tt);

    }

    fclose(ff); fclose(gg);

    return 0;
}
