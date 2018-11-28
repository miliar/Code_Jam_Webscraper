#include<cstdio>

int N,T,Pd,Pg,i,t;

int main() {
    scanf("%d",&T);
    for(t=1;t<=T;t++) {
        scanf("%d %d %d",&N,&Pd,&Pg);

        printf("Case #%d: ",t);

        int p,q;
        if(Pd % 5 == 0)
            if((Pd/5) % 5 == 0)
                p=0;
            else
                p=1;
        else p=2;

        if(Pd % 2 == 0)
            if((Pd/2) % 2 == 0)
                q=0;
            else
                q=1;
        else
            q=2;

        int minN = 1;
        if(p == 1) minN *= 5;
        if(p == 2) minN *= 25;
        if(q == 1) minN *= 2;
        if(q == 2) minN *= 4;

//        printf("(%d:%d:%d)",p,q,minN);
        if(N >= minN) {
            if((Pd < 100 && Pg == 100) || (Pd > 0 && Pg == 0))
                printf("Broken\n");
            else
                printf("Possible\n");
        }
        else
            printf("Broken\n");
    }
    return 0;
}
