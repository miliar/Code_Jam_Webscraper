#include<stdio.h>
#include<stdlib.h>
using namespace std;

int t,m,n;
char arr[60][60];
int main() {
    scanf(" %d", &t);
    for(int i=1;i<=t;i++) {
        scanf(" %d %d", &m, &n);
        int total = 0;
        for(int j=0;j<m;j++){
            getchar();
            for(int k=0;k<n;k++) {
                scanf("%c", &arr[j][k]);
                if(arr[j][k] == '#') total++;
            }
        }

        if(total%4) {
            printf("Case #%d:\nImpossible\n", i);
            continue;
        }
        bool flag = true;
        while(total && flag){
            for(int j=0;j<m && flag;j++){
                for(int k=0;k<n && flag;k++) {
                    if(arr[j][k] == '#'){
                        if(j+1>=m || k+1>=n
                                ||arr[j+1][k]!='#'
                                ||arr[j][k+1]!='#'
                                ||arr[j+1][k+1]!='#'){
                            flag = false;
                            break;
                        }
                        arr[j][k] = '/';
                        arr[j+1][k] = '\\'; 
                        arr[j][k+1] = '\\';
                        arr[j+1][k+1] = '/';
                        total -= 4;
                    }
                }
            }
        }
        if(!flag) {
            printf("Case #%d:\nImpossible\n", i);
            continue;
        }
        printf("Case #%d:\n", i);
        for(int j=0;j<m;j++){
            for(int k=0;k<n;k++) {
                printf("%c", arr[j][k]);
            }
            printf("\n");
        }
        


    }
    return 0;
}
