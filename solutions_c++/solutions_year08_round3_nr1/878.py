#include <stdio.h>
#include <stdlib.h>

#define M 1005

int num[M];

int cmp(const void *a, const void *b){
    return *(int *)a - *(int *)b;
}
int main(void){
    int cas, p, k, l;
    int i, j;
    int per, ans, tmp;
    
    freopen("1.txt","w", stdout);
    scanf("%d", &cas);
    for( i=1; i<=cas; i++ ){
         scanf("%d%d%d", &p ,&k, &l);
         for( j=0; j<l; j++ ) scanf("%d", &num[j]);
         qsort(num, l, sizeof(int), cmp);
         j=l-1;per=1;tmp=k;
         ans=0;
         while( j>=0 ){
                ans += num[j]*per;
                //printf("ans%d tmp%d per%d j%d\n", ans, tmp, per, j);
                tmp--;
                if( tmp==0 ){tmp=k;per ++;}
                //per++;
                j--;
         }
         printf("Case #%d: %d\n", i, ans);
    }
    
    return 0;
} 
