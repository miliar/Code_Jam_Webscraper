#include <cstdio>
#include <cmath>

int getlen(int val){
    if(val >= 0 && val <10)
        return 1;
    else if(val>=10 && val < 100)
        return 2;
    else if(val>=100 && val <1000)
        return 3;
    else if(val>=1000 && val <10000)
        return 4;
}

int mi(int base, int n){
    int r = 1;
    int i;
    for(i=0;i<n;++i)
        r*=base;

    return r;
}
int getdigitsbackn(int val, int n){
    int p = 1;
    int i;
    for(i=0;i<n;++i)
        p*=10;
    int v = val % p;
    return v / (p/10);
}
/**
 * 保证最后第n位不为0
 */
int getrecycle(int val, int n){

    int len = getlen(val);
    int fore = val / mi(10, n);
    int back = (val % mi(10, n))*mi(10, len - n);

    int r = fore + back;
    //printf("pow:%d\n", (int)pow(10.0, n));
    //printf("len:%d, in: %d, out:%d, n:%d, fore:%d, back:%d\n", len, val, r, n, fore, back);
}
int main(){
    int T, A, B;
    FILE *fin = fopen("C-small-attempt0.in", "r");
    FILE *fout = fopen("C-small.out", "w");

    fscanf(fin,"%d\n", &T);
    int i;
    for(i=1;i<=T;++i){
        fscanf(fin, "%d%d\n", &A, &B);
        int count = 0;

        int j;
        for(j=A;j<=B;++j){
            int len = getlen(j);
            int k;
            for(k=1;k<len;++k){
                if(getdigitsbackn(j, k) != 0){
                    int one = getrecycle(j, k);
                    if(one > j && one >= A && one <= B)
                    {
                        count++;
                        //printf("n: %d m: %d\n", j, one);
                    }

                }
            }
        }

        fprintf(fout, "Case #%d: %d\n", i, count);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
