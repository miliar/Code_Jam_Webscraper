#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include <string>
#include <iostream>
#include <algorithm>
#include <string>
#include <string>
#include <sys/ioctl.h>
#include <unistd.h>
#include <termios.h>
#include <signal.h>
#include <time.h>
#include <algorithm>
#include <sys/time.h>
#include <stdlib.h>
using namespace std;
int ddx[] = {1, 0, 1};
int ddy[] = {0, 1, 1};
string m[4];
int t2 = 0;
int t = 0;
int comp = 1;
bool check(int x, int y, int dx, int dy){
    int cx = 0;
    int cy = 0;
    for(int i = 0; i< 4; i++){
        char ch = m[x+i*dx][y+i*dy];
        if(ch == 'X'){
            cx++;
        }
        if(m[x+i*dx][y+i*dy] == 'O'){
            cy++;
        }
        if(m[x+i*dx][y+i*dy] == 'T'){
            cx++;
            cy++;
        }
        if(m[x+i*dx][y+i*dy] == '.'){
            comp = 0;
        }
    }
    if(cx == 4){
        printf("Case #%d: X won\n", t+1);
        return true;
    }
    if(cy == 4){
        printf("Case #%d: O won\n", t+1);
        return true;
    }
    return false;
}
int main(){
    cin >> t2;
    for(t = 0; t < t2; t++){
        for(int j = 0; j < 4; j++){
            cin >> m[j];
        }
        comp = 1;
        bool f = false;
        for(int k = 0; k < 4; k++){
            if(check(0, k, 1, 0)){
                f = true;
                break;
            }
        }
        if(f)continue;

        for(int k = 0; k < 4; k++){
            if(check(k, 0, 0, 1)){
                f = true;
                break;
            }
        }
        if(f)continue;
        if(check(0, 0, 1, 1)){
            continue;
        }
        if(check(0, 3, 1, -1)){
            continue;
        }
        if(comp){
            printf("Case #%d: Draw\n",t+1);
        }else{
            printf("Case #%d: Game has not completed\n",t+1);
        }
    }
    return 0;
}
