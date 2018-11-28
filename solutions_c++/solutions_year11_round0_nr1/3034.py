#include <stdio.h>
#define abs(a) ((a) > 0 ? (a) : -(a))
char str[10];
int main () {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cs,num,step,i;
    int blue,orange;
    int curBlue, curOrange;
    char pre;
    scanf("%d",&T);
    for (cs = 1; cs <= T; cs++) {
        scanf("%d",&num);
        blue = orange = 0;
        curBlue = curOrange = 1;
        pre = 0;
        for (i = 0; i < num; i++) {
            scanf("%s%d",str,&step);
            //printf("%c %d\n",str[0],step);
            if (str[0] == 'B') {
                blue += abs(step - curBlue) + 1;
                if (pre == 'O' && blue <= orange) {
                    blue = orange + 1;
                }
                curBlue = step;
                pre = 'B';
            } else {
                orange += abs(step - curOrange) + 1;
                if (pre == 'B' && orange <= blue) {
                    orange = blue + 1;
                }
                curOrange = step;
                pre = 'O';
            }
        }
        //printf("%d %d\n",orange,blue);
        printf("Case #%d: %d\n", cs, (blue > orange ? blue : orange));
    }
    return 0;
}
