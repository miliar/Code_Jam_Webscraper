#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;
int t;
char a[10][10];
int row() {
    for(int i = 0; i < 4; i++) {
        int sum = 0;
        for(int j = 0; j < 4; j++) {
            if(a[i][j] == 'X') sum += 1;
            if(a[i][j] == 'O') sum -= 1;
        }
        if(sum >= 3) return 1;
        if(sum <= -3) return -1;
    }
    return 0;
}
int col() {
    for(int i = 0; i < 4; i++) {
        int sum = 0;
        for(int j = 0; j < 4; j++) {
            if(a[j][i] == 'X') sum += 1;
            if(a[j][i] == 'O') sum -= 1;
        }
        if(sum >= 3) return 1;
        if(sum <= -3) return -1;
    }
    return 0;
}
int dia() {
    int sum = 0;
    if(a[0][0] == 'X') sum += 1;
    if(a[1][1] == 'X') sum += 1;
    if(a[2][2] == 'X') sum += 1;
    if(a[3][3] == 'X') sum += 1;
    if(a[0][0] == 'O') sum -= 1;
    if(a[1][1] == 'O') sum -= 1;
    if(a[2][2] == 'O') sum -= 1;
    if(a[3][3] == 'O') sum -= 1;
    if(sum >= 3) return 1;
    if(sum <= -3) return -1;
    
    sum = 0;
    if(a[0][3] == 'X') sum += 1;
    if(a[1][2] == 'X') sum += 1;
    if(a[2][1] == 'X') sum += 1;
    if(a[3][0] == 'X') sum += 1;
    if(a[0][3] == 'O') sum -= 1;
    if(a[1][2] == 'O') sum -= 1;
    if(a[2][1] == 'O') sum -= 1;
    if(a[3][0] == 'O') sum -= 1;
    if(sum >= 3) return 1;
    if(sum <= -3) return -1;
    return 0;
}
bool check() {
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(a[i][j] == '.') return false;
        }
    }
    return true;
}
int main() {
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        scanf("%s", &a[0]);
        scanf("%s", &a[1]);
        scanf("%s", &a[2]);
        scanf("%s", &a[3]);
        printf("Case #%d: ", i);
        int x = row();
        int y = col();
        int z = dia();
        if(x == 1 || y == 1 || z == 1) {
            printf("X won\n");
            continue;
        }
        if(x == -1 || y == -1 || z == -1) {
            printf("O won\n");
            continue;
        }
        if(check()) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    
    
    //system("pause");
    return 0;
}
