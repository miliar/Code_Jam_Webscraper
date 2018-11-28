#include <iostream>
#include <cstdio>
using namespace std;

void proc(int caso) {
    int A, B ;
    scanf("%d%d",&A,&B); 
    A = (1<<A ) ;
    if( B%A==A-1 ) {
        printf("Case #%d: ON\n",caso);
    }
    else {
        printf("Case #%d: OFF\n",caso);
    }
}

int main() {
    int T;
    scanf("%d",&T);
    for( int I=0; I<T; I++ ) {
        proc(I+1);
    }
    return 0;
}
