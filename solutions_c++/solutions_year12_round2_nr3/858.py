#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;

int n;
int in[25];
int dp[25][2000005];
int path[25][2000005];
int check = 0;
int search(int x, int y){
    if(x){  
        if(y == in[x]){
            check = 1;
            printf("%d",in[x]);
        } else if(path[x][y] == 0){
            search(x-1,y);
        } else {
            search(x-1,path[x][y]);
            check = 1;
            printf(" %d", in[x]);
        }
    }
}

class Solve {

    public:
    void main2(){
        bool solve = false;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&in[i]);
        for(int i=0;i<25;i++)
            for(int j=0;j<2000005;j++){
                dp[i][j] = 0;
                path[i][j] = 0;
            }
        for(int i=0;i<25;i++)
            dp[i][0] = 100;
        for(int i=1;i<=n;i++){
            for(int j=in[i];j<2000005;j++){
                if(dp[i-1][j - in[i]] >= 1){
                    dp[i][j] = dp[i-1][j] + 1;
                    if(dp[i][j] == 1){
                        path[i][j] = j - in[i];
                    }
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
            for(int j=0;j<in[i];j++){
                dp[i][j] = dp[i-1][j];
            }
        }
        for(int i=0;i<=n;i++){
            for(int j=1;j<2000005;j++){
                if(dp[i][j] >= 2){
                    check = 0;
                    search(i - 1,j - in[i]);
                    if(check)
                        printf(" %d", in[i]);
                    else 
                        printf("%d",in[i]);
                    printf("\n");
                    search(i - 1,j);
                    printf("\n");
                    return ;
                }
            }
        }
        printf("Impossible\n");

    }
};

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        Solve ___test;
        printf("Case #%d:\n", t);
        ___test.main2();
    }
return 0;
}
