#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define N 10

int  n = 4;
char maze[N][N];

int find(char ch){
    int  num1, num2;
    for(int i = 0 ; i < n; i++){
        num1 = num2 = 0;
        for(int  j = 0; j < n; j++){
            if(maze[i][j] == ch) {
                num1++;
            }
            else if('T' == maze[i][j]){
                num2++;
            }
        }
        if(4 == num1) return 1;
        if(3 == num1 && 1 == num2) return 1;
    }
    
    for(int i = 0 ; i < n; i++){
        num1 = num2 = 0;
        for(int  j = 0; j < n; j++){
            if(maze[j][i] == ch) {
                num1++;
            }
            else if('T' == maze[j][i]){
                num2++;
            }
        }
        if(4 == num1) return 1;
        if(3 == num1 && 1 == num2) return 1;
    }
    num1 = num2 = 0;
    for(int i = 0; i < n; i++){
        if(maze[i][i] == ch) {
            num1++;
        }
        else if('T' == maze[i][i]){
            num2++;
        }
    }
    if(4 == num1) return 1;
    if(3 == num1 && 1 == num2) return 1;
    
    num1 = num2 = 0;
    for(int i = 0; i < n; i++){
        if(maze[i][n-i-1] == ch) {
            num1++;
        }
        else if('T' == maze[i][n-i-1]){
            num2++;
        }
    }
    if(4 == num1) return 1;
    if(3 == num1 && 1 == num2) return 1;
    return 0;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas = 1; cas <= T; cas ++){
        int numEmply = 0;
        for(int i = 0; i < n; i++){
           scanf("%s",maze[i]);
           for(int  j = 0; j < n; j++){
               if('.' == maze[i][j]){
                   numEmply ++;
               }
           }
        }
        int flag1, flag2;
        flag1 = flag2 = 0;
        flag1 = find('X');
        flag2 = find('O');
        if(1 == flag1) {
            printf("Case #%d: X won\n",cas);
        }
        else if(1 == flag2) {
            printf("Case #%d: O won\n",cas);
        }
        else if(numEmply){
            printf("Case #%d: Game has not completed\n",cas);
        }
        else {
            printf("Case #%d: Draw\n",cas);
        }
        
    }
    return 0;
}