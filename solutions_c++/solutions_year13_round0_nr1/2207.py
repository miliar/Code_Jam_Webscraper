#include <cstdio>
#include <cstring>

char cs[11][11];
int xwin, owin, incomp;
char flag[256];

void rowcheck()
{
   int i, j;
   for (i=0; i<4; i++) {
       flag['X']=flag['O']=flag['.']=flag['T']=0;
       for (j=0; j<4; j++) {
            flag[(int)cs[i][j]]++;
       }
       if(flag['X']==4 || (flag['X']==3 && flag['T']==1)) xwin=1;
       if(flag['O']==4 || (flag['O']==3 && flag['T']==1)) owin=1;
       if(flag['.']>0) incomp=1;
   }
}

void colcheck()
{
    int i, j;
    for (j=0; j<4; j++) {
        flag['X']=flag['O']=flag['.']=flag['T']=0;
        for (i=0; i<4; i++) {
            flag[(int)cs[i][j]]++;
        }
        if(flag['X']==4 || (flag['X']==3 && flag['T']==1)) xwin=1;
        if(flag['O']==4 || (flag['O']==3 && flag['T']==1)) owin=1;
        if(flag['.']>0) incomp=1;
    }
}

void diagcheck()
{
    int i;
    flag['X']=flag['O']=flag['.']=flag['T']=0;
    for(i=0; i<4; i++) {
        flag[(int)cs[i][i]]++;
    }
    if(flag['X']==4 || (flag['X']==3 && flag['T']==1)) xwin=1;
    if(flag['O']==4 || (flag['O']==3 && flag['T']==1)) owin=1;
    if(flag['.']>0) incomp=1;

    flag['X']=flag['O']=flag['.']=flag['T']=0;
    for(i=0; i<4; i++) {
        flag[(int)cs[i][3-i]]++;
    }
    if(flag['X']==4 || (flag['X']==3 && flag['T']==1)) xwin=1;
    if(flag['O']==4 || (flag['O']==3 && flag['T']==1)) owin=1;
    if(flag['.']>0) incomp=1;
}

int main()
{
    int t, i, caseno=0;
    scanf("%d", &t);
    while (t--) {
        for (i=0; i<4; i++) {
            scanf("%s", cs[i]);
        }
        xwin=owin=incomp=0;
        rowcheck();
        colcheck();
        diagcheck();
        printf("Case #%d: ", ++caseno);
        if ((xwin==1 && owin==1) || (xwin==0 && owin==0 && incomp==0)) {
            printf("Draw\n");
        }
        else if (xwin==1) {
            printf("X won\n");
        }
        else if (owin==1) {
            printf("O won\n");
        }
        else {
            printf("Game has not completed\n");
        }
    }
    return 0;
}
