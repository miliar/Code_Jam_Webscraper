#include <cstdio>
#include <iostream>

using namespace std;

inline int abs(int a){
    return a<0?-1*a:a;
}


int main(){
    char t[51][51];
    int n,r,c;
    scanf("%d", &n);
    for(int i=0; i<n; ++i){
        scanf("%d %d ", &r, &c);
        for(int j=0; j<r; ++j){
            for(int k=0; k<c; ++k){
                scanf("%c ", &t[j][k]);
            }
        }
        bool f=0;
        for(int j=0; j<r; ++j){
            for(int k=0; k<c; ++k){
                if(t[j][k]=='#' && j<r-1 && k<c-1){
                    if(t[j+1][k]=='#' && t[j][k+1]=='#' && t[j+1][k+1]=='#'){
                        t[j][k]='/';
                        t[j][k+1]='\\';
                        t[j+1][k]='\\';
                        t[j+1][k+1]='/';
                    }
                    else {
                        f = 1;
                        break;
                    }
                } else
                    if(t[j][k]=='#') f=1;
                if(f) break;
            }
        }
        printf("Case #%d:\n", i+1);
        if(!f){
            for(int j=0; j<r; j++){
                for(int k=0; k<c; k++){
                    printf("%c", t[j][k]);
                }
                printf("\n");
            }
        }
        else
            printf("Impossible\n");
    }
}
