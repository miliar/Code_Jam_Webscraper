#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>

using namespace std;

int n, na, nb;
int turn;
int adisp[2000];
int bdisp[2000];
int adep[2000];
int bdep[2000];

int main() {
    int h, m;
    int i;
    int t;
    int aresp, bresp;
    int disp;
    scanf("%d", &n);
    for (t=0; t<n; t++) {
        for (i=0; i<2000; i++) {
            adisp[i] = 0;
            bdisp[i] = 0;
            adep[i] = 0;
            bdep[i] = 0;
        }
        aresp = 0;
        bresp = 0;
        scanf("%d\n%d %d\n", &turn, &na, &nb);
        for (i=0; i<na; i++)
        {
            scanf("%d:%d ", &h, &m);
            adep[h*60+m]++;
            scanf("%d:%d\n", &h, &m);
            bdisp[h*60+m+turn]++;
        }
        for (i=0; i<nb; i++)
        {
            scanf("%d:%d ", &h, &m);
            bdep[h*60+m]++;
            scanf("%d:%d\n", &h, &m);
            adisp[h*60+m+turn]++;
        }
        disp = 0;
        for (i=0; i<1440; i++) {
            disp += adisp[i];
            if (disp >= adep[i]){
                disp -= adep[i];
            }
            else {
                aresp += adep[i] -disp;
                disp = 0;
            }
        }
        disp = 0;
        for (i=0; i<1440; i++) {
            disp += bdisp[i];
            if (disp >= bdep[i]){
                disp -= bdep[i];
            }
            else {
                bresp += bdep[i] -disp;
                disp = 0;
            }
        }
        printf("Case #%d: %d %d\n", t+1, aresp, bresp);
    }
    return 0;
}
