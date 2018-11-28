#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*int cmp(const void *elem1, const void *elem2){
    return *(long long int*)elem1 - *(long long int*)elem2;
}*/

int main(){
    char    temp1[100], temp2[100];
    int     A1, i, j, k, l, k1, n, N, flag, M, p, q, r, s, len1, len2;
    double A, a, b, B, C, D, x0, y0, point[100000][2];
    FILE    *fout;
    fout = fopen("A1out.txt", "w");
    scanf("%d", &N);
    k1 = 1;
    while(k1 <= N){
        scanf("%d%lf%lf%lf%lf%lf%lf%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        point[0][0] = x0;
        point[0][1] = y0;
        for(i = 1; i < n; i ++){
            point[i][0] = (A * point[i - 1][0] + B);
            point[i][1] = (C * point[i - 1][1] + D);
            while(point[i][0] >= M)
                point[i][0] -= M;
            while(point[i][1] >= M)
                point[i][1] -= M;
            //printf("%lf, %lf\n", point[i][0], point[i][1]); 
        }
        A1 = 0;
        for(i = 0; i < n - 2; i ++){
            for(j = i + 1; j < n - 1; j ++){
                for(k = j + 1; k < n; k ++){
                    a = point[i][0] + point[j][0] + point[k][0];
                    b = point[i][1] + point[j][1] + point[k][1];
                    sprintf(temp1, "%lf", a);
                    sprintf(temp2, "%lf", b);
                    len1 = strlen(temp1);
                    len2 = strlen(temp2);
                    r = 0;
                    s = 0;
                    for(p = 0; p < len1; p ++){
                        if(temp1[p] == '.')
                            break;
                        r += temp1[p] - 48;
                    }
                    //printf("string1: %s = %d\n", temp1, r);
                    for(q = 0; q < len2; q ++){
                        if(temp2[q] == '.')
                            break;
                        s += temp2[q] - 48;
                    }
                    //printf("string2: %s = %d\n", temp2, s);
                    //printf("string: %s\n", temp);
                    //printf("r = %d, s = %d\n", r, s);
                    if((r % 3 == 0) && (s % 3 == 0)){
                        //printf("YAYA");
                        A1 += 1;
                    }
                }
            }
        }
        
        fprintf(fout, "Case #%d: %d\n", k1, A1);
        printf("Case #%d: %d\n", k1, A1);
        k1 ++;
    }
    
    system("pause");
    return 0;
}
