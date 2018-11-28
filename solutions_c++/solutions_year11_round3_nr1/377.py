#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
    
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,N,M;
    scanf("%d",&T);
    
    for (int Test = 1;Test <= T ; Test ++){
        scanf("%d%d",&N,&M);    
        char str[1<<8][1<<8];
        for (int i = 0;i < N; i++)
            scanf("%s",str[i]);
        bool flag = 0;
        for (int i = 0;i < N; i++)
            for (int j = 0;j < M; j++)
                if (str[i][j] == '#'){
                    if (str[i+1][j] == '#' && 
                        str[i][j+1] == '#' && 
                        str[i+1][j+1] == '#'){
                        str[i][j] = '/';
                        str[i][j+1] = '\\';
                        str[i+1][j] = '\\';
                        str[i+1][j+1] = '/';
                    }
                    else flag = 1;
                }
        printf("Case #%d:\n",Test);
        if (flag) puts("Impossible");
        else
            for (int i = 0;i < N;i++)
                printf("%s\n",str[i]);
    }
    return 0;
}
