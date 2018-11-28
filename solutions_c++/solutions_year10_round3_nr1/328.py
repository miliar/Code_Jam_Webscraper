
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int left;
    int right;
    int idx;
} line;

int compleft(const void * a, const void * b) {

 return ( ((line *) a)->left - ((line *)b)->left);
}

int compright(const void *a, const void *b) {

 return ( ((line *) a)->right - ((line *)b)->right);
}

main() {

 int T;
 int N;
 line lines[2000];
 int posl[2000];
 int posr[2000];
 int crossings;
 int n,i;
 scanf("%d",&T);

 for (int t = 1; t <= T; t++) {

     crossings = 0;
     scanf("%d",&N);
     for (n=0; n < N; n++) {
       scanf("%d %d",&lines[n].left,&lines[n].right);
       lines[n].idx = n;
     }

     qsort(lines,N,sizeof(line),compleft);
     for (n=0; n < N; n++) {
       posl[lines[n].idx] = n;
     }
     qsort(lines,N,sizeof(line),compright);

     for (n=0; n < N; n++) {
       for (i=0; i < n; i++) {
         if (posl[lines[i].idx] > posl[lines[n].idx]) {
             crossings++;
         }
       }
     }

     printf ("Case #%d: %d\n",t,crossings);
 }


}
