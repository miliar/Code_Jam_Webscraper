#include<iostream>
#include<cstdlib>
#include<cstdio>

void work() {
    int N, s, p, goo[200],score, tot=0;
    scanf("%d%d%d", &N, &s, &p);
    for(int i =0;i < N; i++){
        scanf("%d", &score);
        if (score >= 3*p)tot++;
        else if (score >= 3*p-2 && p-1 >=0)tot++;
        else if (score >= 3*p-4 && p-2 >=0 && s > 0){
            s--;
            tot++;
        }
    }
    printf("%d",tot);
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i =1; i <=t;i++) {
        printf("Case #%d: ",i);
        work();
        printf("\n");
    }
}

