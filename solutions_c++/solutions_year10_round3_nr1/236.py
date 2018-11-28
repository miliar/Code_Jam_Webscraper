#include <iostream>
#include <cstdio>

using namespace std;

int p[1100][2];
int n;

int main(){
    int t;
    freopen("A.in", "r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 0; i < t; ++i){
        printf("Case #%d: ",i + 1);
        scanf("%d",&n);
        for (int j = 0; j < n; ++j) scanf("%d%d",&p[j][0], &p[j][1]);
        if (n == 1){
           puts("0");
        }
        else{
           if ((p[0][0] < p[1][0] && p[0][1] < p[1][1]) || (p[0][0] > p[1][0] && p[0][1] > p[1][1])){
               puts("0");
           }  
           else puts("1");
        }
    }
    return 0;
}
