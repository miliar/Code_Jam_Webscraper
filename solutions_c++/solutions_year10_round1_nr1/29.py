/**********************************************************************
Author: hanshuai
Created Time:  2010/5/22 8:48:52
File Name: a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;
char a[100][100];
int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0,  1,  1,  1, 0, -1, -1, -1};
int n, k;
int ok(char c){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j ++){
            for(int d = 0; d < 8; d ++){
                bool over = false;
                for(int l = 0; l < k; l ++){
                    int tx = i + dx[d]*l, ty = j + dy[d]*l;
                    if(tx < 0 || tx >= n || ty < 0 || ty >= n || a[tx][ty] != c){
                        over = true;
                        break;
                    }
                }
                if(!over) return 1;
            }
        }
    }
    return 0;
}
int main() {
    freopen("a.out", "w", stdout);
    int test, cas = 0;
    scanf("%d", &test);
    while(test --){
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", ++cas);
        for(int i = 0; i < n; i++){
            scanf("%s", a[i]);
            int x = n - 1;
            for(int j = n - 1; j >= 0; j --){
                if(a[i][j] != '.'){
                    a[i][x] = a[i][j];
                    x --;
                }
            }
            while(x >= 0){
                a[i][x] = '.';
                x --;
            }
        }
        int t1 = ok('B'), t2 = ok('R');
        if(t1 && !t2) printf("Blue\n");
        else if(t2 && !t1) printf("Red\n");
        else if(t1 && t2) printf("Both\n");
        else printf("Neither\n");
    }
    return 0;
}

