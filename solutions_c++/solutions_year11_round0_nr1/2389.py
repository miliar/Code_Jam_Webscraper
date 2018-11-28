#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    int pre,step,totalstep,pos,posa,posb;
    int n,move;
    char rb;
    scanf("%d", &t);
    for (int i=1; i<=t; i++){
        scanf("%d", &n);
        pre = 0;
        step = 0;
        totalstep = 0;
        posa = 1;
        posb = 1;
        for(int j=0; j<n ; j++){
            scanf(" %c", &rb);
            scanf("%d", &pos);
            if (rb == 'O') {
                move = posa - pos;
                if (move < 0) move = -move;
                if (pre == 2) {
                    move = move - step;
                    if (move < 0) move = 0;
                    move = move + 1;
                    totalstep = totalstep + move;
                    pre = 1;
                    step = move;
                } else {
                    move = move + 1;
                    totalstep = totalstep + move;
                    pre = 1;
                    step = step + move;
                }
                posa = pos;
            } else {
                move = posb - pos;
                if (move < 0) move = -move;
                if (pre == 1) {
                    move = move - step;
                    if (move < 0) move = 0;
                    move = move + 1;
                    totalstep = totalstep + move;
                    pre = 2;
                    step = move;        
                } else {
                    move = move + 1;
                    totalstep = totalstep + move;
                    pre = 2;
                    step = step + move;
                }
                posb = pos;
            }
        }
        printf("Case #%d: %d\n",i, totalstep);
    }
 //   system("PAUSE");
    return EXIT_SUCCESS;
}
