#include<iostream> 
#include<cstdio>
#include<queue>
#include<fstream>

#define MAXN 52 
int R , C;
int n[MAXN][MAXN]; 

bool putin(int x, int y)
{
    if(x + 1 >= R || y + 1 >= C)return false;
    if(n[x + 1][y] != 1)return false;
    if(n[x][y + 1] != 1)return false;
    if(n[x + 1][y + 1] != 1)return false;
    n[x][y] = 2;
    n[x + 1][y] = 3;
    n[x][y + 1] = 3;
    n[x + 1][y + 1] = 2;
    return true;

}

int main()
{
    int cases = 0;
    int casenum = 1;
    freopen("A-large.in", "r", stdin);
    freopen("output", "w", stdout);
    scanf("%d", &cases);
    while(cases--)
    {
        char tmp[MAXN];
        memset(n, 0, sizeof(n));
        scanf("%d%d", &R, &C);
        for(int i = 0;i < R; i++){
            scanf("%s", tmp);
            for(int j = 0;j < C; j++){
                if(tmp[j] == '.')n[i][j] = 0;
                else    n[i][j] = 1;
            }
        }
        printf("Case #%d:\n", casenum++);
        bool ispossible = true;
        for(int i = 0;i < R; i++){
            for(int j = 0;j < C; j++){
                if(n[i][j] != 1)continue;
                if(n[i][j] == 1){
                    ispossible = putin(i, j);

                    if(ispossible == false){
                        //cout<<i<<" "<<j<<endl;
                        break;
                    }
                }
            }
            if(ispossible == false)break;
        }

        if(ispossible == false)
            printf("Impossible\n");
        else{
            for(int i = 0;i < R; i++){
                for(int j = 0;j < C; j++){
                    if(n[i][j] == 0)printf(".");
                    if(n[i][j] == 2)printf("/");
                    if(n[i][j] == 3)printf("\\");
                }
                printf("\n");
            }
        }

    }
    return 0;
}
