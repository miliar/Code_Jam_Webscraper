#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int testcase, i, j, k;
    int length, height;
    int impossible;
    char map[100][100];

    scanf("%d", &testcase);

    for(i = 0; i < testcase; ++i){
        scanf("%d %d", &height, &length);
        for(j = 0; j < height; ++j){
                scanf("%s", map[j]);
        }

        for(j = 0; j < height; ++j){
            for(k = 0; k < length; ++k){
                if(map[j][k] == '#' && j+1 < height && map[j+1][k] == '#'  && k+1 < length && map[j][k+1] == '#' && map[j+1][k+1] == '#'){
                    map[j][k] = '/';
                    map[j+1][k] = '\\';
                    map[j][k+1] = '\\';
                    map[j+1][k+1] = '/';
                }
            }
        }

        impossible = 0;

        for(j = 0; j < height; ++j){
            for(k = 0; k < length; ++k){
                if(map[j][k] == '#'){
                    impossible = 1;
                }
            }
        }


        printf("Case #%d:\n", i+1);
        if(impossible){
            printf("Impossible\n");
        }
        else{
            for(j = 0; j < height; ++j){
                printf("%s\n", map[j]);
            }

        }
    }

	return 0;
}
