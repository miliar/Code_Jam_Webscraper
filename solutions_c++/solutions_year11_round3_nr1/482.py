#include <cstdio>

using namespace std;

char temp[300][300];

int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0; test < t; ++test){
        int r,c;
        scanf("%d %d",&r,&c);
        for(int i = 0; i < r; ++i)
            scanf("%s", temp[i]);

        for(int i = 0; i < r-1; ++i){
            for(int j = 0; j < c-1; ++j){
                if( temp[i][j] == '#' && temp[i+1][j] == '#' && temp[i][j+1] == '#' && temp[i+1][j+1] == '#'){
                    temp[i][j] = temp[i+1][j+1] =  '/';
                    temp[i][j+1] = temp[i+1][j] = '\\';

                }
            }
        }
        bool ok = true;
        for(int i = 0; i < r; ++i){
            for(int j = 0; j < c; ++j){
                if( temp[i][j] == '#') ok = false;
            }
        }
        if(!ok) printf("Case #%d:\nImpossible\n",test+1); else{
            printf("Case #%d:\n",test+1);
            for(int i = 0; i < r; ++i){
                printf("%s\n", temp[i]);
            }

        }
    }
    return 0;
}
