#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){
    int cases,k;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    while(~scanf("%d",&cases)){
        for(k=1; k<=cases;k++){
            int r,c,i,j;
            char pic[60][60];
            memset(pic,0,sizeof(pic));
            scanf("%d%d",&r,&c);
            for(i=1; i<=r; i++){
                getchar();
                for(j=1; j<=c; j++){
                    scanf("%c",&pic[i][j]);
                }
                //getchar();
            }
            bool flag = false;
            for(i=1; i<=r; i++){
                for(j=1; j<=c; j++){
                    if(pic[i][j] != '#' &&pic[i][j] != '.'){
                        continue;
                    }
                    if(pic[i][j] == '#'){
                        if(pic[i+1][j] == '#' && pic[i][j+1] == '#' && pic[i+1][j+1] == '#') {
                            pic[i][j] = '/';
                            pic[i][j+1] = '\\';
                            pic[i+1][j] = '\\';
                            pic[i+1][j+1] = '/';
                        }
                        else{
                            flag = true;
                            break;
                        }
                    }
                }
                if (flag) break;
            }
            printf("Case #%d:\n",k);
            if (flag){
                printf("Impossible\n");
            }
            else{
                for(i=1; i<=r; i++){
                    for(j=1; j<=c; j++){
                        printf("%c",pic[i][j]);
                    }
                    printf("\n");
                }
            }
        }
    }
    return 0;
}
