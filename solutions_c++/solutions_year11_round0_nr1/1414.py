
#include <cstdio>
#include <cmath>
#include <algorithm>

#define MAX 200
#define ABS(X) ( ((X)>0) ? (X) : -(X) )

using namespace std;

typedef struct {
    char robot;
    int pos;
} Instruction;

Instruction inst[MAX];
int ninst;

int simulate() {
     int posO=1, posB=1, tO=0,tB=0;
     for (int i=0; i<ninst; i++) {
         if (inst[i].robot == 'O') {
             int dt = ABS(posO-inst[i].pos)+1;
             posO = inst[i].pos;
             tO = max(tO+dt,tB+1);
         } else {
             int dt = ABS(posB-inst[i].pos)+1;
             posB = inst[i].pos;
             tB = max(tB+dt,tO+1);
         }
     }
     return max(tO, tB);
}

int main() {
    int T;
    scanf("%i",&T);
    for (int c=0; c<T; c++) {
        scanf("%i",&ninst);
        for (int i=0; i<ninst; i++) {
            char R[10]; int P;            
            scanf("%s %i",R,&P);
            inst[i].robot=R[0]; inst[i].pos=P;
            //printf("%c %i\n",R[0],P);
        }
        int x = simulate();
        printf("Case #%i: %i\n",c+1, x);
    }
}

         
