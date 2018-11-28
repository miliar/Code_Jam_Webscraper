#include<stdio.h>
#include<stdlib.h>

int cmp(const void *elem1, const void *elem2){
    return *(int*)elem1 - *(int*)elem2;
}

int main(){
    int     i, j, k, n, N, A, map1[1000], map2[1000];
    FILE    *fout;
    fout = fopen("Aout.txt", "w");
    scanf("%d", &N);
    k = 1;
    while(k <= N){
        scanf("%d", &n);
        for(i = 0; i < n; i ++){
            scanf("%d", &map1[i]);
        }
        for(i = 0; i < n; i ++){
            scanf("%d", &map2[i]);
        }
        qsort(map1, n, sizeof(int), cmp);
        qsort(map2, n, sizeof(int), cmp);
        A = 0;
        for(i = 0; i < n; i ++){
            A += map1[i] * map2[n - i - 1]; 
        }
        fprintf(fout, "Case #%d: %d\n", k, A);
        printf("Case #%d: %d\n", k, A);
        k ++;
    }
    
    system("pause");
    return 0;
}
